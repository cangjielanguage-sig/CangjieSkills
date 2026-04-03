### func removeResource(String)

```cangjie
public func removeResource(path: String): Unit
```

**功能：** 应用运行时移除指定的资源路径，还原被覆盖前的资源。

> **说明**
>
> rawfile和resfile目录不支持资源覆盖。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|资源路径。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001010 | Invalid overlay path. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let path = "/data/storage/el2/base/haps/entry/files/library-default-unsigned.hsp"
    resourceManager.removeResource(path)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```