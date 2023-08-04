# File is responsible for signing, encoding , decoding and returning JWTs.

import time  # jwt tokens has expiration time
import jwt
from decouple import config

# Get the values from environment (.env)
JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# This returns generated JWT tokesn
def token_response(token : str):
    return {
        "access token" : token
    }

# Used in signing the JWT string
def signJWT(userID : str):
    # this is the payload
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    return token_response(token)

# used in signing to decode
def decodeJWT(token : str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        if decode_token["expiry"] >= time.time():
            return decode_token
        else:
            return None
    except:
        return {}


