from datetime import datetime, timedelta, timezone
import os
import requests

owner = os.getenv('owner')
repo = os.getenv('repo')

offset = int(os.getenv('offset'))  # hour

if __name__ == "__main__":
    res1 = requests.get(
        "https://api.github.com/repos/{}/{}/git/refs/tags".format(owner, repo))
    print(res1.status_code)
    if res1.status_code == 200:
        tags = res1.json()
        for tag in tags:
            ot = tag['object']['type']
            ou = tag['object']['url']
            if ot == 'tag':
                res2 = requests.get(ou)
                if res2.status_code == 200:
                    t = res2.json()
                    tagDate = datetime.strptime(
                        t['tagger']['date'], "%Y-%m-%dT%H:%M:%SZ")
                    version = t['tag']
                    tagd = tagDate + timedelta(hours=offset)
                print(tagd,version)
                if tagDate + timedelta(hours=offset) >= datetime.now():
                    print(version)
