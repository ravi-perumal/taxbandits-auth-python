import json
import requests
from jose import jws
import time


class JWT_authentication:

    # config values
    jwtKey = "your client secret"  # Client Secret
    jwtClientId = "your client id"   # Client Id
    jwtUserToken = "your user token"  # User Token
    authUrl = "https://testoauth.expressauth.net/v2/tbsauth"

    # Fetching current epoch time
    ts = int(time.time())

    # Constructing JWS
    encoded = jws.sign({
        'iss': jwtClientId,  # Issuer: Client Id
        'sub': jwtClientId,  # Subject: Client Id
        'aud': jwtUserToken,  # Audience: User Token
        'iat': ts    # Issued at: Current time (Unix epoch format)
    }, jwtKey,  # Client Secret
        algorithm='HS256')

    # Get JWT Access Token
    headers = {'Authentication': encoded, 'Content-Type': 'application/json'}
    response = requests.get(authUrl, headers=headers)

    # Saving Response to a variable
    jwt = json.loads(response.text)
    # Saving Access Token in a variable
    accessToken = jwt["AccessToken"]

    # Print the Access Token
    print('Access Token: ', accessToken)
