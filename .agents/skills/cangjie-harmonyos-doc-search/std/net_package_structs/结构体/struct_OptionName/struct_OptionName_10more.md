## struct OptionName

```cangjie
public struct OptionName {
    public static const IP_HDRINCL: Int32
    public static const IP_TOS: Int32
    public static const IP_TTL: Int32
    public static const SO_ACCEPTCONN: Int32
    public static const SO_BROADCAST: Int32
    public static const SO_DEBUG: Int32 = 0x0001
    public static const SO_DONTROUTE: Int32
    public static const SO_ERROR: Int32
    public static const SO_KEEPALIVE: Int32
    public static const SO_LINGER: Int32
    public static const SO_OOBINLINE: Int32
    public static const SO_RCVBUF: Int32
    public static const SO_RCVTIMEO: Int32
    public static const SO_REUSEADDR: Int32
    public static const SO_SNDBUF: Int32
    public static const SO_SNDTIMEO: Int32
    public static const TCP_KEEPCNT: Int32
    public static const TCP_KEEPIDLE: Int32
    public static const TCP_KEEPINTVL: Int32
    public static const TCP_NODELAY: Int32 = 0x0001
}
```

功能：提供了常用的套接字选项。

### static const IP_HDRINCL

```cangjie
public static const IP_HDRINCL: Int32
```

功能：用于在发送数据包时指定 IP 头部是否由应用程序提供的套接字选项。不同系统下的值分别为：

- macOS: 0x0002
- Windows: 0x0002
- 其他情况：0x0003

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const IP_TOS

```cangjie
public static const IP_TOS: Int32
```

功能：用于指定数据包服务类型和优先级的套接字选项。不同系统下的值分别为：

- macOS: 0x0003
- Windows: 0x0003
- 其他情况：0x0001

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const IP_TTL

```cangjie
public static const IP_TTL: Int32
```

功能：用于限制 IP 数据包在网络中传输最大跳数的套接字选项。不同系统下的值分别为：

- macOS: 0x0004
- Windows: 0x0004
- 其他情况：0x0002

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_ACCEPTCONN

```cangjie
public static const SO_ACCEPTCONN: Int32
```

功能：用于查询套接字是否处于监听状态的套接字选项。不同系统下的值分别为：

- macOS: 0x0002
- Windows: 0x0002
- 其他情况：0x001E

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_BROADCAST

```cangjie
public static const SO_BROADCAST: Int32
```

功能：用于设置套接字是否允许发送广播消息的套接字选项。不同系统下的值分别为：

- macOS: 0x0020
- Windows: 0x0020
- 其他情况：0x0006

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_DEBUG

```cangjie
public static const SO_DEBUG: Int32 = 0x0001
```

功能：用于启用或禁用调试模式的套接字选项。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_DONTROUTE

```cangjie
public static const SO_DONTROUTE: Int32
```

功能：用于在连接套接字时，不路由套接字数据包的套接字选项。不同系统下的值分别为：

- macOS: 0x0010
- Windows: 0x0010
- 其他情况：0x0005

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_ERROR

```cangjie
public static const SO_ERROR: Int32
```

功能：获取和清除套接字上错误状态的套接字选项。不同系统下的值分别为：

- macOS: 0x1007
- Windows: 0x1007
- 其他情况：0x0004

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_KEEPALIVE

```cangjie
public static const SO_KEEPALIVE: Int32
```

功能：用于检测 `TCP` 连接是否仍然处于活动状态的套接字选项。不同系统下的值分别为：

- macOS: 0x0008
- Windows: 0x0008
- 其他情况：0x0009

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)