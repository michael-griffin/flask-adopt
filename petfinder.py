import os

from flask import Flask, redirect
import requests
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

PETFINDER_URL = "https://api.petfinder.com/v2/animals"
AUTH_TOKEN_URL = "https://api.petfinder.com/v2/oauth2/token"
# Get Info on a Random Pet»

# You’ll need to write two functions that interact with the petfinder API.

#     Authenticate with the api to get an Oauth token.
#     Make a GET request to /animals url to find a random pet


#@app.before_first_request #move to app
# def refresh_credentials():
#     global auth_token
#     auth_token = update_auth_token()

#TODO: current status: we're getting the KEYs, but
#requests.get is saying we're not authorized

def update_auth_token():
    """Return page about book."""
    # print(f"api key \n\n\n{PETFINDER_API_KEY}")
    # print(f"secret key \n\n\n{PETFINDER_SECRET_KEY}")


    resp = requests.post(f"{AUTH_TOKEN_URL}",
        data= {"grant_type" : "client_credentials",
                "client_id": PETFINDER_API_KEY,
                "client_secret": PETFINDER_SECRET_KEY})


    auth_token = resp.json()
    #print(f"authorization token: \n\n\n {auth_token}")
    return auth_token["access_token"]


# curl -d "grant_type=client_credentials&client_id=
# zyqEKd5OExsgatVOinJIZRmNcXVcvWgT1LljTGQyF39ZZRYBdr&client_secret=
# O1eAKb1Gx09dhdZutBaY7F9VWP28uLouGnOq1yhO" https://api.petfinder.com/v2/oauth2/token