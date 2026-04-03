## struct OperationMode

```cangjie
public struct OperationMode <: ToString & Equatable<OperationMode> {
    public static let ECB: OperationMode
    public static let CBC: OperationMode
    public static let OFB: OperationMode
    public static let CFB: OperationMode
    public static let CTR: OperationMode
    public static let GCM: OperationMode
    public let mode: String
}
```

功能：对称加解密算法的工作模式。

父类型：

- ToString
- Equatable\<[OperationMode](#struct-operationmode)>

### static let ECB

```cangjie
public static let ECB: OperationMode
```

功能：Electronic CodeBook（单子密码本）工作模式， ECB 初始值是 [OperationMode](crypto_package_structs.md#struct-operationmode)("ECB")。

类型：[OperationMode](crypto_package_structs.md#struct-operationmode)

### static let CBC

```cangjie
public static let CBC: OperationMode
```

功能：Cipher Block Chaining（密码分组链接）工作模式，CBC 初始值是 [OperationMode](crypto_package_structs.md#struct-operationmode)("CBC")。

类型：[OperationMode](crypto_package_structs.md#struct-operationmode)

### static let OFB

```cangjie
public static let OFB: OperationMode
```

功能：Output FeedBack（输出反馈）工作模式，OFB 初始值是 [OperationMode](crypto_package_structs.md#struct-operationmode)("OFB")。

类型：[OperationMode](crypto_package_structs.md#struct-operationmode)

### static let CFB

```cangjie
public static let CFB: OperationMode
```

功能：Cipher FeedBack（密文反馈）工作模式，CFB 初始值是 [OperationMode](crypto_package_structs.md#struct-operationmode)("CFB")。

类型：[OperationMode](crypto_package_structs.md#struct-operationmode)

### static let CTR

```cangjie
public static let CTR: OperationMode
```

功能：CounTeR（计数器）工作模式，CTR 初始值是 [OperationMode](crypto_package_structs.md#struct-operationmode)("CTR")。

类型：[OperationMode](crypto_package_structs.md#struct-operationmode)

### static let GCM

```cangjie
public static let GCM: OperationMode
```

功能：Galois Counter（伽罗瓦计数器）工作模式，GCM 初始值是 [OperationMode](crypto_package_structs.md#struct-operationmode)("GCM")。

类型：[OperationMode](crypto_package_structs.md#struct-operationmode)

### let mode

```cangjie
public let mode: String
```

功能：operation 分组加解密的工作模式，目前支持 ECB、CBC CFB OFB CTR GCM。

类型：String

### func toString()

```cangjie
public override func toString(): String
```

功能：获取工作模式字符串。

返回值：

- String - 工作模式字符串。

### func ==(OperationMode)

```cangjie
public override operator func ==(other: OperationMode): Bool
```

功能：工作模式比较是否相同。

参数：

- other: [OperationMode](crypto_package_structs.md#struct-operationmode) - 工作模式。

返回值：

- Bool - true 相同，false 不相同。

### func !=(OperationMode)

```cangjie
public override operator func !=(other: OperationMode): Bool
```

功能：工作模式比较是否不相同。

参数：

- other: [OperationMode](crypto_package_structs.md#struct-operationmode) - 工作模式。

返回值：

- Bool - true 不相同，false 相同。