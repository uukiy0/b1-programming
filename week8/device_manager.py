


from auth_system import User

# Lab 8 - IoT Device Management System
# This program manages IoT devices with security and access control.

from datetime import datetime

class Device:

    # This runs when a new device is created
    # It validates basic inputs and sets default security values.
    def __init__(self, device_id, device_type, owner, firmware="1.0"):
        
        if not device_id or not device_type:
            raise ValueError("Device ID and type cannot be empty")

        self.__device_id = device_id
        self.__device_type = device_type
        self.__firmware = firmware
        self.__owner = owner
        self.__compliance = "unknown"
        self.__last_scan = None
        self.__active = True
        self.__logs = []

    # This method checks if a user can access the device.
    # Access depends on ownership, compliance, and user role.
    def authorise_access(self, user):

        if not self.__active:
            self.__log(user.get_username(), "Access denied - Device inactive")
            return False

        # Check compliance unless admin
        if not self.check_compliance():
            if not user.has_permission("admin"):
                self.__log(user.get_username(), "Access denied - Not compliant")
                return False

        # Check ownership unless admin
        if user.get_username() != self.__owner:
            if not user.has_permission("admin"):
                self.__log(user.get_username(), "Access denied - Not owner")
                return False

        self.__log(user.get_username(), "Access granted")
        return True

    # This simulates running a security scan.
    # After scan, device becomes compliant.
    def run_scan(self):
        self.__last_scan = datetime.now()
        self.__compliance = "compliant"
        self.__log("SYSTEM", "Security scan completed")

    # This checks if the device is still compliant.
    # If last scan was over 30 days ago, device becomes non-compliant.
    def check_compliance(self):

        if self.__last_scan is None:
            self.__compliance = "non-compliant"
            return False

        days = (datetime.now() - self.__last_scan).days

        if days > 30:
            self.__compliance = "non-compliant"
            return False

        return True

    # This allows admin users to update firmware.
    # Standard users cannot update firmware.
    def update_firmware(self, new_version, user):

        if not user.has_permission("admin"):
            return False

        self.__firmware = new_version
        self.__log(user.get_username(), f"Firmware updated to {new_version}")
        return True

    # This method quarantines (disables) the device.
    # Only admins can quarantine devices.
    def quarantine(self, user):

        if not user.has_permission("admin"):
            return False

        self.__active = False
        self.__log(user.get_username(), "Device quarantined")
        return True

    # This private method logs actions with timestamps.
    # Logs are stored safely inside the object.
    def __log(self, username, action):
        self.__logs.append(f"{datetime.now()} - {username}: {action}")

    # This returns safe device information.
    # Sensitive logs are not exposed.
    def get_info(self):
        return {
            "device_id": self.__device_id,
            "type": self.__device_type,
            "firmware": self.__firmware,
            "owner": self.__owner,
            "compliance": self.__compliance,
            "active": self.__active
        }


class DeviceManager:

    # This creates an empty device list.
    def __init__(self):
        self.__device_list = {}

    # This adds a device to the system.
    def add_device(self, device):
        info = device.get_info()
        self.__device_list[info["device_id"]] = device

    # Only admins can remove devices.
    def remove_device(self, device_id, user):

        if not user.has_permission("admin"):
            return False

        if device_id in self.__device_list:
            del self.__device_list[device_id]
            return True

        return False

    # Only admins can generate security reports.
    # The report shows current device status.
    def generate_report(self, user):

        if not user.has_permission("admin"):
            return None

        report = []

        for device in self.__device_list.values():
            device.check_compliance()
            report.append(device.get_info())

        return report


# Simple Testing
admin = User("admin", "admin123", "admin")
employee = User("sarah", "pass123", "standard")

device1 = Device("D100", "Camera", "sarah")
manager = DeviceManager()

manager.add_device(device1)

# Run security scan so device becomes compliant
device1.run_scan()

# Standard user accessing own device
print(device1.authorise_access(employee))  # True

# Standard user trying to update firmware (should fail)
print(device1.update_firmware("2.0", employee))  # False

# Admin updating firmware
print(device1.update_firmware("2.0", admin))  # True

# Admin quarantining device
device1.quarantine(admin)

# Attempt access after quarantine
print(device1.authorise_access(employee))  # False

# Generate admin report
print(manager.generate_report(admin))
