from flask import Flask, request
import requests
from .entities import CoinMarketCapGlobalEntity
from .usecases import fill_global_entity_from_api_response

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

global_api = "https://api.coinmarketcap.com/v2/global/"

@app.route('/')
def getRoot():
    fake_response = {
        "data": {
            "active_cryptocurrencies": 25,
            "active_markets": 20,
            "bitcoin_percentage_of_market_cap": 33.5
        },
        "quotes": {
            "USD": {
                "total_market_cap": 33333.33,
                "total_volume_24h": 333.12
            },
            "last_updated": 11234
        },
        "metadata": {
            "timestamp": 11234,
            "error": None
        }
    }

    response = requests.get(global_api).json()

    entity = fill_global_entity_from_api_response(
        response,
        CoinMarketCapGlobalEntity()
    )
    return(str(entity.__dict__))



