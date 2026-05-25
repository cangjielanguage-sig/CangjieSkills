### init(SocketAddress)

```cangjie
public init(bindAt!: SocketAddress)
```

功能：创建一个未连接的 [UnixDatagramSocket](net_package_classes.md#class-unixdatagramsocket) 实例。

此文件类型可通过 [isSock](../../posix/posix_package_api/posix_package_funcs.md#func-issockstring-deprecated)() 判断是否存在，可通过 [unlink()](../../posix/posix_package_api/posix_package_funcs.md#func-unlinkstring-deprecated) 接口删除。

参数：

- bindAt!: [SocketAddress](net_package_classes.md#class-socketaddress) - 连接的套接字地址。地址应当不存在，在 `bind` 时会创建。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当路径为空或已存在时，抛出异常。

### init(String)

```cangjie
public init(bindAt!: String)
```

功能：创建一个未连接的 [UnixDatagramSocket](net_package_classes.md#class-unixdatagramsocket) 实例。

此文件类型可通过 [isSock()](../../posix/posix_package_api/posix_package_funcs.md#func-issockstring-deprecated) 判断是否存在，可通过 [unlink()](../../posix/posix_package_api/posix_package_funcs.md#func-unlinkstring-deprecated) 接口删除。

参数：

- bindAt!: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 连接的文件地址。文件地址应当不存在，在 `bind` 时会创建。

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当文件地址不合法时，抛出异常。
- [SocketException](net_package_exceptions.md#class-socketexception) - 当文件地址为空或已存在时，抛出异常。

### func bind()

```cangjie
public func bind(): Unit
```

功能：绑定一个 `Unix datagram` 套接字，并创建监听队列。

此接口自动在本地地址中创建一个套接字文件，如该文件已存在则会绑定失败。此文件类型可通过 [isSock()](../../posix/posix_package_api/posix_package_funcs.md#func-issockstring-deprecated) 判断是否存在，可通过 [unlink()](../../posix/posix_package_api/posix_package_funcs.md#func-unlinkstring-deprecated) 接口删除，失败后需要 `close` 套接字，不支持多次重试。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当文件地址已存在，或文件创建失败时，抛出异常。

### func close()

```cangjie
public override func close(): Unit
```

功能：关闭套接字，所有操作除了 `close/isClosed` 之外，均不允许再调用。接口允许多次调用。

### func connect(SocketAddress)

```cangjie
public func connect(remote: SocketAddress): Unit
```

功能：连接特定远端地址，可通过 `disconnect` 撤销配置。

仅接受该远端地址的报文。默认执行 `bind`，因此不需额外调用 `bind`。此操作执行后，端口将开始接收 ICMP 报文，若收到异常报文后，可能导致 `send/sendTo` 执行失败。

参数：

- remote: [SocketAddress](net_package_classes.md#class-socketaddress) - 远端套接字地址。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当地址未绑定时，抛出异常。

### func connect(String)

```cangjie
public func connect(remotePath: String): Unit
```

功能：连接特定远端地址，可通过 `disconnect` 撤销配置。

仅接受该远端地址的报文。必须在 `bind` 后调用。此操作执行后，端口将开始接收 ICMP 报文，若收到异常报文后，可能导致 `send/sendTo` 执行失败。

参数：

- remotePath: [String](../../core/core_package_api/core_package_structs.md#struct-string) - 远端文件地址。

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当地址未绑定时，抛出异常。