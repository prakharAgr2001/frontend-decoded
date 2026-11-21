"""Post the next unposted reel from publish/queue.json to Instagram (Graph API, resumable upload).
Env: IG_TOKEN, IG_USER_ID, optional GRAPH_VERSION, EPISODE (force one id), COUNT (default 1), DRY_RUN=1 (only check token).
Video and cover are fetched by Instagram from the public repo (cover_url). Nothing is rendered here."""
import calendar, json, os, sys, time
import requests

TOKEN, IG_ID = os.environ['IG_TOKEN'].strip(), os.environ['IG_USER_ID'].strip()
VER = os.environ.get('GRAPH_VERSION', 'v24.0')
QUEUE = os.environ.get('QUEUE') or 'publish/queue.json'
TRIAL = os.environ.get('TRIAL') == '1'  # Instagram trial reel: shown to non-followers first
RAW = 'https://raw.githubusercontent.com/' + os.environ.get('GITHUB_REPOSITORY', 'prakharAgr2001/frontend-decoded') + '/main/'

def pick_host():
    # Instagram-login tokens live on graph.instagram.com, Facebook/system-user tokens on graph.facebook.com
    for host in ('https://graph.instagram.com', 'https://graph.facebook.com'):
        r = requests.get(f'{host}/{VER}/{IG_ID}', params={'fields': 'id,username', 'access_token': TOKEN}, timeout=30)
        if r.ok:
            print('token OK on', host, '->', r.json().get('username')); return host
        print(host, '->', r.status_code, r.text[:300])
    sys.exit('Token not accepted by either Graph host. Check IG_TOKEN / IG_USER_ID secrets.')

def make_container(host, e, trial):
    data = {'media_type': 'REELS', 'video_url': RAW + e['video'], 'caption': e['caption'],
            'cover_url': RAW + e['cover'], 'share_to_feed': 'true', 'access_token': TOKEN}
    r = None
    if trial:
        r = requests.post(f'{host}/{VER}/{IG_ID}/media', data={**data, 'trial_params': json.dumps({'graduation_strategy': 'SS_PERFORMANCE'})}, timeout=60)
        if not r.ok: print('trial reel not accepted, posting normally:', r.text[:200]); r = None
    if r is None:
        r = requests.post(f'{host}/{VER}/{IG_ID}/media', data=data, timeout=60)
    if not r.ok: print('create container failed:', r.text[:300]); return None
    cid = r.json()['id']; print(e['id'], 'container', cid, '(trial)' if trial else '')
    for _ in range(90):  # up to 15 min
        s = requests.get(f'{host}/{VER}/{cid}', params={'fields': 'status_code,status', 'access_token': TOKEN}, timeout=30).json()
        code = s.get('status_code'); print('status', code)
        if code == 'FINISHED': return cid
        if code in ('ERROR', 'EXPIRED'): print('processing failed:', s); return None
        time.sleep(10)
    print('processing timed out'); return None

def post(host, e):
    # Instagram sometimes fails processing for no reason on our side (e.g. "error code 2207076").
    # Its docs say: make a NEW container and try again. Last attempt drops the trial flag.
    cid = None
    for attempt, trial in enumerate([TRIAL, TRIAL, False], 1):
        cid = make_container(host, e, trial)
        if cid: break
        if attempt < 3: print(f'attempt {attempt} failed, retrying in 60 s with a new container'); time.sleep(60)
    if not cid: sys.exit(f'{e["id"]}: Instagram could not process the video after 3 attempts')
    p = requests.post(f'{host}/{VER}/{IG_ID}/media_publish', data={'creation_id': cid, 'access_token': TOKEN}, timeout=60)
    if not p.ok: sys.exit(f'publish failed: {p.text}')
    mid = p.json()['id']
    link = requests.get(f'{host}/{VER}/{mid}', params={'fields': 'permalink', 'access_token': TOKEN}, timeout=30).json().get('permalink')
    print('PUBLISHED', e['id'], mid, link)
    return mid, link

if __name__ == '__main__':
    host = pick_host()
    if os.environ.get('DRY_RUN') == '1': sys.exit(0)
    q = json.load(open(QUEUE)); want = os.environ.get('EPISODE', '').strip().upper()
    gap = float(os.environ.get('SKIP_IF_POSTED_WITHIN_H') or 0)   # scheduled backup runs: don't double-post
    if gap and not want:
        last = max((calendar.timegm(time.strptime(e['posted_at'], '%Y-%m-%d %H:%M UTC'))
                    for e in q if e.get('posted_at')), default=0)
        if time.time() - last < gap * 3600:
            print(f'Already posted within {gap} h, skipping this run.'); sys.exit(0)
    todo = [e for e in q if (e['id'] == want if want else not e['posted'])][:int(os.environ.get('COUNT') or 1)]
    if not todo: print('nothing to post'); sys.exit(0)
    for e in todo:
        mid, link = post(host, e)
        e.update(posted=True, media_id=mid, permalink=link, posted_at=time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()))
        json.dump(q, open(QUEUE, 'w'), indent=1, ensure_ascii=False)
