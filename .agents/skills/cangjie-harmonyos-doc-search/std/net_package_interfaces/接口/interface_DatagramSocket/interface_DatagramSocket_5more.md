## interface DatagramSocket

```cangjie
public interface DatagramSocket <: Resource & ToString {
    prop localAddress: SocketAddress
    prop remoteAddress: ?SocketAddress
    mut prop receiveTimeout: ?Duration
    mut prop sendTimeout: ?Duration
    func receiveFrom(buffer: Array<Byte>): (SocketAddress, Int64)
    func sendTo(address: SocketAddress, payload: Array<Byte>): Unit
}
```

功能：[DatagramSocket](net_package_interfaces.md#interface-datagramsocket) 是一种接收和读取数据包的套接字。

一个数据包通常有有限的大小，可能为空。不同的数据包套接字类型有不同的数据包最大值。例如 `UDP` 套接字一次可以处理最大 64KB 的数据包。
数据包传输不是一种可靠的传输，不保证传输顺序。数据包大小在发送端决定，例如：一端发送了 10 字节和 15 字节的报文，对端将收到相同大小的对应报文，10 字节和 15 字节。

父类型：

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

### prop receiveTimeout

```cangjie
mut prop receiveTimeout: ?Duration
```

功能：设置和读取 `receiveFrom` 超时时间，无超时时间设置为 `None`。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。

### prop remoteAddress

```cangjie
prop remoteAddress: ?SocketAddress
```

功能：读取 `Socket` 已经连接的远端地址，当 `Socket` 未连接时返回 None。

类型：?[SocketAddress](net_package_classes.md#class-socketaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当 `Socket` 已经被关闭时，抛出异常。

### prop sendTimeout

```cangjie
mut prop sendTimeout: ?Duration
```

功能：设置和读取 `sendTo` 超时时间，默认设置为 `None`。

如果设置的时间过小将会设置为最小时钟周期值；过大时将设置为最大超时时间（2<sup>63</sup>-1 纳秒）；默认值为 `None`。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当超时时间小于 0 时，抛出异常。