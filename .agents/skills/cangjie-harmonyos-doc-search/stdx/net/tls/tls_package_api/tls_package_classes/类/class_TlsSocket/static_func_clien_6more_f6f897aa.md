### static func client(StreamingSocket, ?TlsSession, TlsClientConfig)

```cangjie
public static func client(
    socket: StreamingSocket,
    session!: ?TlsSession = None,
    clientConfig!: TlsClientConfig = TlsClientConfig()
): TlsSocket
```

功能：根据传入的 StreamingSocket 实例创建指定地址的客户端 TLS 套接字，该套接字可用于客户端 TLS 握手及会话。

参数：

- socket: StreamingSocket - 已连接到服务端的客户端 TCP 套接字。
- session!: ?[TlsSession](tls_package_structs.md#struct-tlssession) - TLS 会话 id，若存在可用的 TLS 会话， 则可通过该 id 恢复历史 TLS 会话，省去 TLS 建立连接时间，但使用该会话依然可能协商失败。默认为 `None`。
- clientConfig!: [TlsClientConfig](tls_package_structs.md#struct-tlsclientconfig) - 客户端配置，默认为 [TlsClientConfig](tls_package_structs.md#struct-tlsclientconfig)()。

返回值：

- [TlsSocket](tls_package_classes.md#class-tlssocket) - 构造出的 [TlsSocket](tls_package_classes.md#class-tlssocket) 实例。

### static func server(StreamingSocket, ?TlsSessionContext, TlsServerConfig)

```cangjie
public static func server(
    socket: StreamingSocket,
    sessionContext!: ?TlsSessionContext = None,
    serverConfig!: TlsServerConfig
): TlsSocket
```

功能：根据传入的 StreamingSocket 实例创建指定地址的服务端 TLS 套接字，该套接字可用于服务端 TLS 握手及会话。

参数：

- socket: StreamingSocket - TCP 连接建立完成后接受到套接字。
- sessionContext!: ?[TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) - TLS 会话 id， 若存在可用的 TLS 会话， 则可通过该 id 恢复历史 TLS 会话，省去 TLS 建立连接时间，但使用该会话依然可能协商失败。默认为 None。
- serverConfig!: [TlsServerConfig](tls_package_structs.md#struct-tlsserverconfig) - 服务端配置，默认为 [TlsServerConfig](tls_package_structs.md#struct-tlsserverconfig)()。

返回值：

- [TlsSocket](tls_package_classes.md#class-tlssocket) - 构造出的 [TlsSocket](tls_package_classes.md#class-tlssocket) 实例。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭套接字。

异常：

- SocketException - 底层连接无法关闭时，抛出异常。

### func handshake(?Duration)

```cangjie
public func handshake(timeout!: ?Duration = None): Unit
```

功能：TLS 握手。不支持重新协商握手，因此只能被调用一次。调用对象可以为客户端或者服务端的 [TlsSocket](tls_package_classes.md#class-tlssocket)。

参数：

- timeout!: ?Duration - 握手超时时间，默认为 None 不对超时时间进行设置，此时采用默认 30s 的超时时间。

异常：

- SocketException - 本端建连的底层 TCP 套接字关闭，抛出异常。
- SocketTimeoutException - 底层 TCP 套接字连接超时时，抛出异常。
- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当握手已经开始或者已经结束，抛出异常；或当握手阶段出现系统错误时，抛出异常。
- IllegalArgumentException - 设定的握手超时时间为负值时，抛出异常。

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：返回 TLS 套接字对象的哈希值。

返回值：

- Int64 - 对 TLS 套接字对象进行哈希计算后得到的结果。

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：返回套接字是否关闭的状态。

返回值：

- Bool - 连接断开返回 true；否则，返回 false。