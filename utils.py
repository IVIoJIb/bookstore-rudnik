# utils.py
def validate_price(price):
    if price <= 0:
        raise ValueError("Ціна повинна бути більшою за нуль")
    return True