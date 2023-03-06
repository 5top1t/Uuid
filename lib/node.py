import hashlib
import uuid

def _get_mac_address_node():
    # UUID version 1, the node field consists of an IEEE 802 MAC
    # address, usually the host address
    mac = uuid.getnode()
    
    # Convert the MAC address to a string format
    mac_str = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    return mac_str


def _get_md5_node(namespace):
    # version 3 UUID is meant for generating UUIDs from "names"
    # For example, some name spaces are the
    # domain name system, URLs, ISO Object IDs(OIDs)
    string_bytes = namespace.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(string_bytes)
    hash_hex = md5.hexdigest()
    
    return hash_hex


def _get_sha1_node(namespace):
    # version 5 UUID is meant for generating UUIDs from "names"
    # For example, some name spaces are the
    # domain name system, URLs, ISO Object IDs(OIDs)
    string_bytes = namespace.encode('utf-8')
    sha1 = hashlib.sha1()
    sha1.update(string_bytes)
    hash_hex = sha1.hexdigest()
    
    return hash_hex


def _get_node_version(version: int, namespace: str = ""):
    if (version == 1):
        return _get_mac_address_node()
    if (version == 3):
        return _get_md5_node(namespace)
    elif (version == 5):
        return _get_sha1_node(namespace)
    else:
       raise ValueError("Version {} is not supported".format(version))


def get_node_dict(version: int, namespace: str):
    return {
        "namespace": _get_node_version(version, namespace)
    }
