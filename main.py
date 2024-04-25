import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_URL = os.getenv('PIXELA_URL')
PIXELA_USER_TOKEN = os.getenv('PIXELA_USER_TOKEN')
PIXELA_USER_NAME = os.getenv('PIXELA_USER_NAME')

## Create a user
# user_params = {
#     "token": PIXELA_USER_TOKEN,
#     "username": PIXELA_USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response_user = requests.post(url=PIXELA_URL, json=user_params)
# print(response_user.text)
#
graph_endpoint = f"{PIXELA_URL}/{PIXELA_USER_NAME}/graphs"
graph_config = {
    "id": "coding",
    "name": "Coding graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}
headers = {
    'X-USER-TOKEN': PIXELA_USER_TOKEN
}

response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response_graph.text)