class CoinMarketCapGlobalEntity(object):
    def __init__(self):
        pass

    @property
    def active_cryptocurrencies(self):
        return self._active_cryptocurrencies

    @property
    def active_markets(self):
        return self._active_markets

    @property
    def bitcoin_percentage_of_market_cap(self):
        return self._bitcoin_percentage_of_market_cap

    @property
    def total_market_cap_usd(self):
        return self._total_market_cap_usd

    @property
    def total_volume_24h_usd(self):
        return self._total_volume_24h_usd

    @property
    def last_updated(self):
        return self._last_updated

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def error(self):
        return self._error

    @active_cryptocurrencies.setter
    def active_cryptocurrencies(self, active_cryptocurrencies: int):
        if(isinstance(active_cryptocurrencies, int)):
           self._active_cryptocurrencies = active_cryptocurrencies
        else:
           self._raise_type_error("int", "active_cryptocurrencies", active_cryptocurrencies)

    @active_markets.setter
    def active_markets(self, active_markets: int):
        if(isinstance(active_markets, int)):
           self._active_markets = active_markets
        else:
           self._raise_type_error("int", "active_markets", active_markets)

    @bitcoin_percentage_of_market_cap.setter
    def bitcoin_percentage_of_market_cap(self, bitcoin_percentage_of_market_cap: float):
        if(isinstance(bitcoin_percentage_of_market_cap, float)):
           self._bitcoin_percentage_of_market_cap = bitcoin_percentage_of_market_cap
        else:
           self._raise_type_error("float", "bitcoin_percentage_of_market_cap", bitcoin_percentage_of_market_cap)

    @total_market_cap_usd.setter
    def total_market_cap_usd(self, total_market_cap_usd: float):
        if(isinstance(total_market_cap_usd, float)):
           self._total_market_cap_usd = total_market_cap_usd
        else:
           self._raise_type_error("float", "total_market_cap_usd", total_market_cap_usd)

    @total_volume_24h_usd.setter
    def total_volume_24h_usd(self, total_volume_24h_usd: float):
        if(isinstance(total_volume_24h_usd, float)):
           self._total_volume_24h_usd = total_volume_24h_usd
        else:
           self._raise_type_error("float", "total_volume_24h_usd", total_volume_24h_usd)

    @last_updated.setter
    def last_updated(self, last_updated: int):
        if(isinstance(last_updated, int)):
           self._last_updated = last_updated
        else:
           self._raise_type_error("int", "last_updated", last_updated)

    @timestamp.setter
    def timestamp(self, timestamp: int):
        if(isinstance(timestamp, int)):
           self._timestamp = timestamp
        else:
           self._raise_type_error("int", "timestamp", timestamp)

    @error.setter
    def error(self, error: str):
        if(isinstance(error, str) or error is None):
           self._error = error
        else:
           self._raise_type_error("str or None", "error", error)

    def _raise_type_error(self, expected_type, property_name, prop):
           raise TypeError("Expected type {0} for {1}, got type {2}".format(expected_type, property_name, type(prop)))

