## enum CryptoMode

```cangjie
public enum CryptoMode <: Equatable<CryptoMode> & ToString {
    | EncryptMode
    | DecryptMode
    | ...
}
```

**功能：** 表示加解密操作的枚举。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**父类型：**

- Equatable\<CryptoMode>
- ToString

### DecryptMode

```cangjie
DecryptMode
```

**功能：** 表示进行解密操作。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### EncryptMode

```cangjie
EncryptMode
```

**功能：** 表示进行加密操作。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### func !=(CryptoMode)

```cangjie
public operator func !=(other: CryptoMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

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

**起始版本：** 22

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|