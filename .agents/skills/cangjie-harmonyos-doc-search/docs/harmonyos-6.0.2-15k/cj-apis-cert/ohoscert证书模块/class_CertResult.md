## class CertResult

```cangjie
public class CertResult {
    public static const SUCCESS = 0_i32
    public static const INVALID_PARAMS = 401_i32
    public static const NOT_SUPPORT = 801_i32
    public static const ERR_OUT_OF_MEMORY = 19020001_i32
    public static const ERR_RUNTIME_ERROR = 19020002_i32
    public static const ERR_CRYPTO_OPERATION = 19030001_i32
    public static const ERR_CERT_SIGNATURE_FAILURE = 19030002_i32
    public static const ERR_CERT_NOT_YET_VALID = 19030003_i32
    public static const ERR_CERT_HAS_EXPIRED = 19030004_i32
    public static const ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 19030005_i32
    public static const ERR_KEYUSAGE_NO_CERTSIGN = 19030006_i32
    public static const ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 19030007_i32
}
```

**功能：** 表示执行结果。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### static const ERR_CERT_HAS_EXPIRED

```cangjie
public static const ERR_CERT_HAS_EXPIRED = 19030004_i32
```

**功能：** 表示证书过期。

**类型：** Int32

**起始版本：** 19

### static const ERR_CERT_NOT_YET_VALID

```cangjie
public static const ERR_CERT_NOT_YET_VALID = 19030003_i32
```

**功能：** 表示证书尚未生效。

**类型：** Int32

**起始版本：** 19

### static const ERR_CERT_SIGNATURE_FAILURE

```cangjie
public static const ERR_CERT_SIGNATURE_FAILURE = 19030002_i32
```

**功能：** 表示证书签名验证错误。

**类型：** Int32

**起始版本：** 19

### static const ERR_CRYPTO_OPERATION

```cangjie
public static const ERR_CRYPTO_OPERATION = 19030001_i32
```

**功能：** 表示调用三方算法库API出错。

**类型：** Int32

**起始版本：** 19

### static const ERR_KEYUSAGE_NO_CERTSIGN

```cangjie
public static const ERR_KEYUSAGE_NO_CERTSIGN = 19030006_i32
```

**功能：** 表示证书的密钥用途不含证书签名。

**类型：** Int32

**起始版本：** 19

### static const ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE

```cangjie
public static const ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 19030007_i32
```

**功能：** 表示证书的密钥用途不含数字签名。

**类型：** Int32

**起始版本：** 19

### static const ERR_OUT_OF_MEMORY

```cangjie
public static const ERR_OUT_OF_MEMORY
```

**功能：** 表示内存错误。

**类型：** Int32

**起始版本：** 19

### static const ERR_RUNTIME_ERROR

```cangjie
public static const ERR_RUNTIME_ERROR = 19020002_i32
```

**功能：** 表示运行时外部错误。

**类型：** Int32

**起始版本：** 19

### static const ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY

```cangjie
public static const ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 19030005_i32
```

**功能：** 表示无法获取证书的颁发者。

**类型：** Int32

**起始版本：** 19

### static const INVALID_PARAMS

```cangjie
public static const INVALID_PARAMS = 401_i32
```

**功能：** 表示非法入参。

**类型：** Int32

**起始版本：** 19

### static const NOT_SUPPORT

```cangjie
public static const NOT_SUPPORT = 801_i32
```

**功能：** 表示操作不支持。

**类型：** Int32

**起始版本：** 19

### static const SUCCESS

```cangjie
public static const SUCCESS = 0_i32
```

**功能：** 表示执行成功。

**类型：** Int32

**起始版本：** 19