import pokebase as pb
import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

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

# Send data to phone
client = Client(sid, auth)
message = client.messages.create(
    to=nums,
    from_= "19789042343",
    body= values
)


