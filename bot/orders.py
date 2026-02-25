import logging
from typing import Optional
from .client import BinanceFuturesClient

logger = logging.getLogger("orders")


class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None,
    ):
        """
        Build payload and call client.
        """

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        # LIMIT orders require price + timeInForce
        if order_type.upper() == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")

            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Order payload: {params}")

        response = self.client.place_order(params)

        return response
