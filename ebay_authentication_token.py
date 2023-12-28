import requests
from base64 import b64encode
from urllib.parse import urlparse, parse_qs
import webbrowser

# Prompt the user to enter their eBay production application credentials and redirect URI
client_id = input("Enter your eBay client ID: ")
client_secret = input("Enter your eBay client secret: ")
redirect_uri = input("Enter your eBay redirect URI: ")

# Define all the scopes based on your requirements
scopes = (
    "https://api.ebay.com/oauth/api_scope "
    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly "
    "https://api.ebay.com/oauth/api_scope/sell.marketing "
    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly "
    "https://api.ebay.com/oauth/api_scope/sell.inventory "
    "https://api.ebay.com/oauth/api_scope/sell.account.readonly "
    "https://api.ebay.com/oauth/api_scope/sell.account "
    "https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly "
    "https://api.ebay.com/oauth/api_scope/sell.fulfillment "
    "https://api.ebay.com/oauth/api_scope/sell.analytics.readonly "
    "https://api.ebay.com/oauth/api_scope/sell.finances "
    "https://api.ebay.com/oauth/api_scope/sell.payment.dispute "
    "https://api.ebay.com/oauth/api_scope/commerce.identity.readonly "
    "https://api.ebay.com/oauth/api_scope/sell.reputation "
    "https://api.ebay.com/oauth/api_scope/sell.reputation.readonly "
    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription "
    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly "
    "https://api.ebay.com/oauth/api_scope/sell.stores "
    "https://api.ebay.com/oauth/api_scope/sell.stores.readonly"
)

# Set the target endpoint for the consent request in production
consent_endpoint_production = "https://auth.ebay.com/oauth2/authorize"
token_endpoint = "https://api.ebay.com/identity/v1/oauth2/token"

# Define the consent URL
consent_url = (
    f"{consent_endpoint_production}?"
    f"client_id={client_id}&"
    f"redirect_uri={redirect_uri}&"
    f"response_type=code&"
    f"scope={scopes}"
)

# Open the consent URL in the default web browser
webbrowser.open(consent_url)

print("Opening the browser. Please grant consent in the browser.")

# Retrieve the authorization code from the user after they grant consent
authorization_code_url = input("Enter the authorization code URL: ")

# Parse the URL to extract the authorization code
parsed_url = urlparse(authorization_code_url)
query_params = parse_qs(parsed_url.query)
authorization_code = query_params.get('code', [])[0]

# Make the authorization code grant request to obtain the token
payload = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri
}

# Encode the client credentials for the Authorization header
credentials = f"{client_id}:{client_secret}"
encoded_credentials = b64encode(credentials.encode()).decode()

# Set the headers for the token request
token_headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {encoded_credentials}"
}

# Make the POST request to the token endpoint
response = requests.post(token_endpoint, headers=token_headers, data=payload)

# Check the response
if response.status_code == 200:
    # Parse and print the response JSON
    response_json = response.json()
    print("Response containing the User access token:")
    print(response_json)
else:
    print(f"Error: {response.status_code}, {response.text}")
