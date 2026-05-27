### func read(Array\<Byte>)

```cangjie
public override func read(buffer: Array<Byte>): Int64
```

功能：[TlsSocket](tls_package_classes.md#class-tlssocket) 读取数据。

参数：

- buffer: Array\<Byte> - 存储读取到的数据内容的数组。

返回值：

- Int64 - 读取到的数据内容字节数。

异常：

- SocketException - 本端建连的底层 TCP 套接字关闭，抛出异常。
- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当 `buffer` 为空，或者 [TlsSocket](tls_package_classes.md#class-tlssocket) 未连接，或读取数据出现系统错误等。

### func toString()

```cangjie
public func toString(): String
```

功能：套接字的字符串表示，字符串内容为当前套接字状态。

> **说明：**
>
> 例如：当前套接字处于可开始进行握手状态时，该接口将返回字符串 "[TlsSocket](tls_package_classes.md#class-tlssocket)(TcpSocket(\${本端地址} -> \${对端地址}), ready for handshake)"

返回值：

- String - 该 TLS 连接字符串。

### func write(Array\<Byte>)

```cangjie
public func write(buffer: Array<Byte>): Unit
```

功能：[TlsSocket](tls_package_classes.md#class-tlssocket) 发送数据。

参数：

- buffer: Array\<Byte> - 存储将要发送的数据内容数组。

异常：

- SocketException - 本端建连的底层 TCP 套接字关闭，抛出异常。
- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字已关闭，或者 [TlsSocket](tls_package_classes.md#class-tlssocket) 未连接，或写入数据出现系统错误等。

### operator func !=(TlsSocket)

```cangjie
public override operator func !=(other: TlsSocket): Bool
```

功能：判断两 [TlsSocket](tls_package_classes.md#class-tlssocket) 是否引用不同实例。

参数：

- other: [TlsSocket](tls_package_classes.md#class-tlssocket) - 对比的 TLS 套接字。

返回值：

- Bool - 对比的套接字不同返回 `true`；否则，返回 `false`。

### operator func ==(TlsSocket)

```cangjie
public override operator func ==(other: TlsSocket): Bool
```

功能：判断两 [TlsSocket](tls_package_classes.md#class-tlssocket) 是否引用同一实例。

参数：

- other: [TlsSocket](tls_package_classes.md#class-tlssocket) - 对比的 TLS 套接字。

返回值：

- Bool - 对比的套接字相同返回 `true`；否则，返回 `false`。