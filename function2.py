def get_price_with_vat(price):
    return price + price*20/100
price_without_vat = 100
price_with_vat = get_price_with_vat(price_without_vat)

print(f"Print with vat: {price_with_vat}")
