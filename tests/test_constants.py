import cloudy


def test_lat_type():
    assert isinstance(cloudy.LAT, float) == True


def test_long_type():
    assert isinstance(cloudy.LONG, float) == True


def test_darksky_api_not_empty():
    assert cloudy.DARK_SKY_API != ""
