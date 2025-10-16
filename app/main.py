from tabulate import tabulate

from .rating_average_brand import rating_average, RATE_HEADERS
from .price_average_brand import price_average, PRICE_HEADERS
from .parser import file_names, type_report


def main(files, types):
    if "average-rating" in types:
        return tabulate(
            rating_average(files, types),
            headers=RATE_HEADERS,
            tablefmt="grid",
        )
    elif "average-price" in types:
        return tabulate(
            price_average(files, types),
            headers=PRICE_HEADERS,
            tablefmt="grid",
        )
    else:
        return "Введён некорректный параметр"


if __name__ == "__main__":
    print(main(files=file_names, types=type_report))
