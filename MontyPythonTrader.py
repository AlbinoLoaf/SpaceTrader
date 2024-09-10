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
    waypointset= {'FUEL_STATION':0, 'ASTEROID_BASE':1, 'PLANET':2, 'ASTEROID':3, 'ORBITAL_STATION':4, 'GAS_GIANT':5, 'JUMP_GATE':6, 'ENGINEERED_ASTEROID':7, 'MOON':8}
    colour=['b','g','r','c','m','y','k','tab:orange','tab:purple']
    xy_set = np.zeros((len(waypointset)*2,size))
    i=0
    print(data)
    fig, ax = plt.subplots()
    for key in data['data']['waypoints']:
        index = waypointset[key['type']]*2
        xy_set[index,i]= key['x']
        xy_set[index+1,i]= key['y']
        i=i+1
    if show:
        for key in waypointset:
            index = waypointset[key] *2
            ax.scatter(xy_set[index,:],xy_set[index+1,:],label=key,color=colour[waypointset[key]])
        ax.grid(True)
        ax.legend()
        ax.grid(False)
        plt.show()
get_system(Agent.headquarters,True)

def get_myContracts():
    url= c.API_base+"my/contracts"
    data = r.get(url=url,headers=Auth_header)
    return data.text

#print(get_myContracts())
