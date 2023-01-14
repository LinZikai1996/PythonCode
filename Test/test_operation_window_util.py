import time

from win32gui import IsWindow, IsWindowEnabled, IsWindowVisible, GetWindowText, GetClassName, GetWindowRect, \
    EnumWindows

from tool.operation_window import OperationWindowUtil


def test_open_app():
    OperationWindowUtil("").open_app()


def test_get_windows_title():
    def foo(handle, mouse):
        if IsWindow(handle) and IsWindowEnabled(handle) and IsWindowVisible(handle):
            print(GetWindowText(handle))

    EnumWindows(foo, 0)


def test_open_app_and_start_game():
    operation = OperationWindowUtil("MuMu模拟器")
    operation.open_app()
    time.sleep(10)
    # operation.prepare_window()
