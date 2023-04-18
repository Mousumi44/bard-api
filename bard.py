from Bard import Chatbot
from dotenv import load_dotenv
import os
import random
import sys

load_dotenv() #load environment
bard_token=os.environ["BARD_TOKEN"] 

chatbot = Chatbot(bard_token) #create bard client

def get_response(prompt):
    answer = chatbot.ask(prompt)
    return answer["content"]

if __name__=="__main__":
    prompt="Help me finish my art studio tagline: craft, create, and ..."
    print(get_response(prompt))


