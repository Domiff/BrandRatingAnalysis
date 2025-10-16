from .csv_file_reader import make_data_brands
from .brands import brands


RATE_HEADERS = ["brand", "rating"]


def rating_average(file_names, type_report):
    data = make_data_brands(file_names, type_report)

    for i in range(len(file_names)):
        data.remove(RATE_HEADERS)

    rate_dict = {brand: 0 for brand in set(brands(data))}

    for brand, rate in data:
        rate_dict[brand] += float(rate)

    rating_average_dict = {
        brand: round(rate / brands(data).count(brand), 2)
        for brand, rate in rate_dict.items()
    }

    sorted_data = sorted(
        rating_average_dict.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_data
