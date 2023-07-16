from Arknights.arknight_auto import confirm_click_position
from Arknights.automation_function import ArknightsAuto

auto = ArknightsAuto()


def test_go_back_to_home_page():
    auto.go_back_to_home_page()


def test_confirm_click_position():
    result, x, y = confirm_click_position("/Volumes/mobile_hard_disk/work_temp/screenshot/back_button.png")
    if x and y:
        print(f"({x}, {y})")
    else:
        print("没找到")
