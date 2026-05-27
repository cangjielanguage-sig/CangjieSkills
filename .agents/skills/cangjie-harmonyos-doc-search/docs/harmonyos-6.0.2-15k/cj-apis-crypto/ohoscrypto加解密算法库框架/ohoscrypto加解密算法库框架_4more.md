# ohos.crypto（加解密算法库框架）

为屏蔽底层硬件和算法库，向上提供统一的密码算法库加解密相关接口。

## 导入模块

```cangjie
import kit.CryptoArchitectureKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createAsyKeyGenerator(String)

```cangjie
public func createAsyKeyGenerator(algName: String): AsyKeyGenerator
```

**功能：** 通过指定算法名称的字符串，获取相应的非对称密钥生成器实例。

支持的规格详见[非对称密钥生成和转换规格](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-asym-key-generation-conversion-spec.md)。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|[非对称密钥生成支持的算法名](../../../../Dev_Guide/security/CryptoArchitectureKit/cj-crypto-asym-key-generation-conversion-spec.md)。|

**返回值：**

|类型|说明|
|:----|:----|
|[AsyKeyGenerator](#class-asykeygenerator)|返回非对称密钥生成器的对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[crypto framework错误码](../../errorcodes/cj-errorcode-crypto.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|invalid parameters. Possible causes: <br>1. Mandatory parameters are left unspecified;<br>2. Incorrect parameter types;<br>3. Parameter verification failed.|
  |801|this operation is not supported.|
  |17620001|memory error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let asyKeyGenerator = createAsyKeyGenerator('ECC256')
```