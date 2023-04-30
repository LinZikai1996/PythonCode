import time

import psutil

from Arknights.automation_function import ArknightsAuto
from tool.control_mouse_and_keyboard import left_click
from tool.logger import Logger
from tool.run_os_command import run_command

log = Logger()


def is_app_exist(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return True
    return False


def open_emulator():
    log.info("开始运行明日方舟脚本")

    if is_app_exist('qemu-system-aarch64') is False:
        log.info("打开安卓模拟器")
        run_command("screen -S emulator -d -m $HOME/Library/Android/sdk/emulator/emulator -avd Robot")

        log.info("等待 5 秒模拟器后再继续执行 ....")
        time.sleep(5)

    log.info("移动模拟器归位")
    run_command('osascript script/set_position.scpt')

    log.info("使模拟器活跃")
    left_click(x=760, y=37)


if __name__ == '__main__':
    open_emulator()
    ArknightsAuto().start()
