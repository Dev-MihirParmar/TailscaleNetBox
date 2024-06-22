import subprocess
import platform

class WinBoxManager:
    def __init__(self):
        pass

    def launch_winbox(self, network_key):
        try:
            if platform.system() == "Windows":
                subprocess.run(["winbox.exe", f"{network_key}"], check=True, shell=True)
            else:
                subprocess.run(["winbox", f"{network_key}"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error launching WinBox: {e}")
