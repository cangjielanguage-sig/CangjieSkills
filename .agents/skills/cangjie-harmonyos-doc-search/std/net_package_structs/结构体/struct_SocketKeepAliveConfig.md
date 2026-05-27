## struct SocketKeepAliveConfig

```cangjie
public struct SocketKeepAliveConfig <: ToString & Equatable<SocketKeepAliveConfig> {
    public let count: UInt32
    public let idle: Duration
    public let interval: Duration
    public init(idle!: Duration = Duration.second * 45, interval!: Duration = Duration.second * 5, count!: UInt32 = 5)
}
```

功能：TCP KeepAlive 属性配置。

父类型：

- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)
- [Equatable](../../core/core_package_api/core_package_interfaces.md#interface-equatablet)\<[SocketKeepAliveConfig](#struct-socketkeepaliveconfig)>

### let count

```cangjie
public let count: UInt32
```

功能：查询连接是否失效的报文个数。

类型：[UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32)

### let idle

```cangjie
public let idle: Duration
```

功能：允许连接空闲的时长，空闲超长将关闭连接。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### let interval

```cangjie
public let interval: Duration
```

功能：保活报文发送周期。

类型：[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

### init(Duration, Duration, UInt32)

```cangjie
public init(idle!: Duration = Duration.second * 45, interval!: Duration = Duration.second * 5, count!: UInt32 = 5)
```

功能：初始化 [SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig) 实例对象。

参数：

- idle!: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 允许空闲的时长，默认 45 秒。
- interval!: [Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 保活报文发送周期，默认 45 秒。
- count!: [UInt32](../../core/core_package_api/core_package_intrinsics.md#uint32) - 查询连接是否失效的报文个数， 默认 5 个。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当配置为空闲状态或设置间隔小于 0 时，抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：将 TCP KeepAlive 属性配置转换为字符串。

返回值：

- [String](../../core/core_package_api/core_package_structs.md#struct-string) - 转换后的字符串。

### operator func !=(SocketKeepAliveConfig)

```cangjie
public override operator func !=(other: SocketKeepAliveConfig): Bool
```

功能：判断两个 [SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig) 实例是否不等。

参数：

- other: [SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig) - 参与比较的 [SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果不等，则返回 `true`；否则，返回 `false`。

### operator func ==(SocketKeepAliveConfig)

```cangjie
public override operator func ==(other: SocketKeepAliveConfig): Bool
```

功能：判断两个 [SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig) 实例是否相等。

参数：

- other: [SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig) - 参与比较的 [SocketKeepAliveConfig](net_package_structs.md#struct-socketkeepaliveconfig) 实例。

返回值：

- [Bool](../../core/core_package_api/core_package_intrinsics.md#bool) - 如果相等，则返回 `true`；否则，返回 `false`。