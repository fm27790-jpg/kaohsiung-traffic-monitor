import os
import requests
import json


TOKEN = os.environ.get("THREADS_TOKEN")


url = "https://graph.threads.net/v1.0/me"


params = {
    "fields": "id,username",
    "access_token": TOKEN
}


r = requests.get(
    url,
    params=params
)


print(r.text)
