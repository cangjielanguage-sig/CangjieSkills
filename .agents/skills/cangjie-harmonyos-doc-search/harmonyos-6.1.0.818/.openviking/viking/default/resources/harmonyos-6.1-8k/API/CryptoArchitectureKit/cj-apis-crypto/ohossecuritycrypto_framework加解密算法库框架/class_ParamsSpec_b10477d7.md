## class ParamsSpec

```cangjie
public open class ParamsSpec {
    public var algName: String
}
```

**功能：** 加解密参数，在进行对称加解密时需要构造其子类对象，并将子类对象传入[initialize()](#func-initializecryptomode-key-paramsspec)方法。

适用于需要iv等参数的对称加解密模式（对于无iv等参数的模式如ECB模式，无需构造，在[initialize()](#func-initializecryptomode-key-paramsspec)中传入None即可）。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

### var algName

```cangjie
public var algName: String
```

**功能：** 指明对称加解密参数的算法模式。可选值如下：

"IvParamsSpec"：适用于CBC\|CTR\|OFB\|CFB模式。

"GcmParamsSpec"：适用于GCM模式。

"CcmParamsSpec"：适用于CCM模式。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22