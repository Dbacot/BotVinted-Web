import requests
import time
import json
from PIL import Image
from io import BytesIO

with open("params.json", "r") as f:
    config = json.load(f)

search_term = config["search"]
access_token = config["access_token"]
refresh_token = config["refresh_token"]
webhook_url = config["webhook"]
sent_items = set()

def fetch_items():
    url = "https://www.vinted.fr/api/v2/catalog/items"
    params = {
        "search_text": search_term,
        "price_to": 450,
        "status_ids[]": 1,
        "order": "newest_first",
    }

    cookies = {
        "access_token_web": access_token,
        "refresh_token_web": refresh_token,
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers, cookies=cookies)
    if response.status_code != 200:
        print(f"Erreur API : {response.status_code}")
        return []

    return response.json().get("items", [])

def send_to_discord(item):
    img_url = item['photo']['url']
    img_data = requests.get(img_url).content
    img = Image.open(BytesIO(img_data))
    img = img.resize((200, 200))
    img.save("temp.jpg")

    message = {
        "content": f"**{item['title']}**\nPrix: {item['price']['amount']} {item['price']['currency_code']}\nVendeur: {item['user']['login']}\n[Voir le produit]({item['url']})"
    }

    with open("temp.jpg", "rb") as img_file:
        files = {"file": ("image.jpg", img_file, "image/jpeg")}
        requests.post(webhook_url, data=message, files=files)

def main_loop():
    while True:
        items = fetch_items()
        new_items = [item for item in items[:3] if item["id"] not in sent_items]

        for item in new_items:
            send_to_discord(item)
            sent_items.add(item["id"])

        print("Attente de 10 secondes...")
        time.sleep(10)

main_loop()
