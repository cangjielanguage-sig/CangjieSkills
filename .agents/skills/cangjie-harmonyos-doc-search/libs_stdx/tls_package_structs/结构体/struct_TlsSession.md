## struct TlsSession

```cangjie
public struct TlsSession <: Equatable<TlsSession> & ToString & Hashable
```

功能：此结构体表示已建立的客户端会话。此结构体实例用户不可创建，其内部结构对用户不可见。

当客户端 TLS 握手成功后，将会生成一个会话，当连接因一些原因丢失后，客户端可以通过这个会话 id 复用此次会话，省略握手流程。

父类型：

- Equatable\<[TlsSession](#struct-tlssession)>
- ToString
- Hashable

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：生成会话 id 的哈希值。

返回值：

- Int64 - 会话 id 的哈希值。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成会话 id 的字符串。

返回值：

- String - [TlsSession](tls_package_structs.md#struct-tlssession)（会话 id 字符串）。

### operator func !=(TlsSession)

```cangjie
public override operator func !=(other: TlsSession): Bool
```

功能：判断会话 id 是否不同。

参数：

- other: [TlsSession](tls_package_structs.md#struct-tlssession) - 待比较的会话对象。

返回值：

- Bool - 若会话 id 不同，则返回 `true`，否则返回 `false`。

### operator func ==(TlsSession)

```cangjie
public override operator func ==(other: TlsSession): Bool
```

功能：判断会话 id 是否相同。

参数：

- other: [TlsSession](tls_package_structs.md#struct-tlssession) - 待比较的会话对象。

返回值：

- Bool - 若会话 id 相同，则返回 `true`，否则返回 `false`。