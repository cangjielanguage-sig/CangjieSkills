## class TlsSessionContext

```cangjie
public class TlsSessionContext <: Equatable<TlsSessionContext> & ToString

```

功能：该类表示 TLS 会话上下文，给客户端提供信息，确保客户端所连接的服务端仍为相同实例，用于连接复用时，验证客户端合法性。

> **说明：**
>
> 当客户端尝试恢复会话时，双方都必须确保他们正在恢复与合法对端的会话。

父类型：

- Equatable\<[TlsSessionContext](#class-tlssessioncontext)>
- ToString

### static func fromName(String)

```cangjie
public static func fromName(name: String): TlsSessionContext
```

功能：通过名称创建 [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) 实例。

通过 [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) 保存的名称获取 [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) 对象。该名称用于区分 TLS 服务器，因此客户端依赖此名称来避免意外，尝试恢复与错误的服务器的连接。这里不一定使用加密安全名称，因为底层实现可以完成这项工作。从此函数返回的具有相同名称的两个 TlsSessionContext 可能不相等，并且不保证可替换。尽管它们是从相同的名称创建的，因此服务器实例应该在整个生命周期内创建一个 TlsSessionContext ，并且在每次 [TlsSocket](tls_package_classes.md#class-tlssocket).server() 调用中使用它。

参数：

- name: String - 会话上下文名称。

返回值：

- [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) - 会话上下文。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成会话上下文名称字符串。

返回值：

- String - [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext)（会话上下文名称字符串）。

### operator func !=(TlsSessionContext)

```cangjie
public override operator func !=(other: TlsSessionContext): Bool
```

功能：判断两 [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) 实例名称是否不同。

参数：

- other: [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) - 被比较的会话上下文对象。

返回值：

- Bool - 若 [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) 对象不同，返回 `true`；否则，返回 `false`。

### operator func ==(TlsSessionContext)

```cangjie
public override operator func ==(other: TlsSessionContext): Bool
```

功能：判断两 [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) 实例名称是否相同。

参数：

- other: [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) - 被比较的会话上下文对象。

返回值：

- Bool - 若 [TlsSessionContext](tls_package_classes.md#class-tlssessioncontext) 对象相同，返回 `true`；否则，返回 `false`。