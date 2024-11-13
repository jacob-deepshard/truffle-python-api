import subprocess
import platform
import time
from typing import List, Optional

class NetworkManager:
    def connect_to_wifi(self, ssid: str, password: str):
        system = platform.system()
        if system == "Darwin":
            self._connect_mac(ssid, password)
        elif system == "Linux":
            self._connect_linux(ssid, password)
        else:
            raise OSError(f"Unsupported OS: {system}")

    def _connect_mac(self, ssid: str, password: str):
        cmd = [
            "networksetup", "-setairportnetwork",
            "en0", ssid, password
        ]
        subprocess.run(cmd, check=True)

    def _connect_linux(self, ssid: str, password: str):
        cmd = [
            "nmcli", "dev", "wifi", "connect",
            ssid, "password", password
        ]
        subprocess.run(cmd, check=True)

    def ping_host(self, host: str, timeout: int = 1) -> bool:
        cmd = ["ping", "-c", "1", "-W", str(timeout), host]
        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0

    def scan_for_networks(self) -> List[str]:
        system = platform.system()
        if system == "Darwin":
            return self._scan_mac()
        elif system == "Linux":
            return self._scan_linux()
        else:
            raise OSError(f"Unsupported OS: {system}")

    def _scan_mac(self) -> List[str]:
        cmd = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        networks = []
        for line in result.stdout.split('\n')[1:]:
            if line.strip():
                ssid = line.strip().split()[0]
                networks.append(ssid)
        return networks

    def _scan_linux(self) -> List[str]:
        cmd = ["nmcli", "-t", "-f", "SSID", "device", "wifi", "list"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        networks = result.stdout.strip().split('\n')
        return [ssid for ssid in networks if ssid]

    def get_current_ssid(self) -> Optional[str]:
        system = platform.system()
        if system == "Darwin":
            cmd = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if " SSID: " in line:
                    return line.split("SSID: ")[1].strip()
        elif system == "Linux":
            cmd = ["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            for line in result.stdout.strip().split('\n'):
                if line.startswith('yes:'):
                    return line.split(':')[1]
        return None 