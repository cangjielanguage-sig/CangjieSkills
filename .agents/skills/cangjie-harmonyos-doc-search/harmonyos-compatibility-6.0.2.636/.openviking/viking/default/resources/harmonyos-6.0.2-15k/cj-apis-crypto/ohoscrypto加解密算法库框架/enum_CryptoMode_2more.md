## enum CryptoMode

```cangjie
public enum CryptoMode <: Equatable<CryptoMode> & ToString {
    | ENCRYPT_MODE
    | DECRYPT_MODE
    | ...
}
```

**功能：** 表示加解密操作。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**父类型：**

- Equatable\<CryptoMode>
- ToString

### DECRYPT_MODE

```cangjie
DECRYPT_MODE
```

**功能：** 表示进行解密操作。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### ENCRYPT_MODE

```cangjie
ENCRYPT_MODE
```

**功能：** 表示进行加密操作。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### func !=(CryptoMode)

```cangjie
public operator func !=(other: CryptoMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CryptoMode](#enum-cryptomode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CryptoMode)

```cangjie
public operator func ==(other: CryptoMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CryptoMode](#enum-cryptomode)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|

## enum Result

```cangjie
public enum Result <: ToString {
    | INVALID_PARAMS
    | NOT_SUPPORT
    | ERR_OUT_OF_MEMORY
    | ERR_RUNTIME_ERROR
    | ERR_CRYPTO_OPERATION
    | ...
}
```

**功能：** 表示执行结果。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**父类型：**

- ToString

### ERR_CRYPTO_OPERATION

```cangjie
ERR_CRYPTO_OPERATION
```

**功能：** 调用三方算法库API出错。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### ERR_OUT_OF_MEMORY

```cangjie
ERR_OUT_OF_MEMORY
```

**功能：** 内存错误。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### ERR_RUNTIME_ERROR

```cangjie
ERR_RUNTIME_ERROR
```

**功能：** 运行时外部错误。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### INVALID_PARAMS

```cangjie
INVALID_PARAMS
```

**功能：** 非法入参。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### NOT_SUPPORT

```cangjie
NOT_SUPPORT
```

**功能：** 操作不支持。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|枚举的值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|