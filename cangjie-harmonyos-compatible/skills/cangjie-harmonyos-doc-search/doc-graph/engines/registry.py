"""图谱引擎注册表 — 管理所有已注册的图谱引擎插件。

采用单例注册模式：引擎类通过 @register 装饰器自动注册，
运行时通过 get_engine()/create_engine() 查找和实例化。
注册键由类名去掉 "Engine" 后缀得到（如 GraphifyEngine → "graphify"）。
"""

from typing import Optional, Type
from .base import GraphEngine

_registry: dict[str, Type[GraphEngine]] = {}


def register(engine_cls: Type[GraphEngine]) -> Type[GraphEngine]:
    """注册图谱引擎 — 作为类装饰器使用。

    注册键 = 类名小写 + 去掉 "engine" 后缀，如 GraphifyEngine → "graphify"。
    返回原类不变，不影响继承链。
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
