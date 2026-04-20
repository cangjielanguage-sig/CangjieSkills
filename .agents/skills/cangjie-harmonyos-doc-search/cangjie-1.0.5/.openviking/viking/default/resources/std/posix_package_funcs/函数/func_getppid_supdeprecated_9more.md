## func getppid() <sup>(deprecated)</sup>

```cangjie
public func getppid(): Int32
```

功能：获取调用进程的父进程 `ID`。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 返回调用进程的父进程 `ID`。

## func getuid() <sup>(deprecated)</sup>

```cangjie
public func getuid(): UInt32
```

功能：获取调用进程的真实用户 `ID`。

> **注意：**
>
> 未来版本即将废弃。

返回值：

- [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 当前真实用户 `ID`。

## func isatty(Int32) <sup>(deprecated)</sup>

```cangjie
public func isatty(fd: Int32): Bool
```

功能：用于测试文件描述符是否引用终端，成功时返回 `true`，否则返回 `false`。

> **注意：**
>
> 未来版本即将废弃。

参数：

- fd: [Int32](../../core/core_package_api/core_package_intrinsics.md#int32) - 文件描述符。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 操作成功时返回 `true`，否则返回 `false`。

## func isBlk(String) <sup>(deprecated)</sup>

```cangjie
public func isBlk(path: String): Bool
```

功能：检查传入对象是否为块设备，并返回布尔类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是，返回 `true`，否则返回 `false`。

## func isChr(String) <sup>(deprecated)</sup>

```cangjie
public func isChr(path: String): Bool
```

功能：检查传入对象是否为字符设备，返回布尔类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是，返回 `true`，否则返回 `false`。

## func isDir(String) <sup>(deprecated)</sup>

```cangjie
public func isDir(path: String): Bool
```

功能：检查传入对象是否为文件夹，返回布尔类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是，返回 `true`，否则返回 `false`。

## func isFIFO(String) <sup>(deprecated)</sup>

```cangjie
public func isFIFO(path: String): Bool
```

功能：检查传入对象是否为 `FIFO` 文件，返回布尔类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是，返回 `true`，否则返回 `false`。

## func isLnk(String) <sup>(deprecated)</sup>

```cangjie
public func isLnk(path: String): Bool
```

功能：检查传入对象是否为软链路，返回布尔类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是，返回 `true`，否则返回 `false`。

## func isReg(String) <sup>(deprecated)</sup>

```cangjie
public func isReg(path: String): Bool
```

功能：检查传入对象是否为普通文件，返回布尔类型。

> **注意：**
>
> 未来版本即将废弃。

参数：

- path: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 文件路径。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果是，返回 `true`，否则返回 `false`。