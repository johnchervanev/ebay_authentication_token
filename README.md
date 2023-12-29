# eBay OAuth Script: User Authentication and Token Retrieval

## Overview

This Python script facilitates the eBay authentication process and token retrieval using OAuth. It opens the user's default web browser to grant consent, obtains an authorization code, and exchanges it for an access token from the eBay API. The script also provides a refresh token for extended access.

### Consent Process

The script automates the consent process by opening the user's default web browser to grant consent on the eBay website.

### Token Retrieval

After the user grants consent, the script retrieves the authorization code and exchanges it for an access token and refresh token from the eBay API.

## Problem

Interacting with the eBay API requires user authentication, and obtaining access tokens manually can be cumbersome. This script simplifies the authentication process for eBay applications.

## Solution

The script automates the eBay OAuth consent and token retrieval, making it convenient for developers to integrate eBay API authentication into their applications. It also provides a refresh token for extended access.

## Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/johnchervanev/ebay_authentication_token
    cd ebay_authentication_token
    ```

2. **Open the script in your preferred Python editor or IDE.**

    Review Scopes:

    Before running the script, carefully review the specified `scopes` to ensure they align with your eBay application's requirements. The `scopes` variable determines the level of access your application has to eBay APIs. Make sure to include the necessary scopes based on the features your application utilizes. For more information on eBay API scopes, refer to the [eBay API documentation](https://developer.ebay.com/tools/api-scopes).

    ```bash
    scopes = (
        "https://api.ebay.com/oauth/api_scope "
        "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly "
        # ... (customize the scopes based on your requirements)
    )
    ```

3. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

    Activate the Virtual Environment:

    On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies:**

    Run the following command to install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Script:**

    Execute the script in your Python environment.

    ```bash
    ebay_authentication_token.py
    ```

    When you run the script, it will prompt you in the console to input your eBay client ID, client secret, and redirect URI.

    If you don't have an eBay application yet, you can obtain your `client_id`, `client_secret`, and `redirect_uri` which is known as the RuName by creating an application on the [eBay Developer website](https://developer.ebay.com/my/keys).

6. **Consent Process:**

    The script will automatically open your default web browser, prompting you to grant consent on the eBay website. Follow the on-screen instructions to log in to your eBay account and authorize the requested permissions.

7. **Retrieve Authorization Code:**

    After granting consent, the eBay website will redirect you to a specified redirect URI.

8. **Retrieve Access and Refresh Tokens:**

    Copy the entire URL in your browser and paste it into the script when prompted in the console. Note that the authorization code is present after the `code=`, but the script will extract the necessary part. After you paste the entire URL in the console, the script will then exchange the authorization code for an access token and refresh token from the eBay API.

9. **Script Output:**

    If the token retrieval is successful, the script will output the obtained access token and refresh token. These tokens are required for authenticating your application when making requests to the eBay API.

## Important Notes

- Keep the access token and refresh token secure. These tokens are sensitive information that grants access to your eBay account. Do not share them publicly.
- Once you close the script, all input values and output, including the access token and refresh token, are deleted from memory. It is important to note that these values are not persisted between script runs.

## Contribution

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or raise an issue.

## License

This project is licensed under the MIT License.
