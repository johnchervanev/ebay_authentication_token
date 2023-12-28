# eBay OAuth Script: User Authentication and Token Retrieval

## Overview

This Python script facilitates the eBay authentication process and token retrieval using OAuth. It opens the user's default web browser to grant consent, obtains an authorization code, and exchanges it for an access token from the eBay API. The script also provides a refresh token for extended access.

## Features

### Configuration

Easily customize the script behavior through variables at the beginning of the script:

- `client_id`: Your eBay application client ID.
- `client_secret`: Your eBay application client secret.
- `redirect_uri`: Your eBay application redirect URI.
- `scopes`: Define the required scopes based on your application's needs.

### Consent Process

The script automates the consent process by opening the user's default web browser to grant consent on the eBay website.

### Token Retrieval

After the user grants consent, the script retrieves the authorization code and exchanges it for an access token and refresh token from the eBay API.

## Problem

Interacting with the eBay API requires user authentication, and obtaining access tokens manually can be cumbersome. This script simplifies the authentication process for eBay applications.

## Solution

The script automates the eBay OAuth consent and token retrieval, making it convenient for developers to integrate eBay API authentication into their applications. It also provides a refresh token for extended access.

## Instructions

1. Open the script in your preferred Python editor or IDE.
2. Copy and paste the script into your Python environment.
3. Customize the script by updating the variables at the beginning with your eBay application credentials and desired scopes.
4. Run the script.

## Important Notes

- Ensure that you keep your eBay application credentials secure.
- Review and customize the script's scopes based on your application's requirements.
- The script provides a refresh token for extended access.

## Contribution

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or raise an issue.

## License

This project is licensed under the MIT License.
