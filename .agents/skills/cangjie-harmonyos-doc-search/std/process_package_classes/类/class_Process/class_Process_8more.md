## class Process

```cangjie
public open class Process
```

功能：此类为进程类，提供进程操作相关功能。

> **说明：**
>
> 提供功能具体如下：
>
> - 提供获取当前进程实例的功能。
> - 提供根据进程 `id` 绑定进程实例的功能。
> - 提供根据输入信息创建子进程的功能。
> - 提供获取进程信息的功能。
> - 提供关闭进程的功能，允许设置是否强制关闭进程。

### static prop current <sup>(deprecated)</sup>

```cangjie
public static prop current: CurrentProcess
```

功能：获取当前进程实例。

> **注意：**
>
> 未来版本即将废弃，使用 [env](../../env/env_package_overview.md#函数) 包的全局函数替代。

类型：[CurrentProcess](process_package_classes.md#class-currentprocess-deprecated)

### prop arguments <sup>(deprecated)</sup>

```cangjie
public open prop arguments: Array<String>
```

功能：获取进程参数。`Windows` 平台下无法在非特权 `API` 下获取到本属性。

> **注意：**
>
> 未来版本即将废弃。

类型：[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>

异常：

- [ProcessException](process_package_exceptions.md#class-processexception) - 当进程不存在或对应进程为僵尸进程，或在 `Windows` 平台不支持场景下获取进程参数时，抛出异常。

### prop command

```cangjie
public prop command: String
```

功能：获取进程命令。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

异常：

- [ProcessException](process_package_exceptions.md#class-processexception) - 当进程不存在或对应进程为僵尸进程，无法获取进程命令时，抛出异常。

### prop commandLine <sup>(deprecated)</sup>

```cangjie
public prop commandLine: Array<String>
```

功能：获取当前进程命令行。对于 Windows 平台，只能获取当前进程的命令行，其他场景下无法在非特权 API 下获取到本属性。

> **注意：**
>
> 未来版本即将废弃，使用 [getcommandline()](../../env/env_package_api/env_package_funcs.md#func-getcommandline) 替代。

类型：[Array](../../core/core_package_api/core_package_structs.md#struct-arrayt)\<[String](../../core/core_package_api/core_package_structs.md#struct-string)>

异常：

- [ProcessException](process_package_exceptions.md#class-processexception) - 当进程不存在、对应进程为僵尸进程或在其他不支持的场景下无法获取进程命令行时，抛出异常。

### prop environment <sup>(deprecated)</sup>

```cangjie
public prop environment: Map<String, String>
```

功能：获取当前进程环境变量。对于 Windows 平台，只能获取当前进程的环境变量，其他场景下无法在非特权 API 下获取到本属性。

> **注意：**
>
> 未来版本即将废弃，使用 [getVariables()](../../env/env_package_api/env_package_funcs.md#func-getvariables) 替代。

类型：[Map](../../collection/collection_package_api/collection_package_interface.md#interface-mapk-v)\<[String](../../core/core_package_api/core_package_structs.md#struct-string), [String](../../core/core_package_api/core_package_structs.md#struct-string)>

异常：

- [ProcessException](process_package_exceptions.md#class-processexception) - 当进程不存在、对应进程为僵尸进程或在其他不支持的场景下无法获取进程环境变量时，抛出异常。

### prop name

```cangjie
public prop name: String
```

功能：获取进程名。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

异常：

- [ProcessException](process_package_exceptions.md#class-processexception) - 当进程不存在或对应进程为僵尸进程，无法获取进程名时，抛出异常。

### prop pid

```cangjie
public prop pid: Int64
```

功能：获取进程 `id`。

类型：[Int64](../../core/core_package_api/core_package_intrinsics.md#int64)