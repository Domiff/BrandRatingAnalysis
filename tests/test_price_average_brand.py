from app.price_average_brand import price_average


def test_price_average_brand(file_names, price):
    result = price_average(file_names, "average-price")
    assert result == price
