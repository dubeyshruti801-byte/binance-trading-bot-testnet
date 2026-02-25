VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str):
    if not symbol:
        raise ValueError("Symbol is required")

    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs supported (example: BTCUSDT)")

    return symbol.upper()


def validate_side(side: str):
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()

    if order_type not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price, order_type: str):
    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

    return price
