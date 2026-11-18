"""'Comment NOTES' bot: DMs each commenter the cheat sheet for THAT reel, via InstantDM's API.
Runs every ~10 min from GitHub Actions. Env: INSTANTDM_KEY, optional PUBLIC_REPLY=1, DRY_RUN=1, LOOKBACK_DAYS (default 6).
Followers get the episode link; non-followers get a 'follow, then comment NOTES again' DM.
Handled comment ids are kept in publish/notes_sent.json so nobody is messaged twice. Each DM costs 1 InstantDM credit."""
import json, os, random, sys, time
from datetime import datetime, timedelta, timezone
import requests

KEY = os.environ.get('INSTANTDM_KEY', '').strip()
if not KEY: print('INSTANTDM_KEY secret not set yet, skipping'); sys.exit(0)
H = {'Authorization': f'Bearer {KEY}', 'x-api-key': KEY}
V2, V1 = 'https://openapi.instantdm.com', 'https://api.instantdm.com/api-webhook'
REPO = os.environ.get('GITHUB_REPOSITORY', 'prakharAgr2001/frontend-decoded')
PAGE = f'https://github.com/{REPO}/blob/main/cheatsheets/{{}}.md'
DRY = os.environ.get('DRY_RUN') == '1'
PUBLIC = os.environ.get('PUBLIC_REPLY') == '1'
SENT = 'publish/notes_sent.json'
LOOKBACK = timedelta(days=int(os.environ.get('LOOKBACK_DAYS') or 6))  # Meta allows private replies for 7 days

def items(j):
    if isinstance(j, list): return j
    for k in ('data', 'comments', 'items', 'results'):
        v = j.get(k) if isinstance(j, dict) else None
        if isinstance(v, list): return v
        if isinstance(v, dict):
            for k2 in ('data', 'comments', 'items'):
                if isinstance(v.get(k2), list): return v[k2]
    return []

def cursor(j):
    if not isinstance(j, dict): return None
    for src in (j, j.get('data') if isinstance(j.get('data'), dict) else {}):
        p = src.get('paging') or {}
        c = (p.get('cursors') or {}).get('after') or src.get('after') or src.get('next_cursor')
        if c and (p.get('next') or 'paging' not in src): return c
    return None

def comments(post_id):
    out, after = [], None
    for _ in range(20):
        r = requests.get(f'{V2}/ig_comments', headers=H, params={'post_id': post_id, **({'after': after} if after else {})}, timeout=30)
        if not r.ok: print('ig_comments', post_id, r.status_code, r.text[:300]); break
        j = r.json(); out += items(j); after = cursor(j)
        if not after: break
    for c in list(out):  # include threaded replies if returned
        out += items(c.get('replies') or {})
    return out

def ts(c):
    t = c.get('timestamp') or c.get('created_time') or c.get('created_at')
    try: return datetime.fromisoformat(str(t).replace('Z', '+00:00').replace('+0000', '+00:00'))
    except Exception: return datetime.now(timezone.utc)

def following(uid):
    r = requests.get(f'{V2}/contact_profile', headers=H, params={'contact_id': uid}, timeout=30)
    if r.ok:
        d = r.json().get('data') or r.json()
        if 'is_following' in d: return bool(d['is_following'])
    print('contact_profile', uid, r.status_code, r.text[:200])
    return None  # unknown -> be generous, send the sheet

def send(comment_id, text):
    if DRY: print('  [dry] DM:', text.replace('\n', ' | ')); return True
    r = requests.post(V1, headers=H, json={'action': 'send_message', 'type': 'comment_reply',
                                           'comment_id': comment_id, 'message': {'text': text}}, timeout=30)
    print('  send_message', r.status_code, r.text[:200])
    return r.ok

def public_reply(comment_id):
    if DRY or not PUBLIC: return
    t = random.choice(['Sent! Check your DMs 📩', 'Done ✅ cheat sheet is in your inbox', 'On its way to your DMs 🦊'])
    requests.post(V1, headers=H, json={'action': 'post_comment', 'comment_id': comment_id, 'comment_text': t}, timeout=30)

if __name__ == '__main__':
    q = json.load(open('publish/queue.json'))
    sent = json.load(open(SENT)) if os.path.exists(SENT) else {}
    now = datetime.now(timezone.utc); n_new = 0
    for e in q:
        if not e.get('media_id'): continue
        posted = datetime.strptime(e['posted_at'], '%Y-%m-%d %H:%M UTC').replace(tzinfo=timezone.utc) if e.get('posted_at') else now
        if now - posted > timedelta(days=60): continue  # old reels: skip polling
        for c in comments(e['media_id']):
            cid, text = str(c.get('id', '')), (c.get('text') or c.get('message') or '')
            frm = c.get('from') or {}
            uid, user = str(frm.get('id') or c.get('user_id') or ''), frm.get('username') or c.get('username') or ''
            if not cid or cid in sent or 'notes' not in text.lower() or user == 'tech.explained.dev': continue
            if now - ts(c) > LOOKBACK: sent[cid] = 'expired'; continue
            f = following(uid) if uid else None
            print(e['id'], cid, '@' + user, 'following' if f else ('not following' if f is False else 'follow unknown'))
            if f is False:
                ok = send(cid, "Hey! 👋 Your cheat sheet is ready. Follow @tech.explained.dev, then comment NOTES again and it'll land here in a few minutes 🦊")
                state = 'asked_follow'
            else:
                ok = send(cid, f"Here's your cheat sheet for {e['id'][:2]} · {e['id'][2:]} 🦊\n\n"
                               f"Key ideas, DevTools tricks and interview traps 👇\n{PAGE.format(e['id'])}\n\n"
                               "New episode every day, see you tomorrow!")
                state = 'sent'
                if ok: public_reply(cid)
            if ok and not DRY: sent[cid] = state; n_new += 1
            time.sleep(1)
    if not DRY: json.dump(sent, open(SENT, 'w'), indent=0)
    print('handled', n_new, 'new comments')
