

def validate_token(token: str) -> str:
    """
    Validate the API token.
    Additional authorization and security measures can be implemented here as well.

    :param str token: The Mist API token.
    :return str: The same token unless it has failed validation.
    """
    if len(token) == 96 and token.isalnum():
        return token
    else:
        raise ValueError("Invalid API token.")


def validate_site_id(site_id: str) -> str:
    """
    Validate the site ID.
    Additional checks and advanced logic can be implemented here as well.

    :param str site_id: The Mist site ID.
    :return str: The same site ID unless it has failed validation.
    """
    if len(site_id) == 36:
        return site_id
    else:
        raise ValueError("Invalid site ID.")


def validate_psk(psk: str) -> str:
    """
    Validate the length of the PSK.
    This is where addional validaton to meet security policy requirements can be implemented as well.

    :param str psk: The wireless network preshared key.
    :return str: The same preshared key unless it failed validation.
    """
    if 8 <= len(psk) <= 64:
        return psk
    else:
        raise ValueError(f"Invalid PSK: '{psk}', the length must be between 8 and 64 characters.")


def validate_vlan(vlan: str) -> int:
    """
    Validate the VLAN ID value.
    This is where addional validaton to meet network design/architecture requirements can be implemented as well.

    :param str vlan: The VLAN ID of the wireless network.
    :return int: The same VLAN ID unless it failed validation.
    """
    try:
        if 1 <= int(vlan) <= 4094:
            return int(vlan)
        else:
            raise ValueError(f"Invalid VLAN ID: '{vlan}', the value must be less than 4094.")
    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error validating VLAN '{vlan}': {e}")
