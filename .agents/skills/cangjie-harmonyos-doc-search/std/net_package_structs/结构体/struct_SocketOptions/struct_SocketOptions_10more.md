## struct SocketOptions

```cangjie
public struct SocketOptions {
    public static const IPPROTO_TCP: Int32 = 6
    public static const IPPROTO_UDP: Int32 = 17
    public static const SOL_SOCKET: Int32
    public static const SO_BINDTODEVICE: Int32
    public static const SO_KEEPALIVE: Int32
    public static const SO_LINGER: Int32
    public static const SO_RCVBUF: Int32
    public static const SO_REUSEADDR: Int32
    public static const SO_REUSEPORT: Int32
    public static const SO_SNDBUF: Int32
    public static const TCP_NODELAY: Int32 = 0x0001
    public static const TCP_QUICKACK: Int32
}
```

功能：[SocketOptions](net_package_structs.md#struct-socketoptions) 存储了设置套接字选项的一些参数常量方便后续调用。

### const IPPROTO_TCP <sup>(deprecated)</sup>

```cangjie
public static const IPPROTO_TCP: Int32 = 6
```

功能：常数，用于将套接字选项的 `level` 层级设为 `IPPROTO_TCP`。

> **注意：**
>
> 未来版本即将废弃不再使用，使用 [OptionLevel.TCP](#static-const-tcp) 替代。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const IPPROTO_UDP <sup>(deprecated)</sup>

```cangjie
public static const IPPROTO_UDP: Int32 = 17
```

功能：常数，用于将套接字选项的 `level` 层级设为 `IPPROTO_UDP`。

> **注意：**
>
> 未来版本即将废弃不再使用，使用 [OptionLevel.UDP](#static-const-udp) 替代。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const SO_BINDTODEVICE

```cangjie
public static const SO_BINDTODEVICE: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `SO_BINDTODEVICE`。不同系统下的值分别为：

- macOS: 0xFFFF
- Windows: 0xFFFF
- 其他情况：0x0019

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const SO_KEEPALIVE

```cangjie
public static const SO_KEEPALIVE: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `SO_KEEPALIVE`。不同系统下的值分别为：

- macOS: 0x0008
- Windows: 0x0008
- 其他情况：0x0009

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const SO_LINGER

```cangjie
public static const SO_LINGER: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `SO_LINGER`。不同系统下的值分别为：

- macOS: 0x0080
- Windows: 0x0080
- 其他情况：0x000D

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const SO_RCVBUF

```cangjie
public static const SO_RCVBUF: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `SO_RCVBUF`。不同系统下的值分别为：

- macOS: 0x1002
- Windows: 0x1002
- 其他情况：0x0008

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const SO_REUSEADDR

```cangjie
public static const SO_REUSEADDR: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `SO_REUSEADDR`。不同系统下的值分别为：

- macOS: 0x0004
- Windows: 0x0004
- 其他情况：0x0002

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const SO_REUSEPORT

```cangjie
public static const SO_REUSEPORT: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `SO_REUSEPORT`。不同系统下的值分别为：

- macOS: 0x0200
- Windows: 0xFFFF
- 其他情况：0x000F

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### const SO_SNDBUF

```cangjie
public static const SO_SNDBUF: Int32
```

功能：常数，用于将套接字选项的 `optname` 设为 `SO_SNDBUF`。不同系统下的值分别为：

- macOS: 0x1001
- Windows: 0x1001
- 其他情况：0x0007

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)