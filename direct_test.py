import requests
from dotenv import dotenv_values
import os

# The location of my CA File
cert_file = "/usr/local/share/ca-certificates/mitmproxy.crt"
os.environ["REQUESTS_CA_BUNDLE"] = cert_file
os.environ["SSL_CERT_FILE"] = cert_file
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"


message = {
    "content": 'You are an assistant helping customers with their orders. \nYou do not have ability to process or change the state of orders, you should just explain the status of the order based on our system information of the order.\nThe user is not assumed to be technical so please explain in a simple and clear way.\n\nCustomer: Hi, I placed an order last week and I haven\'t received it yet. Can you help me with that?\n\n\n<order_json>\n\nOrder: {\n    order_id: "ord_fGpNg4MUVogzxfg8FJZgwXxViViG9uhwFIoDTfU+liD9VrJrc/Xy/N3a+/OHiHa3\n2uRCZRlNuzP3k0aq3p+x/w==",\n    order_status: "shipped",\n    order_date: "2022-09-10",\n    estimated_delivery_date: "2022-09-19",\n    shipping_address: {\n        street: "1265 Military Trail",\n        city: "Toronto",\n        province: "ON",\n        postal_code: "M1C1A4",\n        country: "Canada"\n    },\n    items: [\n        {\n            item_id: "item_52139",\n            item_name: "Baby GUND, Lil Luvs Collection Liam Llama Plush Stuffed Animal, Cream and White, 12 ",\n            item_quantity: 1,\n            item_price: 17.06,\n            currency: "CAD"\n        },\n        {\n            item_id: "item_19684",\n            item_name: "Dyson V11™ Cordless Vacuum",\n            item_quantity: 1,\n            item_price: 599.99,\n            currency: "CAD" \n        }\n    ],\n    total_price: 617.05,\n    currency: "CAD",\n    link_to_order: "https://www.orderme.com/orders/ord_fGpNg4MUVogzxfg8FJZgwXxViViG9uhwFIoDTfU+liD9VrJrc/Xy/N3a+/OHiHa3"\n}\n\n</order_json>\n',
    "role": "user",
}


config = dotenv_values(".env")

token = config["PERPLEXITY_API_KEY"]

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "llama-3.1-sonar-small-128k-online",
    "messages": [message],
    "max_tokens": "75",
    "temperature": 0.1,
}
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
