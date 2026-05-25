## struct PaddingMode

```cangjie
public struct PaddingMode <: Equatable<PaddingMode> {
    public static let NoPadding: PaddingMode
    public static let PKCS7Padding: PaddingMode
    public let paddingType: Int64
}
```

功能：对称加解密算法的填充模式。

父类型：

- Equatable\<[PaddingMode](#struct-paddingmode)>

### static let NoPadding

```cangjie
public static let NoPadding: PaddingMode
```

功能：不填充，NoPadding 初始值是 [PaddingMode](crypto_package_structs.md#struct-paddingmode)(0)。

类型：[PaddingMode](crypto_package_structs.md#struct-paddingmode)

### static let PKCS7Padding

```cangjie
public static let PKCS7Padding: PaddingMode
```

功能：采用 PKCS7 协议填充，PKCS7Padding 初始值是 [PaddingMode](crypto_package_structs.md#struct-paddingmode)(1)。

类型：[PaddingMode](crypto_package_structs.md#struct-paddingmode)

### let paddingType

```cangjie
public let paddingType: Int64
```

功能：分组加解密填充方式，目前支持非填充和 pkcs7 填充。

类型：Int64

### func ==(PaddingMode)

```cangjie
public override operator func ==(other: PaddingMode): Bool
```

功能：填充模式比较是否相同。

参数：

- other: [PaddingMode](crypto_package_structs.md#struct-paddingmode) - 填充模式。

返回值：

- Bool - true 相同，false 不相同。

### func !=(PaddingMode)

```cangjie
public override operator func !=(other: PaddingMode): Bool
```

功能：工作模式比较是否不相同。

参数：

- other: [PaddingMode](crypto_package_structs.md#struct-paddingmode)  - 填充模式。

返回值：

- Bool - true 不相同，false 相同。