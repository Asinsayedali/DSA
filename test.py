import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://cosmicreserve.com"
CONSUMER_KEY = "ck_14e26794993826cbf426792a20daa799752dc828"
CONSUMER_SECRET = "cs_3f9d73317efb58eb892b40e058e7c91e036f3f3b"

url = f"{BASE_URL}/wp-json/wc/v3/orders"

response = requests.get(
    url,
    auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET)
)

print(response.status_code)

print("STATUS:", response.status_code)
print("TEXT:", response.text[:500])
orders = response.json()

for order in orders:
    print(f"Order ID: {order['id']}")
    print(f"Customer: {order['billing']['first_name']}")
    print(f"Total: {order['total']}")
    print("-" * 20)