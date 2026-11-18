"""Print reel performance (views, reach, likes, comments, saves, shares, avg watch time) + follower count.
Env: IG_TOKEN, IG_USER_ID. Output goes to the job log as JSON lines (no token printed)."""
import json, os, requests
T, U, V = os.environ['IG_TOKEN'].strip(), os.environ['IG_USER_ID'].strip(), os.environ.get('GRAPH_VERSION', 'v24.0')
G = 'https://graph.facebook.com'
def get(path, **p):
    r = requests.get(f'{G}/{V}/{path}', params={**p, 'access_token': T}, timeout=30)
    return r.json() if r.ok else {'error': r.json().get('error', {}).get('message', r.text[:200])}
acct = get(U, fields='username,followers_count,follows_count,media_count')
print('ACCOUNT', json.dumps(acct))
q = {e['media_id']: e['id'] for e in json.load(open('publish/queue.json')) if e.get('media_id')}
METRICS = ['views', 'reach', 'saved', 'shares', 'total_interactions', 'ig_reels_avg_watch_time', 'follows', 'profile_visits']
for mid, ep in q.items():
    m = get(mid, fields='like_count,comments_count,timestamp')
    row = {'ep': ep, 'likes': m.get('like_count'), 'comments': m.get('comments_count')}
    for met in METRICS:  # one by one: unsupported metrics shouldn't kill the rest
        r = get(f'{mid}/insights', metric=met)
        if 'error' in r and ep == 'S1E01': print('ERR', met, r['error'][:160])
        if 'data' in r and r['data']:
            row[met] = r['data'][0]['values'][0]['value'] if r['data'][0].get('values') else r['data'][0].get('total_value', {}).get('value')
    print('REEL', json.dumps(row))

for met in ['reach', 'views', 'follower_count', 'profile_views', 'accounts_engaged', 'total_interactions']:
    r = get(f'{U}/insights', metric=met, period='day', metric_type='total_value')
    print('ACCT_INSIGHT', met, json.dumps(r.get('data', r))[:300])
r = get(f'{U}/insights', metric='follower_demographics', period='lifetime', metric_type='total_value', breakdown='country')
print('DEMO', json.dumps(r)[:400])
