import requests as r
import json 
import config as c

def post_Registration():
    url = c.API_base +"register"
    data = {
        'symbol': c.TradingAgent,
        'faction': "COSMIC"
    }
    return r.post(url=url, data=data)

def post_myAgent():
    url="https://api.spacetraders.io/v2/my/agent"
    header = {'Authorization':"Bearer " + c.Token}
    return r.post(url=url,headers=header)


resp = post_myAgent()
print(resp.text)









# def get_stock_data():
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
#     response = requests.get(url)
     
#     # Check if the response is successful
#     if response.status_code == 200:
#         data = response.json()
#         last_refreshed = data["Meta Data"]["3. Last Refreshed"]
#         price = data["Time Series (5min)"][last_refreshed]["1. open"]
#         return price
#     else:
#         return None
 
# stock_prices = {}
# price = get_stock_data()
# symbol="IBM"
# if price is not None:
#     stock_prices[symbol] = price