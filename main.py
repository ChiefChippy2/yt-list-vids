import requests
from dotenv import load_dotenv
import os
load_dotenv()

KEY = os.environ.get('KEY')

# Gets upload channel of user
def get_upload_pl(name: str) -> str:
    url = 'https://youtube.googleapis.com/youtube/v3/channels'
    params = {
        'key': KEY,
        'forUsername': name,
        'part': 'contentDetails',
        'maxResults': 100
    }
    result: requests.Response = requests.get(url, params)
    return result.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Gets all videos from playlist id
def pl_vids(id: str) -> dict:
    url = 'https://youtube.googleapis.com/youtube/v3/playlistItems'
    params = {
        'key': KEY,
        'part': 'snippet,id',
        'maxResults': 100,
        'playlistId': id
    }
    page_cur: requests.Response = requests.get(url, params)
    cur_json: dict = page_cur.json()
    all_vids: list[dict] = cur_json['items']
    while cur_json.get('nextPageToken'):
        params['pageToken'] = cur_json.get('nextPageToken')
        page_cur = requests.get(url, params)
        cur_json = page_cur.json()
        all_vids += cur_json.get('items',[])
    return all_vids
