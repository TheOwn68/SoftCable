import os

TYPEC_PATH = "/sys/class/typec/"
POWER_PATH = "/sys/class/power_supply/"

class USBInfo:
    def __init__(self):
        self.port = None
        self.partner = None
        self.pd_supported = False
        self.pd_profiles = []
        self.voltage = None
        self.current = None
        self.wattage = None

def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except:
        return None

def detect_usb_c():
    info = USBInfo()

    # Detect USB-C port
    ports = [p for p in os.listdir(TYPEC_PATH) if "port" in p]
    if not ports:
        return None  # No USB-C ports found

    port = ports[0]
    info.port = port

    partner_path = os.path.join(TYPEC_PATH, port, "partner")
    if os.path.exists(partner_path):
        info.partner = os.path.basename(partner_path)
    else:
        info.partner = None

    # Detect PD support
    pd_path = os.path.join(TYPEC_PATH, port, "usb_power_delivery")
    if os.path.exists(pd_path):
        info.pd_supported = True

        # Read PD profiles
        profiles_path = os.path.join(TYPEC_PATH, port, "port0", "supported_modes")
        if os.path.exists(profiles_path):
            info.pd_profiles = read_file(profiles_path)

    # Read power info
    for item in os.listdir(POWER_PATH):
        if "usb" in item.lower() or "typec" in item.lower():
            voltage = read_file(os.path.join(POWER_PATH, item, "voltage_now"))
            current = read_file(os.path.join(POWER_PATH, item, "current_now"))

            if voltage and current:
                info.voltage = int(voltage) / 1_000_000  # µV → V
                info.current = int(current) / 1_000_000  # µA → A
                info.wattage = round(info.voltage * info.current, 2)

    return info
