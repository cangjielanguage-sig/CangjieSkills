#!/usr/bin/env python3
"""V2 兼容入口，实际转发到 V3 检索实现。"""

from search_v3 import *  # noqa: F401,F403
from search_v3 import main


if __name__ == "__main__":
    main()
