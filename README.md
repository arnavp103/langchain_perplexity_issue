# Perplexity Max Tokens issue

This repository contains the code to reproduce this [issue](https://github.com/langchain-ai/langchain/issues/28229) in the Langchain repository.

## Steps to reproduce   

1. Clone the repository and set up a venv
2. Fill out the `.env` file with a perplexity API key 
3. Run the following command to install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the following command to reproduce the issue:
    ```bash
    python langchain.py
    ```
The output exceeds the maximum number of tokens set in the `**kwargs` of the class:
```
{
    "choices": [
        {
            "delta": {
                "content": "",
                "role": "assistant"
            },
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "I understand your concern, and I'm here to help you understand the status of your order.\n\nBased on the information provided, your order has been shipped. Here's what that means:\n\n- **Shipped**: This means that your order has been packed and handed over to the shipping company. It is now on its way to you.\n- **Estimated Delivery Date**: The estimated delivery date for your order is September 19, 2022. This is the date by which you should receive your package.\n- **Tracking Information**: You should have received a tracking number with your order confirmation. You can use this tracking number to check the status of your package in real-time.\n\nIf you haven't received your package by the estimated delivery date, you might want to contact the shipping company or check with the customer service of the store where you placed the order for further assistance.\n\nI hope this helps If you have any more questions or need further assistance, feel free to ask.",
                "role": "assistant"
            }
        }
    ],
    "citations": [
        "https://www.fulfyld.com/knowledge/what-does-my-order-status-mean/",
        "https://www.artsyltech.com/what-is-order-tracking",
        "https://parcellab.com/glossary/delivery-status/",
        "https://www.speedcommerce.com/what-is/order-tracking/",
        "https://munbyn.com/blogs/news/order-status-types-and-meanings"
    ],
    "created": 1732591845,
    "id": "9b0d0d5e-78d3-4606-b6e3-60b4df55c46c",
    "model": "llama-3.1-sonar-small-128k-online",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 195,
        "prompt_tokens": 448,
        "total_tokens": 643
    }
}
```

5. The output should be limited to a few tokens, but it is not. See how it should run on `python direct_test.py` for comparison.

Output for 75 tokens:
```
{
  "id": "b69e756d-211b-420b-bf86-a63e902d404f",
  "model": "llama-3.1-sonar-small-128k-online",
  "created": 1732592356,
  "usage": {
    "prompt_tokens": 448,
    "completion_tokens": 75,
    "total_tokens": 523
  },
  "citations": [
    "https://www.fulfyld.com/knowledge/what-does-my-order-status-mean/",
    "https://www.artsyltech.com/what-is-order-tracking",
    "https://parcellab.com/glossary/delivery-status/",
    "https://www.speedcommerce.com/what-is/order-tracking/",
    "https://munbyn.com/blogs/news/order-status-types-and-meanings"
  ],
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "finish_reason": "length",
      "message": {
        "role": "assistant",
        "content": "I understand your concern, and I'm here to help you understand the status of your order.\n\nBased on the information provided, here is what we know about your order:\n\n1. **Order ID**: Your order number is `ord_fGpNg4MUVogzxfg8FJZgwXxViViG9uhwFIoDTfU+"
      },
      "delta": {
        "role": "assistant",
        "content": ""
      }
    }
  ]
}
```