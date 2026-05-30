"""图谱引擎注册表。

管理所有已注册的图谱引擎插件。
"""

from typing import Optional, Type
from .base import GraphEngine

_registry: dict[str, Type[GraphEngine]] = {}


def register(engine_cls: Type[GraphEngine]) -> Type[GraphEngine]:
    """注册图谱引擎。

    用法：
        @register
        class MyEngine(GraphEngine):
            ...
    """
    _registry[engine_cls.__name__.lower().replace("engine", "")] = engine_cls
    return engine_cls


def get_engine(name: str) -> Optional[Type[GraphEngine]]:
    """获取已注册的引擎类。"""
    return _registry.get(name.lower())


def list_engines() -> list[str]:
    """列出所有已注册的引擎。"""
    return list(_registry.keys())


def create_engine(name: str, **kwargs) -> GraphEngine:
    """创建引擎实例。

    Args:
        name: 引擎名称
        **kwargs: 传递给引擎构造函数的参数

    Returns:
        引擎实例
    """
    cls = get_engine(name)
    if cls is None:
        available = ", ".join(list_engines())
        raise ValueError(f"未知引擎: {name}。可用引擎: {available}")
    return cls(**kwargs)
