import typer
import logging
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logging

app = typer.Typer()
order_service = OrderService()


@app.command()
def order(
    symbol: str = typer.Argument(..., help="Trading symbol (e.g., BTCUSDT)"),
    side: str = typer.Argument(..., help="BUY or SELL"),
    order_type: str = typer.Argument(..., help="MARKET or LIMIT"),
    quantity: float = typer.Argument(..., help="Order quantity"),
    price: float = typer.Option(None, help="Required for LIMIT orders"),
):
    """
    Place a Futures Testnet order.
    """

    setup_logging()
    logger = logging.getLogger("cli")

    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        # Print request summary
        print("\n===== ORDER REQUEST =====")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Type        : {order_type}")
        print(f"Quantity    : {quantity}")
        if order_type == "LIMIT":
            print(f"Price       : {price}")
        print("=========================\n")

        # Place order
        response = order_service.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        # Print response summary
        print("===== ORDER RESPONSE =====")
        print(f"Order ID    : {response.get('orderId')}")
        print(f"Status      : {response.get('status')}")
        print(f"ExecutedQty : {response.get('executedQty')}")
        print(f"Avg Price   : {response.get('avgPrice')}")
        print("==========================")

        print("\n✅ SUCCESS")

    except Exception as e:
        logger.exception("Order failed")
        print(f"\n❌ FAILED: {str(e)}")


if __name__ == "__main__":
    app()
