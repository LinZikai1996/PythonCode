from tool.ming_ri_fang_zhou import get_image_size_info


def test_get_image_size_info():
    length, width = get_image_size_info("E:\\tmp\\screenshot\\have_potion_or_no.jpg")
    assert length == 733
    assert width == 594
