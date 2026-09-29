import os
import requests
import json
from datetime import datetime


TOKEN = os.environ.get("THREADS_TOKEN")


def get_threads_posts():

    url = "https://graph.threads.net/v1.0/keyword_search"

    keywords = [
        "高雄塞車",
        "高雄車禍",
        "高雄事故",
        "高雄施工",
        "高雄號誌",
        "高雄淹水",
        "高雄交通"
    ]

    results = []

    for keyword in keywords:

        params = {
            "q": keyword,
            "fields": "id,text,timestamp,username",
            "access_token": TOKEN
        }

        r = requests.get(
            url,
            params=params
        )

        try:
            data = r.json()

            if "data" in data:
                results.extend(data["data"])

        except:
            pass


    return results



def main():

    posts = get_threads_posts()


    output = {
        "update_time":
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "count":
            len(posts),
        "posts":
            posts
    }


    with open(
        "traffic.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            output,
            f,
            ensure_ascii=False,
            indent=2
        )


if __name__ == "__main__":
    main()
