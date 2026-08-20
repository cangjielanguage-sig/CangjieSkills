from __future__ import annotations

import sys
from array import array


def pack_vector(values: list[float]) -> bytes:
    packed = array("f", (float(value) for value in values))
    if sys.byteorder != "little":
        packed.byteswap()
    return packed.tobytes()


def unpack_vector(blob: bytes | memoryview | None) -> list[float]:
    if not blob:
        return []
    packed = array("f")
    packed.frombytes(bytes(blob))
    if sys.byteorder != "little":
        packed.byteswap()
    return packed.tolist()
