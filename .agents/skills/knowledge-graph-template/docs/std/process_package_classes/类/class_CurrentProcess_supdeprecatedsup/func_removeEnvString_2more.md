### func removeEnv(String)

```cangjie
public func removeEnv(k: String): Unit
```

功能：通过指定环境变量名称移除环境变量。

参数：

- k: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 环境变量名称。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `k` 包含空字符时，抛出异常。

### func setEnv(String, String)

```cangjie
public func setEnv(k: String, v: String): Unit
```

功能：用于设置一对环境变量。如果设置了同名环境变量，原始环境变量值将被覆盖。

> **说明：**
>
> Windows 下如果传入的参数 v 是空字符串，那么会从环境中移除变量 k。

参数：

- k: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 环境变量名称。
- v: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 环境变量值。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当函数参数 `k` 或 `v` 中包含空字符时，抛出异常。