def fill_global_entity_from_api_response(api_response, coin_mark_cap_global):
    try:
        coin_mark_cap_global.active_cryptocurrencies = api_response["data"]["active_cryptocurrencies"]
        coin_mark_cap_global.active_markets = api_response["data"]["active_markets"]
        coin_mark_cap_global.bitcoin_percentage_of_market_cap = api_response["data"]["bitcoin_percentage_of_market_cap"]
        coin_mark_cap_global.total_market_cap_usd = api_response["data"]["quotes"]["USD"]["total_market_cap"]
        coin_mark_cap_global.total_volume_24h_usd = api_response["data"]["quotes"]["USD"]["total_volume_24h"]
        coin_mark_cap_global.last_updated = api_response["data"]["last_updated"]
        coin_mark_cap_global.timestamp = api_response["metadata"]["timestamp"]
        coin_mark_cap_global.error = api_response["metadata"]["error"]
    except TypeError as e:
        print("Couldn't create coin_market_cap_global entity \n Reason: {}".format(e))
        return empty_global_entity_with_error(coin_mark_cap_global, "Empty entity")
    else:
        return coin_mark_cap_global

def empty_global_entity(global_entity):
    global_entity.active_cryptocurrencies = 0
    global_entity.active_markets = 0
    global_entity.bitcoin_percentage_of_market_cap = 0.0
    global_entity.total_market_cap_usd = 0.0
    global_entity.total_volume_24h_usd = 0.0
    global_entity.last_updated = 0
    global_entity.timestamp = 0
    global_entity.error = ""

    return global_entity

def empty_global_entity_with_error(global_entity, error):
    global_entity = empty_global_entity(global_entity)
    global_entity.error = error
    return global_entity
