from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import dotenv_values
import langchain
import os

# The location of my CA File
cert_file = "/usr/local/share/ca-certificates/mitmproxy.crt"
os.environ["REQUESTS_CA_BUNDLE"] = cert_file
os.environ["SSL_CERT_FILE"] = cert_file
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"

langchain.debug = True
config = dotenv_values(".env")

PERPLEXITY_API_KEY = config["PERPLEXITY_API_KEY"]

order_details = """
Order: {
    order_id: "ord_fGpNg4MUVogzxfg8FJZgwXxViViG9uhwFIoDTfU+liD9VrJrc/Xy/N3a+/OHiHa3
2uRCZRlNuzP3k0aq3p+x/w==",
    order_status: "shipped",
    order_date: "2022-09-10",
    estimated_delivery_date: "2022-09-19",
    shipping_address: {
        street: "1265 Military Trail",
        city: "Toronto",
        province: "ON",
        postal_code: "M1C1A4",
        country: "Canada"
    },
    items: [
        {
            item_id: "item_52139",
            item_name: "Baby GUND, Lil Luvs Collection Liam Llama Plush Stuffed Animal, Cream and White, 12 ",
            item_quantity: 1,
            item_price: 17.06,
            currency: "CAD"
        },
        {
            item_id: "item_19684",
            item_name: "Dyson V11™ Cordless Vacuum",
            item_quantity: 1,
            item_price: 599.99,
            currency: "CAD" 
        }
    ],
    total_price: 617.05,
    currency: "CAD",
    link_to_order: "https://www.orderme.com/orders/ord_fGpNg4MUVogzxfg8FJZgwXxViViG9uhwFIoDTfU+liD9VrJrc/Xy/N3a+/OHiHa3"
}
"""


template = """You are an assistant helping customers with their orders. 
You do not have ability to process or change the state of orders, you should just explain the status of the order based on our system information of the order.
The user is not assumed to be technical so please explain in a simple and clear way.

Customer: Hi, I placed an order last week and I haven't received it yet. Can you help me with that?


<order_json>
{order_details}
</order_json>
"""

prompt = ChatPromptTemplate.from_template(template)


model = ChatPerplexity(
    pplx_api_key=PERPLEXITY_API_KEY,
    model="llama-3.1-sonar-small-128k-online",
    temperature=0.1,
    max_tokens=75,
)

chain = prompt | model

response = chain.invoke({"order_details": order_details})

print(response.content)
