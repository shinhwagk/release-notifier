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
        tags = res.json()
        for tag in tags:
            ot = tag['object']['type']
            ou = tag['object']['url']
            if ot == 'tag':
                res = requests.get(ou)
                if res.status_code == 200:
                    t = res.json()
                    tagDate = datetime.strptime(
                        t['tagger']['date'], "%Y-%m-%dT%H:%M:%SZ")
                    version = t['tag']
                    tagd = tagDate + timedelta(hours=offset)
                print(tagd,version)
                if tagDate + timedelta(hours=offset) >= datetime.now():
                    print(version)
