import pokebase as pb
import random
from twilio.rest import Client
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup


# gather sensitive data
load_dotenv("./vars/.env")
sid = os.environ.get('SID')
auth = os.environ.get('AUTH')
nums = os.environ.get('myNumber')

# Pull data from pokebase
pokemon = pb.pokemon(random.randint(1, 1000))
print(pokemon.abilities)
print(sid)
values = "Name: " + str(pokemon.name) + " " + " Height: " + str(pokemon.height) + " Weight: " + str(pokemon.weight)
# Pull Image from pokedb
r = requests.get('https://pokemondb.net/pokedex/mew')
soup = BeautifulSoup(r.content, 'html.parser')
images = soup.findAll('img')
for item in images:
    sending = item['src']

# Send data to phone
client = Client(sid, auth)
message = client.messages.create(
    to=nums,
    from_= "19789042343",
    body= values
)

message2 = client.messages.create(
    to=nums,
    from_= "19789042343",
    body= sending

)

