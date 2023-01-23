
def test():
    from AppKit import NSWorkspace
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    print(activeAppName)