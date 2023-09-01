import os

from flask import Flask, requests, redirect
from flask_debugtoolbar import DebugToolbarExtension

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

PETFINDER_URL = "https://api.petfinder.com/v2/animals"

# Get Info on a Random Pet»

# You’ll need to write two functions that interact with the petfinder API.

#     Authenticate with the api to get an Oauth token.
#     Make a GET request to /animals url to find a random pet