from .csv_file_reader import make_data_brands
from .brands import brands


PRICE_HEADERS = ["brand", "price"]


def price_average(file_names, type_report):
    data = make_data_brands(file_names, type_report)

    for i in range(len(file_names)):
        data.remove(PRICE_HEADERS)

    price_dict = {brand: 0 for brand in set(brands(data))}

    for brand, price in data:
        price_dict[brand] += float(price)

    price_average_dict = {
        brand: round(price / brands(data).count(brand), 2)
        for brand, price in price_dict.items()
    }

    sorted_data = sorted(
        price_average_dict.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_data
