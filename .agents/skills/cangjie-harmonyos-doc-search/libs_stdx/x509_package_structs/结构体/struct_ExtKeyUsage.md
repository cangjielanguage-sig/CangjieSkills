## struct ExtKeyUsage

```cangjie
public struct ExtKeyUsage <: ToString {
    public static let AnyKey: UInt16 = 0
    public static let ServerAuth: UInt16 = 1
    public static let ClientAuth: UInt16 = 2
    public static let EmailProtection: UInt16 = 3
    public static let CodeSigning: UInt16 = 4
    public static let OCSPSigning: UInt16 = 5
    public static let TimeStamping: UInt16 = 6
    public init(keys: Array<UInt16>)
}
```

功能：数字证书扩展字段中通常会包含携带扩展密钥用法说明，目前支持的用途有：ServerAuth、ClientAuth、EmailProtection、CodeSigning、OCSPSigning、TimeStamping。

父类型：

- ToString

### static let AnyKey

```cangjie
public static let AnyKey: UInt16 = 0
```

功能：表示应用于任意用途。

类型：UInt16

### static let ClientAuth

```cangjie
public static let ClientAuth: UInt16 = 2
```

功能：表示用于 SSL 的客户端验证。

类型：UInt16

### static let CodeSigning

```cangjie
public static let CodeSigning: UInt16 = 4
```

功能：表示用于代码签名。

类型：UInt16

### static let EmailProtection

```cangjie
public static let EmailProtection: UInt16 = 3
```

功能：表示用于电子邮件的加解密、签名等。

类型：UInt16

### static let OCSPSigning

```cangjie
public static let OCSPSigning: UInt16 = 5
```

功能：用于对 OCSP 响应包进行签名。

类型：UInt16

### static let ServerAuth

```cangjie
public static let ServerAuth: UInt16 = 1
```

功能：表示用于 SSL 的服务端验证。

类型：UInt16

### static let TimeStamping

```cangjie
public static let TimeStamping: UInt16 = 6
```

功能：用于将对象摘要值与时间绑定。

类型：UInt16

### init(Array\<UInt16>)

```cangjie
public init(keys: Array<UInt16>)
```

功能：构造指定用途的扩展密钥用法，需要注意同一个密钥可以有多种用途。

参数：

- keys: Array\<UInt16> - 密钥。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成扩展密钥用途字符串。

返回值：

- String - 证书扩展密钥用途字符串。