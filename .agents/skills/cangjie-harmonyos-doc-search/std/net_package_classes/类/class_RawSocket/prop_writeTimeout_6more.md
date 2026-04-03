### prop writeTimeout

```cangjie
public mut prop writeTimeout: ?Duration
```

功能：获取或设置当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例的写超时时间。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当设置的写超时时间为负时，抛出异常。

### init(SocketDomain, SocketType, ProtocolType)

```cangjie
public init(domain: SocketDomain, `type`: SocketType, protocol: ProtocolType)
```

功能：创建特定通信域、类型、协议组合的套接字。

参数：

- domain: [SocketDomain](net_package_structs.md#struct-socketdomain) - 通信域。
- \`type`: [SocketType](net_package_structs.md#struct-sockettype) - 套接字类型。
- protocol: [ProtocolType](net_package_structs.md#struct-protocoltype) - 协议类型。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当通信域、类型、协议组合无法创建套接字时，抛出异常。

### func accept(?Duration)

```cangjie
public func accept(timeout!: ?Duration = None): RawSocket
```

功能：接收当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例监听时挂起连接队列上的第一个连接请求，返回一个用于通信的 [RawSocket](net_package_classes.md#class-rawsocket)。

参数：

- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待连接请求的最大时间，默认值 `None` 表示一直等待。

返回值：

- [RawSocket](net_package_classes.md#class-rawsocket) - 用于通信的新 [RawSocket](net_package_classes.md#class-rawsocket) 实例。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或接收失败时，抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当等待超时时，抛出异常。

### func bind(RawAddress)

```cangjie
public func bind(addr: RawAddress): Unit
```

功能：将当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例与指定的套接字地址进行绑定。

参数：

- addr: [RawAddress](net_package_structs.md#struct-rawaddress) - 套接字地址。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或绑定失败时，抛出异常。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例。

### func connect(RawAddress, ?Duration)

```cangjie
public func connect(addr: RawAddress, timeout!: ?Duration = None): Unit
```

功能：向目标地址发送连接请求。

参数：

- addr: [RawAddress](net_package_structs.md#struct-rawaddress) - 发送连接请求的目标地址。
- timeout!: ?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration) - 等待连接接收的最大时间，默认值 `None` 表示一直等待。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或接收失败时，抛出异常。
- [SocketTimeoutException](net_package_exceptions.md#class-sockettimeoutexception) - 当等待超时时，抛出异常。