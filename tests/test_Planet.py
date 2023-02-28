from sw_planets_api.Planet import Planet


def test_main():
    expected = "TEST"

    p = Planet()
    result = p.test()

    assert result == expected
