"""Post the next unposted reel from publish/queue.json to Instagram (Graph API, resumable upload).
Env: IG_TOKEN, IG_USER_ID, optional GRAPH_VERSION, EPISODE (force one id), COUNT (default 1), DRY_RUN=1 (only check token).
Video comes from the repo; cover = first frame (thumb_offset=0). Nothing is rendered here."""
import json, os, sys, time
import requests

TOKEN, IG_ID = os.environ['IG_TOKEN'].strip(), os.environ['IG_USER_ID'].strip()
VER = os.environ.get('GRAPH_VERSION', 'v24.0')
QUEUE = 'publish/queue.json'

def pick_host():
    # Instagram-login tokens live on graph.instagram.com, Facebook/system-user tokens on graph.facebook.com
    for host in ('https://graph.instagram.com', 'https://graph.facebook.com'):
        r = requests.get(f'{host}/{VER}/{IG_ID}', params={'fields': 'id,username', 'access_token': TOKEN}, timeout=30)
        if r.ok:
            print('token OK on', host, '->', r.json().get('username')); return host
        print(host, '->', r.status_code, r.text[:300])
    sys.exit('Token not accepted by either Graph host. Check IG_TOKEN / IG_USER_ID secrets.')

def post(host, e):
    path = e['video']; size = os.path.getsize(path)
    r = requests.post(f'{host}/{VER}/{IG_ID}/media', data={
        'media_type': 'REELS', 'upload_type': 'resumable', 'caption': e['caption'],
        'thumb_offset': '0', 'share_to_feed': 'true', 'access_token': TOKEN}, timeout=60)
    if not r.ok: sys.exit(f'create container failed: {r.text}')
    cid = r.json()['id']; uri = r.json().get('uri') or f'https://rupload.facebook.com/ig-api-upload/{VER}/{cid}'
    print(e['id'], 'container', cid)
    with open(path, 'rb') as f:
        u = requests.post(uri, data=f, headers={'Authorization': f'OAuth {TOKEN}', 'offset': '0', 'file_size': str(size)}, timeout=600)
    if not u.ok: sys.exit(f'upload failed: {u.text}')
    print('uploaded', size // 1024, 'KB')
    for _ in range(90):  # up to 15 min
        s = requests.get(f'{host}/{VER}/{cid}', params={'fields': 'status_code,status', 'access_token': TOKEN}, timeout=30).json()
        code = s.get('status_code'); print('status', code)
        if code == 'FINISHED': break
        if code in ('ERROR', 'EXPIRED'): sys.exit(f'processing failed: {s}')
        time.sleep(10)
    else: sys.exit('processing timed out')
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
    todo = [e for e in q if (e['id'] == want if want else not e['posted'])][:int(os.environ.get('COUNT') or 1)]
    if not todo: print('nothing to post'); sys.exit(0)
    for e in todo:
        mid, link = post(host, e)
        e.update(posted=True, media_id=mid, permalink=link, posted_at=time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()))
        json.dump(q, open(QUEUE, 'w'), indent=1, ensure_ascii=False)
