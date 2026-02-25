import time
import hmac
import hashlib
import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger("client")

BASE_URL = "https://testnet.binancefuture.com"

API_KEY = os.getenv("BINANCE_API_KEY", "demo_key")
API_SECRET = os.getenv("BINANCE_API_SECRET", "demo_secret")


class BinanceFuturesClient:
    def _sign(self, params: dict):
        query = urlencode(params)
        signature = hmac.new(
            API_SECRET.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, params: dict):
        endpoint = "/fapi/v1/order"

        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {"X-MBX-APIKEY": API_KEY}

        try:
            logger.info(f"Request: {params}")

            r = requests.post(
              BASE_URL + endpoint,
              headers=headers,
              params=params,
              timeout=10
            )


            logger.info(f"Response: {r.text}")
            return r.json()

        except Exception as e:
            logger.exception("Network error")
            raise
