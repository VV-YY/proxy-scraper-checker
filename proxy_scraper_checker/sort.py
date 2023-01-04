from __future__ import annotations

from typing import Tuple

from .proxy import Proxy


def timeout_sort_key(proxy: Proxy) -> float:
    return proxy.timeout


def natural_sort_key(proxy: Proxy) -> Tuple[int, ...]:
    return (*map(int, proxy.host.split(".")), proxy.port)
