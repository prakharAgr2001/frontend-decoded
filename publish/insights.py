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
        if 'data' in r and r['data']:
            row[met] = r['data'][0]['values'][0]['value'] if r['data'][0].get('values') else r['data'][0].get('total_value', {}).get('value')
    print('REEL', json.dumps(row))
