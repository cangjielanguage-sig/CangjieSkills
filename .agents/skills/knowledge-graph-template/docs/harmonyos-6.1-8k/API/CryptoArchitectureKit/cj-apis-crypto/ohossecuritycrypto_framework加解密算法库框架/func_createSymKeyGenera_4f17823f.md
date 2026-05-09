## func createSymKeyGenerator(String)

```cangjie
public func createSymKeyGenerator(algName: String): SymKeyGenerator
```

**功能：** 通过指定算法名称获取相应的对称密钥生成器实例。

支持的规格详见[对称密钥生成和转换规格](../../security/CryptoArchitectureKit/cj-crypto-sym-key-generation-conversion-spec.md)。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|algName|String|是|-|待生成对称密钥生成器的算法名称。具体取值详见[对称密钥生成和转换规格](../../security/CryptoArchitectureKit/cj-crypto-sym-key-generation-conversion-spec.md)一节中的“字符串参数”。|

**返回值：**

|类型|说明|
|:----|:----|
|[SymKeyGenerator](#class-symkeygenerator)|返回对称密钥生成器的对象。|

**异常：**

- BusinessException：对应错误码如下表，请参见[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | this operation is not supported. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let symKeyGenerator = createSymKeyGenerator("3DES192")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```