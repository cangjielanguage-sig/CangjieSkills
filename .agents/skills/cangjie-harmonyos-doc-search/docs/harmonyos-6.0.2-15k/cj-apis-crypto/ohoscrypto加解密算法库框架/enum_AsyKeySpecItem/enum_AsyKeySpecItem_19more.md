## enum AsyKeySpecItem

```cangjie
public enum AsyKeySpecItem <: Equatable<AsyKeySpecItem> & ToString {
    | DSA_P_BN
    | DSA_Q_BN
    | DSA_G_BN
    | DSA_SK_BN
    | DSA_PK_BN
    | ECC_FP_P_BN
    | ECC_A_BN
    | ECC_B_BN
    | ECC_G_X_BN
    | ECC_G_Y_BN
    | ECC_N_BN
    | ECC_H_NUM
    | ECC_SK_BN
    | ECC_PK_X_BN
    | ECC_PK_Y_BN
    | ECC_FIELD_TYPE_STR
    | ECC_FIELD_SIZE_NUM
    | ECC_CURVE_NAME_STR
    | RSA_N_BN
    | RSA_SK_BN
    | RSA_PK_BN
    | DH_P_BN
    | DH_G_BN
    | DH_L_NUM
    | DH_SK_BN
    | DH_PK_BN
    | ED25519_SK_BN
    | ED25519_PK_BN
    | X25519_SK_BN
    | X25519_PK_BN
    | ...
}
```

**功能：** 表示密钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

**父类型：**

- Equatable\<AsyKeySpecItem>
- ToString

### DH_G_BN

```cangjie
DH_G_BN
```

**功能：** DH算法中的参数g。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DH_L_NUM

```cangjie
DH_L_NUM
```

**功能：** DH算法中私钥长度，单位为bit。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DH_PK_BN

```cangjie
DH_PK_BN
```

**功能：** DH算法中的公钥pk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DH_P_BN

```cangjie
DH_P_BN
```

**功能：** DH算法中的素数p。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DH_SK_BN

```cangjie
DH_SK_BN
```

**功能：** DH算法中的私钥sk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DSA_G_BN

```cangjie
DSA_G_BN
```

**功能：** DSA算法的参数g。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DSA_PK_BN

```cangjie
DSA_PK_BN
```

**功能：** DSA算法的公钥pk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DSA_P_BN

```cangjie
DSA_P_BN
```

**功能：** DSA算法的素模数p。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DSA_Q_BN

```cangjie
DSA_Q_BN
```

**功能：** DSA算法中密钥参数q（p-1的素因子）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### DSA_SK_BN

```cangjie
DSA_SK_BN
```

**功能：** DSA算法的私钥sk。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_A_BN

```cangjie
ECC_A_BN
```

**功能：** ECC算法中椭圆曲线的第一个系数a。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_B_BN

```cangjie
ECC_B_BN
```

**功能：** ECC算法中椭圆曲线的第二个系数b。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_CURVE_NAME_STR

```cangjie
ECC_CURVE_NAME_STR
```

**功能：** ECC算法中的SECG(Standards for Efficient Cryptography Group)曲线名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_FIELD_SIZE_NUM

```cangjie
ECC_FIELD_SIZE_NUM
```

**功能：** ECC算法中域的大小，单位为bits（注：对于Fp域，域的大小为素数p的bits长度）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_FIELD_TYPE_STR

```cangjie
ECC_FIELD_TYPE_STR
```

**功能：** ECC算法中，椭圆曲线的域类型（当前只支持Fp域）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_FP_P_BN

```cangjie
ECC_FP_P_BN
```

**功能：** ECC算法中表示椭圆曲线Fp域的素数p。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_G_X_BN

```cangjie
ECC_G_X_BN
```

**功能：** ECC算法中基点g的x坐标。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### ECC_G_Y_BN

```cangjie
ECC_G_Y_BN
```

**功能：** ECC算法中基点g的y坐标。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19