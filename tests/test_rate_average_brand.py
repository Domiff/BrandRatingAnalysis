from app.rating_average_brand import rating_average


def test_rate_average_brand(file_names, rate):
    result = rating_average(file_names, "average-rating")
    assert result == rate
