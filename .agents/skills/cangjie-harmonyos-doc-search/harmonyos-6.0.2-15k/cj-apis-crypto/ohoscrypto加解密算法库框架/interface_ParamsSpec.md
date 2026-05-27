## interface ParamsSpec

```cangjie
public interface ParamsSpec {
    mut prop algName: String
    mut prop iv: DataBlob
}
```

**功能：** 加解密参数，在进行对称加解密时需要构造其子类对象，并将子类对象传入[init()](#func-initcryptomode-key-paramsspec)方法。

适用于需要iv等参数的对称加解密模式（对于无iv等参数的模式如ECB模式，无需构造，在[init()](#func-initcryptomode-key-paramsspec)中传入None即可）。

> **说明：**
>
> 由于[init()](#func-initcryptomode-key-paramsspec)的params参数是ParamsSpec类型（父类），而实际需要传入具体的子类对象（如IvParamsSpec），因此在构造子类对象时应设置其父类ParamsSpec的algName参数，使算法库在init()时知道传入的是哪种子类对象。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### prop algName

```cangjie
mut prop algName: String
```

**功能：** 指明对称加解密参数的算法模式。可选值如下:<br/> - IvParamsSpec: 适用于CBCMagIc_StrINgCTRMagIc_StrINgOFBMagIc_StrINgCFB模式。<br/> - GcmParamsSpec: 适用于GCM模式。<br/> - CcmParamsSpec: 适用于CCM模式。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### prop iv

```cangjie
mut prop iv: DataBlob
```

**功能：** 指明加解密参数iv。常见取值如下：<br/>- AES的CBCMagIc_StrINgCTRMagIc_StrINgOFBMagIc_StrINgCFB模式：iv长度为16字节<br/>- 3DES的CBCMagIc_StrINgOFBMagIc_StrINgCFB模式：iv长度为8字节<br/>- SM4的CBCMagIc_StrINgCTRMagIc_StrINgOFBMagIc_StrINgCFB模式：iv长度为16字节。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [DataBlob](#struct-datablob)

**读写能力：** 可读写

**起始版本：** 12