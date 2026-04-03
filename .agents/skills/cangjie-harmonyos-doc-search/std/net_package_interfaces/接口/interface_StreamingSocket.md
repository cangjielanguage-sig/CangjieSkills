## interface StreamingSocket

```cangjie
public interface StreamingSocket <: IOStream & Resource & ToString {
    prop localAddress: SocketAddress
    prop remoteAddress: SocketAddress
    mut prop readTimeout: ?Duration
    mut prop writeTimeout: ?Duration
}
```

功能：双工流模式下的运行的 `Socket`，可被读写。

[StreamingSocket](net_package_interfaces.md#interface-streamingsocket) 可以被绑定 (`bind`) 和连接 (`connect`)，用户可以通过属性设置绑定和连接的远端和本地地址。
[StreamingSocket](net_package_interfaces.md#interface-streamingsocket) 可以有序分包传输字节流。我们会使用一段缓存空间存储读写的字节流。读取接口 (`read()`) 默认在无数据到来时阻塞式等待，直到下一次数据到达或超时。写操作 (`write()`) 会写入缓存中的数据并在后续被发出，如果缓存不足，或者写入速度快于转发速度，写操作将会阻塞等待缓存空闲，或超时。
读写字符始终保持有序，但不保证传输过程中的分包策略及大小与发包时一致。例如：一端发送 10 字节报文后，又发送了 15 字节报文，对端可能分别收到 10 字节 和 15 字节报文，也可能一次性收到 25 字节的一个报文。
当收到一段异常报文时，将返回报文长度为 -1 。

父类型：

- [IOStream](../../io/io_package_api/io_package_interfaces.md#interface-iostream)
- [Resource](../../core/core_package_api/core_package_interfaces.md#interface-resource)
- [ToString](../../core/core_package_api/core_package_interfaces.md#interface-tostring)

### prop localAddress

```cangjie
prop localAddress: SocketAddress
```

功能：读取 `Socket` 将要或已经被绑定的本地地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭或无可用的本地地址（本地地址未配置并且套接字未连接）时，抛出异常。

### prop readTimeout

```cangjie
mut prop readTimeout: ?Duration
```

功能：设置和读取读超时时间。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### prop remoteAddress

```cangjie
prop remoteAddress: SocketAddress
```

功能：读取 `Socket` 将要或已经连接的远端地址。

类型：[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭时，抛出异常。

### prop writeTimeout

```cangjie
mut prop writeTimeout: ?Duration
```

功能：设置和读取写超时时间。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。