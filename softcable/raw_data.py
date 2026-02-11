import os

def read_sysfs_folder(path):
    """Reads all files in a sysfs folder and returns a dict."""
    data = {}

    if not os.path.exists(path):
        return None

    for item in os.listdir(path):
        full = os.path.join(path, item)

        if os.path.isfile(full):
            try:
                with open(full, "r") as f:
                    data[item] = f.read().strip()
            except:
                data[item] = "<unreadable>"

    return data


def read_power_supply():
    base = "/sys/class/power_supply/"
    result = {}

    if not os.path.exists(base):
        return None

    for entry in os.listdir(base):
        full = os.path.join(base, entry)
        if os.path.isdir(full):
            result[entry] = read_sysfs_folder(full)

    return result


def read_typec():
    base = "/sys/class/typec/"
    result = {}

    if not os.path.exists(base):
        return None

    for entry in os.listdir(base):
        full = os.path.join(base, entry)
        if os.path.isdir(full):
            result[entry] = read_sysfs_folder(full)

    return result


def read_usb_devices():
    base = "/sys/bus/usb/devices/"
    result = {}

    if not os.path.exists(base):
        return None

    for entry in os.listdir(base):
        full = os.path.join(base, entry)
        if os.path.isdir(full):
            result[entry] = read_sysfs_folder(full)

    return result


def get_raw_data():
    return {
        "power_supply": read_power_supply(),
        "typec": read_typec(),
        "usb_devices": read_usb_devices()
    }
