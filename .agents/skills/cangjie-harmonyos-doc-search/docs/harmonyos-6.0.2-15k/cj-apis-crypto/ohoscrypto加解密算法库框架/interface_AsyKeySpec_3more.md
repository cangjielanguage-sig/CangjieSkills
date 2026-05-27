## interface AsyKeySpec

```cangjie
public interface AsyKeySpec {
    mut prop algName: String
    mut prop specType: AsyKeySpecType
}
```

**功能：** 指定非对称密钥参数的基本接口，用于创建密钥生成器。在指定非对称密钥参数时需要构造其子类对象，并将子类对象传入[createAsyKeyGeneratorBySpec()](#func-createasykeygeneratorbyspecasykeyspec)方法创建密钥生成器。构造子类对象时，所有BigInt类型的密钥参数均采用大端写法，并使用正数。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop algName

```cangjie
mut prop algName: String
```

**功能：** 指定非对称密钥的算法名称，比如"RSA"、"DSA"、"ECC"、"SM2"、"Ed25519"、"X25519"、"DH"。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### prop specType

```cangjie
mut prop specType: AsyKeySpecType
```

**功能：** 指定密钥参数类型，用于区分公/私钥参数。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [AsyKeySpecType](#enum-asykeyspectype)

**读写能力：** 可读写

**起始版本：** 19

## interface ECField

```cangjie
public interface ECField {
    mut prop fieldType: String
}
```

**功能：** 指定椭圆曲线的域。当前只支持Fp域。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop fieldType

```cangjie
mut prop fieldType: String
```

**功能：** 指定椭圆曲线域的类型，当前只支持"Fp"。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

## interface KdfSpec

```cangjie
public interface KdfSpec {
    mut prop algName: String
}
```

**功能：** 密钥派生函数参数，使用密钥派生函数进行密钥派生时，需要构建其子类对象并作为输入。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop algName

```cangjie
mut prop algName: String
```

**功能：** 指明密钥派生函数的算法名，如"PBKDF2"。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 19