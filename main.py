from datetime import datetime, timedelta, timezone
import os
import requests

owner = os.getenv('owner')
repo = os.getenv('repo')

offset = int(os.getenv('offset'))  # hour

if __name__ == "__main__":
    res = requests.get(
        "https://api.github.com/repos/{}/{}/git/refs/tags".format(owner, repo))
    print(res.status_code)
    if res.status_code == 200:
        for tag in res.json():
            if tag['object']['type'] == 'tag':
                res = requests.get(tag['object']['url'])
                if res.status_code == 200:
                    tag = res.json()
                    tagDate = datetime.strptime(
                        tag['tagger']['date'], "%Y-%m-%dT%H:%M:%SZ")
                    version = tag['tag']
                    tagd = tagDate + timedelta(hours=offset)
                print(tagd,version)
                if tagDate + timedelta(hours=offset) >= datetime.now():
                    print(version)
