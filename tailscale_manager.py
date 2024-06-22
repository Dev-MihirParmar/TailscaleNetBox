import subprocess
import platform

class TailscaleManager:
    def __init__(self):
        self.networks = []

    def add_network(self, network_key):
        self.networks.append(network_key)

    def connect_network(self, network_key):
        try:
            if platform.system() == "Windows":
                subprocess.run(["tailscale", "up", "--authkey", network_key], check=True, shell=True)
            else:
                subprocess.run(["tailscale", "up", "--authkey", network_key], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error connecting to Tailscale network: {e}")

    def disconnect_network(self):
        try:
            if platform.system() == "Windows":
                subprocess.run(["tailscale", "down"], check=True, shell=True)
            else:
                subprocess.run(["tailscale", "down"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error disconnecting from Tailscale network: {e}")
