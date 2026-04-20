## class RawSocket

```cangjie
public class RawSocket {
    public init(domain: SocketDomain, `type`: SocketType, protocol: ProtocolType)
}
```

功能：[RawSocket](net_package_classes.md#class-rawsocket) 提供了套接字的基本功能。

可以访问特定通信域（domain）、类型（type）和协议（protocol）组合的套接字。Socket 包已经提供了 TCP、 UDP 等常用网络协议的支持，因此，该类型适用于其他类型的网络编程需求。

> **注意：**
>
> - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 已经验证的功能包括 TCP、UDP、UDS 以及 ICMP 协议套接字，其他类型使用上可能存在预期之外的问题。
> - 此外，由于接口的开放性，可以使用 `connect` 再 `listen` 的组合，部分场景可能存在预期外的问题。建议开发者使用时遵循正常的调用逻辑，避免产生问题。

### prop localAddr <sup>(deprecated)</sup>

```cangjie
public prop localAddr: RawAddress
```

功能：获取当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例的本地地址。

> **注意：**
>
> 未来版本即将废弃不再使用，使用 [localAddress](#prop-localaddress) 替代。

类型：[RawAddress](net_package_structs.md#struct-rawaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或无法获取本地地址时，抛出异常。

### prop localAddress

```cangjie
public prop localAddress: RawAddress
```

功能：获取当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例的本地地址。

类型：[RawAddress](net_package_structs.md#struct-rawaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或无法获取本地地址时，抛出异常。

### prop readTimeout

```cangjie
public mut prop readTimeout: ?Duration
```

功能：获取或设置当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例的读超时时间。

类型：?[Duration](../../core/core_package_api/core_package_structs.md#struct-duration)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭时，抛出异常。
- [IllegalArgumentException](../../core/core_package_api/core_package_exceptions.md#class-illegalargumentexception) - 当设置的读超时时间为负时，抛出异常。

### prop remoteAddr <sup>(deprecated)</sup>

```cangjie
public prop remoteAddr: RawAddress
```

功能：获取当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例的对端地址。

> **注意：**
>
> 未来版本即将废弃不再使用，使用 [remoteAddress](#prop-remoteaddress) 替代。

类型：[RawAddress](net_package_structs.md#struct-rawaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或无法获取对端地址时，抛出异常。

### prop remoteAddress

```cangjie
public prop remoteAddress: RawAddress
```

功能：获取当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例的对端地址。

类型：[RawAddress](net_package_structs.md#struct-rawaddress)

异常：

- [SocketException](net_package_exceptions.md#class-socketexception) - 当前 [RawSocket](net_package_classes.md#class-rawsocket) 实例已经关闭，或无法获取对端地址时，抛出异常。