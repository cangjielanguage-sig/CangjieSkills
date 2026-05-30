# ohos.vibrator（振动）

vibrator模块提供控制马达振动启停的能力。

## 导入模块

```cangjie
import kit.SensorServiceKit.*
```

## 权限列表

ohos.permission.VIBRATE

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func isHdHapticSupported()

```cangjie
public func isHdHapticSupported(): Bool
```

**功能：** 查询是否支持高清振动。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

let ret = isHdHapticSupported()
AppLog.info("the ret is ${ret}")
```

## func isSupportEffect(EffectId)

```cangjie
public func isSupportEffect(effectId: EffectId): Bool
```

**功能：** 查询是否支持预设的振动效果。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|effectId|[EffectId](#enum-effectid)|是|-|是否预设的振动效果。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回对象。当返回true则表示支持该effectId，否则不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[振动错误码](../../errorcodes/cj-errorcode-vibrator.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.|
  |14600101|Device operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

try {
    let ret = isSupportEffect(EFFECT_CLOCK_TIMER)
    AppLog.info("the ret is ${ret}")
} catch (e: Exception) {
    AppLog.error("test_isSupportEffect :${e.message.toString()}")
}
```