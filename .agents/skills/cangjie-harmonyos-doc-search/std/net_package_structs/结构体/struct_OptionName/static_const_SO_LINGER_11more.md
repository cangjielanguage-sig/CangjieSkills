### static const SO_LINGER

```cangjie
public static const SO_LINGER: Int32
```

功能：用于设置套接字关闭时行为的套接字选项。不同系统下的值分别为：

- macOS: 0x0080
- Windows: 0x0080
- 其他情况：0x000D

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_OOBINLINE

```cangjie
public static const SO_OOBINLINE: Int32
```

功能：用于控制接收带外数据方式的套接字选项。不同系统下的值分别为：

- macOS: 0x0100
- Windows: 0x0100
- 其他情况：0x000A

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_RCVBUF

```cangjie
public static const SO_RCVBUF: Int32
```

功能：用于设置套接字接收缓冲区大小的套接字选项。不同系统下的值分别为：

- macOS: 0x1002
- Windows: 0x1002
- 其他情况：0x0008

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_RCVTIMEO

```cangjie
public static const SO_RCVTIMEO: Int32
```

功能：用于设置套接字接收数据超时时间的套接字选项。不同系统下的值分别为：

- macOS: 0x1006
- Windows: 0x1006
- 其他情况：0x0014

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_REUSEADDR

```cangjie
public static const SO_REUSEADDR: Int32
```

功能：用于在套接字关闭后立即释放其绑定端口，以便其他套接字可以立即绑定该端口的套接字选项。不同系统下的值分别为：

- macOS: 0x0004
- Windows: 0x0004
- 其他情况：0x0002

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_SNDBUF

```cangjie
public static const SO_SNDBUF: Int32
```

功能：用于设置套接字发送缓冲区大小的套接字选项。不同系统下的值分别为：

- macOS: 0x1001
- Windows: 0x1001
- 其他情况：0x0007

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const SO_SNDTIMEO

```cangjie
public static const SO_SNDTIMEO: Int32
```

功能：用于设置套接字发送数据超时时间的套接字选项。不同系统下的值分别为：

- macOS: 0x1005
- Windows: 0x1005
- 其他情况：0x0015

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const TCP_KEEPCNT

```cangjie
public static const TCP_KEEPCNT: Int32
```

功能：用于控制 TCP 连接中发送保持存活探测报文次数的套接字选项。不同系统下的值分别为：

- macOS: 0x0102
- Windows: 0x0010
- 其他情况：0x0006

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const TCP_KEEPIDLE

```cangjie
public static const TCP_KEEPIDLE: Int32
```

功能：用于设置在没有收到对端确认的情况下，`TCP` 保持连接最大次数的套接字选项。不同系统下的值分别为：

- macOS: 0x0010
- Windows: 0x0003
- 其他情况：0x0004

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const TCP_KEEPINTVL

```cangjie
public static const TCP_KEEPINTVL: Int32
```

功能：用于设置 `TCP` 保持连接时发送探测报文时间间隔的套接字选项。不同系统下的值分别为：

- macOS: 0x0101
- Windows: 0x0011
- 其他情况：0x0005

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)

### static const TCP_NODELAY

```cangjie
public static const TCP_NODELAY: Int32 = 0x0001
```

功能：用于控制 `TCP` 协议延迟行为的套接字选项。

类型：[Int32](../../core/core_package_api/core_package_intrinsics.md#int32)