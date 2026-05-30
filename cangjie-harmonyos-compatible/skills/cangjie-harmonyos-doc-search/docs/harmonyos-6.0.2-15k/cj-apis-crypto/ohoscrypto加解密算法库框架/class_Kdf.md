## class Kdf

```cangjie
public class Kdf {}
```

**功能：** 密钥派生函数（key derivation function）类，使用密钥派生方法之前需要创建该类的实例进行操作，通过createKdf(algName: String): Kdf方法构造此实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 19

### prop algName

```cangjie
public prop algName: String
```

**功能：** 密钥派生函数的算法名称。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func generateSecret(KdfSpec)

```cangjie
public func generateSecret(params: KdfSpec): DataBlob
```

**功能：** 基于传入的密钥派生参数进行密钥派生。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|params|[KdfSpec](#interface-kdfspec)|是|-|设置密钥派生函数的参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[DataBlob](#struct-datablob)|用于获取派生得到的密钥DataBlob数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |17620001|memory error.|
  |17620002|runtime error.|
  |17630001|crypto operation error.|