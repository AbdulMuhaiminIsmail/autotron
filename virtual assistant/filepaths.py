import winreg

def get_installed_apps():
    key = r"Software\Microsoft\Windows\CurrentVersion\Uninstall"
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    key = winreg.OpenKey(reg, key)

    installed_apps = []

    try:
        index = 0
        while True:
            subkey_name = winreg.EnumKey(key, index)
            subkey = winreg.OpenKey(key, subkey_name)
            display_name = winreg.QueryValueEx(subkey, 'DisplayName')[0]
            install_location = winreg.QueryValueEx(subkey, 'InstallLocation')[0]
            installed_apps.append((display_name, install_location))
            index += 1
    except WindowsError:
        pass

    return installed_apps

# Example usage
installed_apps = get_installed_apps()
for app_name, app_path in installed_apps:
    print(f"Name: {app_name}, Path: {app_path}")
