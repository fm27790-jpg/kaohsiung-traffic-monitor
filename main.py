import os
import requests
import json
from datetime import datetime


TOKEN = os.environ.get("THREADS_TOKEN")


# Threads Keyword Search
url = "https://graph.threads.net/v1.0/keyword_search"


keywords = [
    "高雄"
]


all_posts = []


for keyword in keywords:

    params = {
        "q": keyword,
        "fields": "id,text,username,timestamp,permalink",
        "access_token": TOKEN
    }


    r = requests.get(url, params=params)


    print("搜尋:", keyword)
    print("狀態:", r.status_code)
    print(r.text)


    if r.status_code == 200:

        data = r.json()

        if "data" in data:
            all_posts.extend(data["data"])



result = {

    "update_time":
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    "count":
        len(all_posts),

    "posts":
        all_posts
}



with open(
    "traffic.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=2
    )


print("完成，共抓到", len(all_posts), "筆")
