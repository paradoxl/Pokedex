import pokebase as pb
import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv("./vars/.env")
sid = os.environ.get('SID')
pokemon = pb.pokemon(random.randint(1,1008))
print(pokemon.name)
print(sid)