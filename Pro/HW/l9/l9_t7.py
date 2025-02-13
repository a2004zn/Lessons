import re
from typing import Any


def ip_addr(ip: str) -> list[Any]:
    """
    Определитель правильности ip-адреса.
    :param ip:
    :return:
    """
    pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    ipv = re.findall(pattern, ip)
    return ipv


txt = """
192.168.1.1
255.255.255.255
10.0.0.1
999.999.999.999, 300.300.300.300
"""

print(ip_addr(txt))
