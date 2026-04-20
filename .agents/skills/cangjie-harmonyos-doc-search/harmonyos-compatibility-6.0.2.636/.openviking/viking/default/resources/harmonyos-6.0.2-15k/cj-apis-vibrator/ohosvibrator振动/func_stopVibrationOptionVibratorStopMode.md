## func stopVibration(Option\<VibratorStopMode>)

```cangjie
public func stopVibration(stopMode: Option<VibratorStopMode>): Unit
```

**功能：** 按照指定模式停止马达振动。

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|stopMode|[Option\<VibratorStopMode>](#enum-vibratorstopmode) |是|-|当stopMode是Some类型时，可以指定停止振动模式，支持两种：<br>VIBRATOR_STOP_MODE_TIME：停止固定时长振动；<br>VIBRATOR_STOP_MODE_PRESET：停止预置振动。当stopMode是None类型时，可以停止任何振动模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[振动错误码](../../errorcodes/cj-errorcode-vibrator.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.|
  |14600101|Device operation failed.|

**示例：**

停止固定时长振动：

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

let vibrateTime = VibrateTime("time", 1000)
let attribute = VibrateAttribute(ALARM, id: 0)
try {
    startVibration(vibrateTime, attribute)
} catch (e: Exception) {
    AppLog.error("test_startVibration_time :${e.message.toString()}")
}
try {
    // 按照VIBRATOR_STOP_MODE_TIME模式停止振动
    stopVibration(Some(VibratorStopMode.VIBRATOR_STOP_MODE_TIME))
} catch (e: Exception) {
    AppLog.error("test_stopVibration_time :${e.message.toString()}")
}
```

停止预置振动：

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

let vibratePreset = VibratePreset("preset", "haptic.clock.timer", count: 1)
let attribute = VibrateAttribute(ALARM, id: 0)
try {
    startVibration(vibratePreset, attribute)
} catch (e: Exception) {
    AppLog.error("test_startVibration_preset :${e.message.toString()}")
}
try {
    // 按照VIBRATOR_STOP_MODE_PRESET模式停止振动
    stopVibration(Some(VibratorStopMode.VIBRATOR_STOP_MODE_PRESET))
} catch (e: Exception) {
    AppLog.error("test_startVibration_preset :${e.message.toString()}")
}
```

停止任意种模式

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

let vibrateTime = VibrateTime("time", 1000)
let attribute = VibrateAttribute(ALARM, id: 0)
try {
    startVibration(vibrateTime, attribute)
} catch (e: Exception) {
    AppLog.error("test_startVibration_time :${e.message.toString()}")
}
try {
    stopVibration(Option<VibratorStopMode>.None)
} catch (e: Exception) {
    AppLog.error("test_stopVibration_time :${e.message.toString()}")
}
```