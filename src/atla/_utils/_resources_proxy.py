from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `atla.resources` module.

    This is used so that we can lazily import `atla.resources` only when
    needed *and* so that users can just import `atla` and reference `atla.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("atla.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
