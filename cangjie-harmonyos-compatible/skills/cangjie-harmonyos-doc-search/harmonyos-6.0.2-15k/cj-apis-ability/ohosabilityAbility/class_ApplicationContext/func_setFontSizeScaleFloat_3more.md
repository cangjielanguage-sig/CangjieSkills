### func setFontSizeScale(Float64)

```cangjie
public func setFontSizeScale(fontSizeScale: Float64): Unit
```

**功能：** 设置应用字体大小缩放比例。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontSizeScale|Float64|是|-|表示字体缩放比例，取值为非负数。|

**异常：**

- IllegalArgumentException:

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |fontSizeScale must >= 0.0|传入参数小于0。|传入大于等于0的数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

try {
    let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
    let appctx = uiAbilityContext.getApplicationContext()
    appctx.setFontSizeScale(2.3)
} catch (e: IllegalArgumentException) {
    AppLog.error("setFontSizeScale failed")
}
```

### func setLanguage(String)

```cangjie
public func setLanguage(language: String): Unit
```

**功能：** 设置应用的语言。仅支持主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|language|String|是|-|设置语言。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000011|The context does not exist.|

### func setSupportedProcessCache(Bool)

```cangjie
public func setSupportedProcessCache(isSupported: Bool): Unit
```

**功能：** 应用设置自身是否支持缓存后快速启动。仅支持主线程调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isSupported|Bool|是|-|表示应用是否支持缓存后快速启动。true表示支持，false表示不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |401|Parameter error.|
  |16000011|The context does not exist.|
  |16000050|Internal error.|