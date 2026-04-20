### 接口

|              接口名          |           功能           |
| --------------------------- | ------------------------ |
| [DatagramSocket](./net_package_api/net_package_interfaces.md#interface-datagramsocket) | `DatagramSocket` 是一种接收和读取数据包的套接字。 |
| [ServerSocket](./net_package_api/net_package_interfaces.md#interface-serversocket) | 提供服务端的 `Socket` 需要的接口。 |
| [StreamingSocket](./net_package_api/net_package_interfaces.md#interface-streamingsocket) | 双工流模式下的运行的 `Socket`，可被读写。 |

### 类

|              类名          |           功能           |
| --------------------------- | ------------------------ |
| [IPAddress](./net_package_api/net_package_classes.md#class-ipaddress) | 此类表示 Internet 协议（IP）地址。 |
| [IPPrefix](./net_package_api/net_package_classes.md#class-ipprefix) | 这个类表示一个 IP 前缀（也称为“IP 子网”），即一个连续的 IP 地址块，边界为 2 的幂。 |
| [IPSocketAddress](./net_package_api/net_package_classes.md#class-ipsocketaddress) | 此类实现了 IP 协议 Socket 地址（IP 地址+端口号）。 |
| [IPv4Address](./net_package_api/net_package_classes.md#class-ipv4address) | 此类表示 Internet 协议版本 4（IPv4）地址。 |
| [IPv6Address](./net_package_api/net_package_classes.md#class-ipv6address) | 此类表示 Internet 协议版本 6（IPv6）地址。 |
| [RawSocket](./net_package_api/net_package_classes.md#class-rawsocket) | `RawSocket` 提供了套接字的基本功能。 |
| [SocketAddress](./net_package_api/net_package_classes.md#class-socketaddress) | 此类表示协议无关的 Socket 地址。 |
| [TcpServerSocket](./net_package_api/net_package_classes.md#class-tcpserversocket) | 监听 TCP 连接的服务端。 |
| [TcpSocket](./net_package_api/net_package_classes.md#class-tcpsocket) | 请求 TCP 连接的客户端。|
| [UdpSocket](./net_package_api/net_package_classes.md#class-udpsocket) | 提供 udp 报文通信。 |
| [UnixDatagramSocket](./net_package_api/net_package_classes.md#class-unixdatagramsocket) | 提供基于数据包的主机通讯能力。 |
| [UnixServerSocket](./net_package_api/net_package_classes.md#class-unixserversocket) | 提供基于双工流的主机通讯服务端。 |
| [UnixSocket](./net_package_api/net_package_classes.md#class-unixsocket) | 提供基于双工流的主机通讯客户端。 |
| [UnixSocketAddress](./net_package_api/net_package_classes.md#class-unixsocketaddress) | 此类实现了 Unix Domain Socket 地址。 |

### 枚举

|              枚举名          |           功能           |
| --------------------------- | ------------------------ |
| [SocketNet](./net_package_api/net_package_enums.md#enum-socketnet) | 传输层协议类型。 |