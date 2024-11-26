from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from dotenv import dotenv_values

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
You do not have ability to process or change the state of orders, you should just explain the status of the order based on the JSON representation of the order.

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
    max_tokens=200,
)

chain = prompt | model

response = chain.invoke({"order_details": order_details})

print(response)


Based on the provided JSON representation of the order, the current status of your order is "shipped." 
This means that the shipping label has been generated, and the order has been handed over to the shipping company. 
The estimated delivery date is September 19, 2022, and the order was placed on September 10, 2022.

Here are the key details from the order JSON:

- **Order Status**: Shipped
- **Order Date**: September 10, 2022
- **Estimated Delivery Date**: September 19, 2022
- **Shipping Address**: 1265 Military Trail, Toronto, ON M1C1A4, Canada

If you haven\'t received your order yet, it might be due to delays in the shipping process. 
You can track the order using the tracking number provided by the shipping company to get more detailed updates on its status