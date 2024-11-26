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
    python main.py
    ```


Based on the provided JSON representation of the order, the current status of your order is "shipped." 
This means that the shipping label has been generated, and the order has been handed over to the shipping company. 
The estimated delivery date is September 19, 2022, and the order was placed on September 10, 2022.

Here are the key details from the order JSON:

- **Order Status**: Shipped
- **Order Date**: September 10, 2022
- **Estimated Delivery Date**: September 19, 2022
- **Shipping Address**: 1265 Military Trail, Toronto, ON M1C1A4, Canada

If you haven't received your order yet, it might be due to delays in the shipping process. 
You can track the order using the tracking number provided by the shipping company to get more detailed updates on its status