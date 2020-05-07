import requests
import json
from .logger import log


def create_wlan(ssid: str, psk: str, site_id: str, token: str, vlan: int, duration: int) -> dict:
    """
    Creates a wireless network at a specified Mist site.

    :param str ssid: The name of the wireless network to be created.
    :param str psk: The preshared key to be used on the wireless network.
    :param str site_id: The unique site ID where the wireless network will be created.
    :param str token: Mist API token with network admin or super user rights.
    :param int vlan: VLAN ID for the wireless network.
    :param int duration: Days before the wireless network expires.

    :return dict: A dictionary containing the JSON response from the Mist API.
    """
    url = f"https://api.mist.com/api/v1/sites/{site_id}/wlans"
    log.info(f"Creating new wireless network '{ssid}' with the PSK '{psk}'.")
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Token {token}"
    }
    wlan = {
        "ssid": ssid,
        "enabled": True,
        "auth": {
            "type": "psk",
            "psk": psk
        },
        "roam_mode": "11r",
        "vlan_enabled": True,
        "vlan_id": vlan
    }
    res = requests.post(url=url, data=json.dumps(wlan), headers=headers)
    data = res.json()
    if res.status_code == 200:
        log.info(f"New wireless network '{ssid}' with a duration of {duration} created!")
        return data
    else:
        log.error("Failed to create new wireless network!")
        log.error(f"Response: {res.json()}")
        return {"error": "failed"}
