## struct CcmParamsSpec

```cangjie
public struct CcmParamsSpec <: ParamsSpec {
    public init(algName: String, iv: DataBlob, add: DataBlob, authTag: DataBlob)
}
```

**功能：** 加解密参数[ParamsSpec](#interface-paramsspec)的子类，用于在对称加解密时作为[init()](#func-initcryptomode-key-paramsspec)方法的参数。

适用于CCM模式。

> **说明：**
>
> 传入[init()](#func-initcryptomode-key-paramsspec)方法前需要指定其algName属性（来源于父类[ParamsSpec](#interface-paramsspec)）。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**父类型：**

- [ParamsSpec](#interface-paramsspec)

### prop aad

```cangjie
public mut prop aad: DataBlob
```

**功能：** 指明加解密参数aad，长度为8字节。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [DataBlob](#struct-datablob)

**读写能力：** 可读写

**起始版本：** 12

### prop authTag

```cangjie
public mut prop authTag: DataBlob
```

**功能：** 指明加解密参数authTag，长度为12字节。<br/>采用CCM模式加密时，需要获取[doFinal()](#func-dofinaldatablob)输出的[DataBlob](#struct-datablob)，取出其末尾12字节作为解密时[init()](#func-initcryptomode-key-paramsspec)方法的入参[CcmParamsSpec](#struct-ccmparamsspec)中的authTag。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [DataBlob](#struct-datablob)

**读写能力：** 可读写

**起始版本：** 12

### prop iv

```cangjie
public mut prop iv: DataBlob
```

**功能：** 指明加解密参数iv，长度为7字节。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** [DataBlob](#struct-datablob)

**读写能力：** 可读写

**起始版本：** 12

### init(String, DataBlob, DataBlob, DataBlob)

```cangjie
public init(algName: String, iv: DataBlob, add: DataBlob, authTag: DataBlob)
```

**功能：** 创建CcmParamsSpec实例。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|指明对称加解密参数的算法模式。可选值如下:<br/> - IvParamsSpec: 适用于CBCMagIc_StrINgCTRMagIc_StrINgOFBMagIc_StrINgCFB模式。<br/> - GcmParamsSpec: 适用于GCM模式。<br/> - CcmParamsSpec: 适用于CCM模式。|
|iv|[DataBlob](#struct-datablob)|是|-|指明加解密参数iv，长度为7字节。|
|add|[DataBlob](#struct-datablob)|是|-|指明加解密参数aad，长度为8字节。|
|authTag|[DataBlob](#struct-datablob)|是|-|指明加解密参数authTag，长度为12字节。采用CCM模式加密时，需要获取doFinal()或doFinalSync()输出的DataBlob，取出其末尾12字节作为解密时init()或initSync()方法的入参CcmParamsSpec中的authTag。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let ccm = GcmParamsSpec("CcmParamsSpec", DataBlob(Array<UInt8>(7, repeat: 1)), DataBlob(Array<UInt8>(8, repeat: 1)),
    DataBlob(Array<UInt8>(12, repeat: 1)))
```