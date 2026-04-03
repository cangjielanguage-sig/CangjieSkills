## struct CipherSuite

```cangjie
public struct CipherSuite <: ToString & Equatable<CipherSuite>
```

功能：TLS 中的密码套件。

父类型：

- ToString
- Equatable\<[CipherSuite](#struct-ciphersuite)>

### static prop allSupported

```cangjie
public static prop allSupported: Array<CipherSuite>
```

功能：返回所有支持的密码套件。

返回值：存放密码套件的数组。

类型：Array\<[CipherSuite](tls_package_structs.md#struct-ciphersuite)>

### func toString()

```cangjie
public func toString(): String
```

功能：返回密码套件名称。

返回值：

- String - 密码套件名称。

### operator func !=(CipherSuite)

```cangjie
public operator func !=(that: CipherSuite): Bool
```

功能：判断两个密码套件是否不等。

参数：

- that: [CipherSuite](tls_package_structs.md#struct-ciphersuite) - 被比较的密码套件对象。

返回值：

- Bool - 若不等，则返回 `true`；反之，返回 `false`。

### operator func ==(CipherSuite)

```cangjie
public operator func ==(that: CipherSuite): Bool
```

功能：判断两个密码套件是否相等。

参数：

- that: [CipherSuite](tls_package_structs.md#struct-ciphersuite) - 被比较的密码套件对象。

返回值：

- Bool - 若相等，则返回 `true`；反之，返回 `false`。