## struct IvParamsSpec

```cangjie
public struct IvParamsSpec <: ParamsSpec {
    public init(algName: String, iv: DataBlob)
}
```

**功能：** 加解密参数[ParamsSpec](#interface-paramsspec)的子类，用于在对称加解密时作为[init()](#func-initcryptomode-key-paramsspec)方法的参数。

适用于CBC、CTR、OFB、CFB这些仅使用iv作为参数的加解密模式。

> **说明：**
>
> 传入[init()](#func-initcryptomode-key-paramsspec)方法前需要指定其algName属性（来源于父类[ParamsSpec](#interface-paramsspec)）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**父类型：**

- [ParamsSpec](#interface-paramsspec)

### prop iv

```cangjie
public mut prop iv: DataBlob
```

**功能：** 指明加解密参数iv。常见取值如下：<br/>- AES的CBCMagIc_StrINgCTRMagIc_StrINgOFBMagIc_StrINgCFB模式：iv长度为16字节<br/>- 3DES的CBCMagIc_StrINgOFBMagIc_StrINgCFB模式：iv长度为8字节<br/>- SM4的CBCMagIc_StrINgCTRMagIc_StrINgOFBMagIc_StrINgCFB模式：iv长度为16字节。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [DataBlob](#struct-datablob)

**读写能力：** 可读写

**起始版本：** 12

### init(String, DataBlob)

```cangjie
public init(algName: String, iv: DataBlob)
```

**功能：** 创建IvParamsSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指明对称加解密参数的算法模式。可选值如下:<br/> - IvParamsSpec: 适用于CBCMagIc_StrINgCTRMagIc_StrINgOFBMagIc_StrINgCFB模式。<br/> - GcmParamsSpec: 适用于GCM模式。<br/> - CcmParamsSpec: 适用于CCM模式。|
|iv|[DataBlob](#struct-datablob)|是|-|指明加解密参数iv。常见取值如下：<br/>- AES的CBC\|CTR\|OFB\|CFB模式：iv长度为16字节<br/>- 3DES的CBC\|OFB\|CFB模式：iv长度为8字节<br/>- SM4的CBC\|CTR\|OFB\|CFB模式：iv长度为16字节。 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let iv = IvParamsSpec("IvParamsSpec", DataBlob(Array<UInt8>(8, repeat: 1)))
```