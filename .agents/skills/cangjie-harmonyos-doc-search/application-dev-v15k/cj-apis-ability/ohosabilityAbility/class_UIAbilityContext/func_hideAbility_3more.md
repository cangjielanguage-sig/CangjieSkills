### func hideAbility()

```cangjie
public func hideAbility(): Unit
```

**功能：** 隐藏当前Ability。仅在2in1和tablet设备上生效。仅支持在主线程调用。调用此接口前要求确保应用已添加至状态栏。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not support.|
  |16000050|Internal error.|
  |16000067|The StartOptions check failed.|

### func isTerminating()

```cangjie
public func isTerminating(): Bool
```

**功能：** 查询ability是否在terminating状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

| 类型                                                         | 说明                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Bool | true：ability当前处于terminating状态；false：不处于terminating状态。 |

### func moveAbilityToBackground()

```cangjie
public func moveAbilityToBackground(): Unit
```

**功能：** 将处于前台的UIAbility移动到后台。仅支持在主线程调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000011|The context does not exist.|
  |16000050|Internal error.|
  |16000061|Operation not supported.|
  |16000065|The API can be called only when the ability is running in the foreground.|
  |16000066|An ability cannot switch to the foreground or background in Wukong mode.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
uiAbilityContext.moveAbilityToBackground()
```