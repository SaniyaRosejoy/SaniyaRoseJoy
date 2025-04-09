products = [
    {"name": "Chain", "price": 3000},
    {"name": "Bangles", "price": 2550},
    {"name": "Ring", "price": 1555},
]

companies = [
    {"name": "DHL Express", "fees": 15},
    {"name": "FedEx", "fees": 20},
    {"name": "UPS", "fees": 10},
]


for index, product in enumerate(products):
    print(f"For {product['name']}) price {product['price']}")


while True:
    product_index = input("Please Enter the product index:\n")
    try:
        product_index = int(product_index)
        if 0 <= product_index < len(products):
            break
        else:
            print("This product does not exist.")
    except ValueError:
        print("Please enter only a number.")

product = products[product_index]


for index, company in enumerate(companies):
    print(f"For {company['name']}) fees {company['fees']}")


while True:
    company_index = input("Please Enter the company index:\n")
    try:
        company_index = int(company_index)
        if 0 <= company_index < len(companies):
            break
        else:
            print("This company does not exist.")
    except ValueError:
        print("Please enter only a number.")

company = companies[company_index]

total = product['price'] + company['fees']

print(f"You selected {product['name']} with price {product['price']} and {company['name']} with fees {company['fees']}.")
print(f"The total cost is: {total}")
