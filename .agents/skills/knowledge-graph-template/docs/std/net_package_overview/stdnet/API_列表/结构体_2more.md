### 结构体

|              结构体名          |           功能           |
| --------------------------- | ------------------------ |
| [AddressFamily](./net_package_api/net_package_structs.md#struct-addressfamily) | 地址族用于在个别地址的使用可能不明确的上下文中标识用于网络通信的个别网络地址方案或编号计划。 |
| [OptionLevel](./net_package_api/net_package_structs.md#struct-optionlevel) | 提供了常用的套接字选项级别。 |
| [OptionName](./net_package_api/net_package_structs.md#struct-optionname) | 提供了常用的套接字选项。 |
| [ProtocolType](./net_package_api/net_package_structs.md#struct-protocoltype) | 提供了常用的套接字协议，以及通过指定 `Int32` 值来构建套接字协议的功能。 |
| [RawAddress](./net_package_api/net_package_structs.md#struct-rawaddress) | 提供了 `RawSocket` 的通信地址创建和获取功能。 |
| [SocketDomain](./net_package_api/net_package_structs.md#struct-socketdomain) | 提供了常用的套接字通信域，以及通过指定 `Int32` 值来构建套接字通信域的功能。 |
| [SocketKeepAliveConfig](./net_package_api/net_package_structs.md#struct-socketkeepaliveconfig) | TCP KeepAlive 属性配置。 |
| [SocketOptions](./net_package_api/net_package_structs.md#struct-socketoptions) | `SocketOptions` 存储了设置套接字选项的一些参数常量方便后续调用。|
| [SocketType](./net_package_api/net_package_structs.md#struct-sockettype) | 提供了常用的套接字类型，以及通过指定 `Int32` 值来构建套接字类型的功能。 |

### 异常类

|              异常类名          |           功能           |
| --------------------------- | ------------------------ |
| [SocketException](./net_package_api/net_package_exceptions.md#class-socketexception) | 提供套接字相关的异常处理。 |
| [SocketTimeoutException](./net_package_api/net_package_exceptions.md#class-sockettimeoutexception) | 提供字符格式相关的异常处理。 |