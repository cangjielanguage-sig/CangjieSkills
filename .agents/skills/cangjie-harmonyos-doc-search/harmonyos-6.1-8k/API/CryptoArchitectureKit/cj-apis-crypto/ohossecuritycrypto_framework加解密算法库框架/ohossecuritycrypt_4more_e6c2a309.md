# ohos.security.crypto_framework（加解密算法库框架）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

crypto_framework模块向上提供统一的密码算法库加解密相关接口，以屏蔽底层硬件和算法库。

## 导入模块

```cangjie
import kit.CryptoArchitectureKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func createCipher(String)

```cangjie
public func createCipher(transformation: String): Cipher
```

**功能：** 通过指定算法名称，获取相应的[Cipher](#class-cipher)实例。

支持的规格详见[对称密钥加解密算法规格](../../security/CryptoArchitectureKit/cj-crypto-sym-encrypt-decrypt-spec.md)和[非对称密钥加解密算法规格](../../security/CryptoArchitectureKit/cj-crypto-asym-encrypt-decrypt-spec.md)。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|transformation|String|是|-|待生成Cipher的算法名称（含密钥长度）、加密模式以及填充方法的组合。|

> **说明：**
>
> 1. 目前对称加解密中，PKCS5和PKCS7的实现相同，其padding长度和分组长度保持一致。在3DES中均按8字节填充，在AES中均按16字节填充。另有NoPadding表示不填充。
>
> 开发者需要自行了解密码学不同分组模式的差异，以便选择合适的参数规格。例如选择ECB和CBC模式时，建议启用填充，否则必须确保明文长度是分组大小的整数倍；选择其他模式时，可以不启用填充，此时密文长度和明文长度一致（即可能不是分组大小的整数倍）。
> 2. 使用RSA或SM2进行非对称加解密时，必须创建两个Cipher对象，分别进行加密和解密操作，不能对同一个Cipher对象进行加解密。对称加解密没有此要求，只要算法规格一致，可以对同一个Cipher对象进行加解密操作。

**返回值：**

|类型|说明|
|:----|:----|
|[Cipher](#class-cipher)|返回加解密生成器的对象。|

**异常：**

- BusinessException：对应错误码如下表，请参见[通用错误码](../cj-errorcode-universal.md)和[crypto framework错误码](./cj-errorcode-crypto.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | this operation is not supported. |
  | 17620001 | memory operation failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let cipherAlgName = "3DES192|ECB|PKCS7"
    let cipher = createCipher(cipherAlgName)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```