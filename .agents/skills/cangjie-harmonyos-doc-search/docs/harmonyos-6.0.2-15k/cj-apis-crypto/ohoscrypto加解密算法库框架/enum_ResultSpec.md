## enum ResultSpec

```cangjie
public enum ResultSpec <: ToString {
    | BIGINT(BigInt)
    | NUMBER(Int32)
    | STRING(String)
    | UINT8ARR(Array<UInt8>)
    | ...
}
```

**功能：** 表示返回值。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- ToString

### BIGINT(BigInt)

```cangjie
BIGINT(BigInt)
```

**功能：** 封装BigInt类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### NUMBER(Int32)

```cangjie
NUMBER(Int32)
```

**功能：** 封装Int32类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 封装String类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### UINT8ARR(Array\<UInt8>)

```cangjie
UINT8ARR(Array<UInt8>)
```

**功能：** 封装Array\<UInt8>类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 打印枚举值。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回枚举值类型的字符串。|