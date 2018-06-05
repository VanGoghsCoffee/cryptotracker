from cryptotracker import app
from cryptotracker.entities import CoinMarketCapGlobalEntity


if __name__ == '__main__':
    app.run('0.0.0.0', 3005, True)
