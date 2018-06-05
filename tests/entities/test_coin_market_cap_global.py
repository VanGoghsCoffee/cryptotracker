import unittest
from cryptotracker.entities.coin_market_cap_global import CoinMarketCapGlobalEntity

class TestCoinMarketCapGlobalEntity(unittest.TestCase):
    def setUp(self):
        self.coin_mark_cap_global = CoinMarketCapGlobalEntity()

    def test_active_cryptocurrencies(self):
        self.coin_mark_cap_global.active_cryptocurrencies = 25
        self.assertEqual(self.coin_mark_cap_global.active_cryptocurrencies, 25)

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.active_cryptocurrencies = 25.5

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.active_cryptocurrencies = "str"

    def test_active_markets(self):
        self.coin_mark_cap_global.active_markets = 25
        self.assertEqual(self.coin_mark_cap_global.active_markets, 25)

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.active_markets = 25.5

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.active_markets = "str"

    def test_bitcoin_percentage_of_market_cap(self):
        self.coin_mark_cap_global.bitcoin_percentage_of_market_cap = 25.0
        self.assertEqual(self.coin_mark_cap_global.bitcoin_percentage_of_market_cap, 25.0)

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.bitcoin_percentage_of_market_cap = 25

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.bitcoin_percentage_of_market_cap = "str"

    def test_total_market_cap_usd(self):
        self.coin_mark_cap_global.total_market_cap_usd = 25.0
        self.assertEqual(self.coin_mark_cap_global.total_market_cap_usd, 25.0)

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.total_market_cap_usd = 25

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.total_market_cap_usd = "str"

    def test_total_volume_24h_usd(self):
        self.coin_mark_cap_global.total_volume_24h_usd = 25.0
        self.assertEqual(self.coin_mark_cap_global.total_volume_24h_usd, 25.0)

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.total_volume_24h_usd = 25

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.total_volume_24h_usd = "str"

    def test_last_updated(self):
        self.coin_mark_cap_global.last_updated = 12345
        self.assertEqual(self.coin_mark_cap_global.last_updated, 12345)

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.last_updated = 25.5

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.last_updated = "str"

    def test_timestamp(self):
        self.coin_mark_cap_global.timestamp = 12345
        self.assertEqual(self.coin_mark_cap_global.timestamp, 12345)

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.timestamp = 25.5

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.timestamp = "str"

    def test_error(self):
        self.coin_mark_cap_global.error = "error message"
        self.assertEqual(self.coin_mark_cap_global.error, "error message")

        self.coin_mark_cap_global.error = None

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.error = 25.5

        with self.assertRaises(TypeError):
            self.coin_mark_cap_global.error = 25

