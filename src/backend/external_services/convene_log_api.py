from utils.handle_urls import get_params
import requests
from requests.exceptions import JSONDecodeError

def get_convene_log(api_url:str,url:str, card_pool_type:int):
    params = get_params(url)

    payload={
        "cardPoolId": params.get('resources_id',''),
        "cardPoolType": card_pool_type,
        "languageCode": params.get('lang','en'),
        "playerId": params.get('player_id',''),
        "recordId": params.get('record_id',''),
        "serverId": params.get('svr_id','')
    }

    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.request("POST", api_url, headers=headers, json=payload)
    except JSONDecodeError:
        return
    except Exception as e:
        return

    return response.json()