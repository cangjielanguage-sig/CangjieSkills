## enum AsyKeySpecType

```cangjie
public enum AsyKeySpecType <: Equatable<AsyKeySpecType> & ToString {
    | COMMON_PARAMS_SPEC
    | PRIVATE_KEY_SPEC
    | PUBLIC_KEY_SPEC
    | KEY_PAIR_SPEC
    | ...
}
```

**功能：** 表示密钥参数类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- Equatable\<AsyKeySpecType>
- ToString

### COMMON_PARAMS_SPEC

```cangjie
COMMON_PARAMS_SPEC
```

**功能：** 表示公私钥中包含的公共参数。使用此类型的参数可以调用[generateKeyPair](#func-generatekeypair-1)随机生成密钥对。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### KEY_PAIR_SPEC

```cangjie
KEY_PAIR_SPEC
```

**功能：** 表示公私钥中包含的全量参数。使用此类型的参数可以调用[generateKeyPair](#func-generatekeypair-1)生成指定的密钥对。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### PRIVATE_KEY_SPEC

```cangjie
PRIVATE_KEY_SPEC
```

**功能：** 表示私钥中包含的参数。使用此类型的参数可以调用[generatePriKey](#func-generateprikey)生成指定的私钥。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### PUBLIC_KEY_SPEC

```cangjie
PUBLIC_KEY_SPEC
```

**功能：** 表示公钥中包含的参数。使用此类型的参数可以调用[generatePubKey](#func-generatepubkey)生成指定的公钥。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### func !=(AsyKeySpecType)

```cangjie
public operator func !=(other: AsyKeySpecType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AsyKeySpecType](#enum-asykeyspectype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(AsyKeySpecType)

```cangjie
public operator func ==(other: AsyKeySpecType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AsyKeySpecType](#enum-asykeyspectype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|