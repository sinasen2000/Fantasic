from yahoo_oauth import OAuth2
import json

creds = {'consumer_key': 'my_key', 'consumer_secret': 'my_secret'}
with open(['<json>'], "w") as f:
   f.write(json.dumps(creds))
oauth = OAuth2(None, None, from_file='private.json')

oauth.