import requests as r
import config as c
import json
from types import SimpleNamespace as sn
import matplotlib.pyplot as plt
import numpy as np

def post_Registration():
    url = c.API_base +"register"
    data = {
        'symbol': c.TradingAgent,
        'faction': "COSMIC"
    }
    return r.post(url=url, data=data)

Auth_header = {'Authorization':"Bearer " + c.Token}

'''
to get agent 
use x,y = get_Agent()
'''
def get_Agent_data():
    url=c.API_base+"my/agent"
    recieved_data = r.get(url=url,headers=Auth_header).json()
    return recieved_data['data']
'''
creates an object with 
    accountId
    symbol 
    headquarters
    credits
    startingFaction
    shipCount
'''
def get_myAgent():
    url=c.API_base+"my/agent"
    recieved_data = r.get(url=url,headers=Auth_header).json()
    return json.loads(json.dumps(recieved_data['data']),object_hook=lambda d: sn(**d))
Agent=get_myAgent()
#print(Agent)
def get_location( waypoiuntID:str):
    LS = waypoiuntID.split("-")[0:2]
    url=c.API_base+"systems/"+LS[0]+"-"+LS[1]+"/waypoints/"+waypoiuntID
    data = r.get(url=url,headers=Auth_header)
#get_location(Agent.headquarters)

def get_system(waypoiuntID:str, show:bool):
    LS = waypoiuntID.split("-")[0:2]
    url=c.API_base+"systems/"+LS[0]+"-"+LS[1]
    data = r.get(url=url,headers=Auth_header).json()
    size= len(data['data']['waypoints'])
    xy_set = np.zeros((2,size))
    i= 0
    for key in data['data']['waypoints']:
        xy_set[0,i]= key['x']
        xy_set[1,i]= key['y']
        i=i+1
    if show:
        plt.scatter(xy_set[0,:],xy_set[1,:])
        plt.show()
#get_system(Agent.headquarters,True)

