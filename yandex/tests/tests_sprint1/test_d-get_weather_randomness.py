from sprint1.d_get_weather_randomness import get_weather_randomness


def test_on_range():
    assert get_weather_randomness([-1, -10, -8, 0, 2, 0, 5]) == 3
    assert get_weather_randomness([5, 5, 5, 5, 5, 5, 5]) == 0
    assert get_weather_randomness([-159, -248, 8, -23, -45, -131, -169,
                                   -184, 159, -241]) == 3
    assert get_weather_randomness([-159, ]) == 1
