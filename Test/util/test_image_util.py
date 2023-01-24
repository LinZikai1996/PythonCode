from util.image_util import check_target_img_is_from_source_img_or_no


def test_check_target_img_is_from_source_img_or_no():
    result, x, y = check_target_img_is_from_source_img_or_no(
        source_path="/Volumes/mobile_hard_disk/work_temp/screenshot/finish_action_test_2.png",
        target_path="/Volumes/mobile_hard_disk/work_temp/screenshot/finish_action_test_1.png")

    print(f"x: {x}, y: {y}")
