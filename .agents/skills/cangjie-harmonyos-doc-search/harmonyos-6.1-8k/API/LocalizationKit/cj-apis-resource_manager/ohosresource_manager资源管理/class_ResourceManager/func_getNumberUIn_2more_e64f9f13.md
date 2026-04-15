### func getNumber(UInt32)

```cangjie
public func getNumber(resId: UInt32): NumberValueType
```

**功能：** 获取指定资源ID对应的Int32数值或者Float32数值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resId|UInt32|是|-|资源ID。|

**返回值：**

|类型|说明|
|:----|:----|
|[NumberValueType](#enum-numbervaluetype)|资源ID值对应的数值。<br>Int32对应的是原数值，Float32不带单位时对应的是原数值，带"vp","fp"单位时对应的是px值，具体参考示例代码。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001001 | Invalid resource ID. |
  | 9001002 | No matching resource is found based on the resource ID. |
  | 9001006 | The resource is referenced cyclically. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.PerformanceAnalysisKit.*
import ohos.arkui.state_macro_manage.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let res = @r(app.integer.test)
    let number = resourceManager.getNumber(res.id)
    match (number) {
        case Int32Value(v) => Hilog.info(0, "test", v.toString(), "")
        case Float32Value(v) => Hilog.info(0, "test", v.toString(), "")
        case _ => throw IllegalArgumentException("The type is not supported.")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getNumberByName(String)

```cangjie
public func getNumberByName(resName: String): NumberValueType
```

**功能：** 获取指定资源名称对应的Int32数值或者Float32数值。

**系统能力：** SystemCapability.Global.ResourceManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resName|String|是|-|资源名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[NumberValueType](#enum-numbervaluetype)|资源名称对应的数值。<br>Int32对应的是原数值，Float32不带单位时对应的是原数值，带"vp","fp"单位时对应的是px值。|

**异常：**

- BusinessException：对应错误码如下表，详见[资源管理错误码](./cj-errorcode-resource-manager.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 9001003 | Invalid resource name. |
  | 9001004 | No matching resource is found based on the resource name. |
  | 9001006 | The resource is referenced cyclically. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.LocalizationKit.*
import kit.PerformanceAnalysisKit.*
import ohos.arkui.state_macro_manage.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let resourceManager = Global.abilityContext.resourceManager
    let number = resourceManager.getNumberByName("test")
    match (number) {
        case Int32Value(v) => Hilog.info(0, "test", v.toString(), "")
        case Float32Value(v) => Hilog.info(0, "test", v.toString(), "")
        case _ => throw IllegalArgumentException("The type is not supported.")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```