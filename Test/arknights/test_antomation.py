from Arknights.automation import ArknightsAuto

auto = ArknightsAuto()


def test_check_home_page():
    assert auto.check_home_page()


def test_go_back_to_home_page():
    auto.go_back_to_home_page()
