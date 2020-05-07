import argparse
from .validators import *


def parse_cli() -> dict:
    """
    Parses the CLI arguments and returns a dictionary containing the data.

    :return dict: Dictionary containing the CLI arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--token',
                        type=validate_token,
                        default="X" * 96,
                        help="Mist API token")
    parser.add_argument('--site_id',
                        type=validate_site_id,
                        required=False,
                        default="S" * 36,
                        help="Mist site ID")
    parser.add_argument('--ssid',
                        type=str,
                        required=False,
                        default="SSS",
                        help="The wireless network name")
    parser.add_argument('--psk',
                        type=validate_psk,
                        required=False,
                        default="PPPPPPPPP",
                        help="PSK for the wireless network")
    parser.add_argument('--vlan',
                        type=validate_vlan,
                        default=1,
                        help="VLAN ID for the wireless network (default: VLAN 1)")
    parser.add_argument('--duration',
                        type=int,
                        default=7,
                        help="Number of days to keep the wireless network online (default: 7 days)")
    arguments = vars(parser.parse_args())
    return arguments
