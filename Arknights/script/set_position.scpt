tell application "System Events"
    tell process "qemu-system-aarch64"
        set theWindow to window "Android Emulator - Robot:5554"
        set position of theWindow to {0, 0}
        set frontmost to true
    end tell
end tell
