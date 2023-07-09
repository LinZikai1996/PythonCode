from tool.control_mouse_and_keyboard import ActionConfigFile


def test_action_config_file():
    action = ActionConfigFile(
        config_file_path="/Volumes/mobile_hard_disk/project/PythonCode/Test/resource/test_step.csv")

    action.run("测试第一步")
    action.run("测试第二步")
    action.run("测试第三步")
    action.run("测试第四步")
