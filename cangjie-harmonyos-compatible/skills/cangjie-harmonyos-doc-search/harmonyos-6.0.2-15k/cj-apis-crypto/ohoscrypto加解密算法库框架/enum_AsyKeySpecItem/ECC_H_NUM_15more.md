### ECC_H_NUM

```cangjie
ECC_H_NUM
```

**功能：** ECC算法中的余因子h。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_N_BN

```cangjie
ECC_N_BN
```

**功能：** ECC算法中基点g的阶n。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_PK_X_BN

```cangjie
ECC_PK_X_BN
```

**功能：** ECC算法中，公钥pk（椭圆曲线上的一个点）的x坐标。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_PK_Y_BN

```cangjie
ECC_PK_Y_BN
```

**功能：** ECC算法中，公钥pk（椭圆曲线上的一个点）的y坐标。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_SK_BN

```cangjie
ECC_SK_BN
```

**功能：** ECC算法中的私钥sk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ED25519_PK_BN

```cangjie
ED25519_PK_BN
```

**功能：** ED25519算法中的公钥pk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ED25519_SK_BN

```cangjie
ED25519_SK_BN
```

**功能：** ED25519算法中的私钥sk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### RSA_N_BN

```cangjie
RSA_N_BN
```

**功能：** RSA算法中的模数n。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### RSA_PK_BN

```cangjie
RSA_PK_BN
```

**功能：** RSA算法中的公钥pk（即公钥指数e）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### RSA_SK_BN

```cangjie
RSA_SK_BN
```

**功能：** RSA算法中的私钥sk（即私钥指数d）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### X25519_PK_BN

```cangjie
X25519_PK_BN
```

**功能：** X25519算法中的公钥pk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### X25519_SK_BN

```cangjie
X25519_SK_BN
```

**功能：** X25519算法中的私钥sk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### func !=(AsyKeySpecItem)

```cangjie
public operator func !=(other: AsyKeySpecItem): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AsyKeySpecItem](#enum-asykeyspecitem)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(AsyKeySpecItem)

```cangjie
public operator func ==(other: AsyKeySpecItem): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AsyKeySpecItem](#enum-asykeyspecitem)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|