from flask import Flask, request
from flask_cors import cross_origin
import json
import requests
from .entities import CoinMarketCapGlobalEntity
from .usecases import fill_global_entity_from_api_response

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

global_api = "https://api.coinmarketcap.com/v2/global/"


@app.route("/")
def getRoot():
    return("Root")


@app.route("/coinmarketcap", methods=["GET"])
@cross_origin()
def get_coin_market_cap():
    response = requests.get(global_api).json()
    entity = fill_global_entity_from_api_response(
        response,
        CoinMarketCapGlobalEntity()
    )
    return(json.dumps({"coin_market_cap_usd": entity.total_market_cap_usd}))

