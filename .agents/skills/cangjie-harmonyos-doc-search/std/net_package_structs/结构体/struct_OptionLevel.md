## struct OptionLevel

```cangjie
public struct OptionLevel {
    public static const ICMP: Int32 = 1
    public static const IP: Int32 = 0
    public static const RAW: Int32 = 255
    public static const SOCKET: Int32
    public static const TCP: Int32 = 6
    public static const UDP: Int32 = 17
}
```

功能：提供了常用的套接字选项级别。

### static const ICMP

```cangjie
public static const ICMP: Int32 = 1
```

功能：控制 `ICMP` 协议行为的套接字选项级别。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const IP

```cangjie
public static const IP: Int32 = 0
```

功能：控制 IP 协议行为的套接字选项级别。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const RAW

```cangjie
public static const RAW: Int32 = 255
```

功能：控制 `RAW` 协议行为的套接字选项级别。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SOCKET

```cangjie
public static const SOCKET: Int32
```

功能：控制基本套接字行为的套接字选项级别。不同系统下的值分别为：

- macOS: 0xFFFF
- Windows: 0xFFFF
- 其他情况：1

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const TCP

```cangjie
public static const TCP: Int32 = 6
```

功能：控制 `TCP` 协议行为的套接字选项级别。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const UDP

```cangjie
public static const UDP: Int32 = 17
```

功能：控制 `UDP` 协议行为的套接字选项级别。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)