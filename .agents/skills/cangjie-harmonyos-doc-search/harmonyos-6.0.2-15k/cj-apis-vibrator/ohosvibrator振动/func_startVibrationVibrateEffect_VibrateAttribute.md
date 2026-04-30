## func startVibration(VibrateEffect, VibrateAttribute)

```cangjie
public func startVibration(effect: VibrateEffect, attribute: VibrateAttribute): Unit
```

**功能：** 根据指定的振动效果和振动属性触发马达振动。

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|effect|[VibrateEffect](#interface-vibrateeffect)|是|-|马达振动效果，支持三种：<br>1、[VibrateTime](#class-vibratetime)：按照指定持续时间触发马达振动；<br>2、[VibratePreset](#class-vibratepreset)：按照预置振动效果触发马达振动；<br>3、[VibrateFromFile](#class-vibratefromfile)：按照自定义振动配置文件触发马达振动。|
|attribute|[VibrateAttribute](#class-vibrateattribute)|是|-|马达振动属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[振动错误码](../../errorcodes/cj-errorcode-vibrator.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.|
  |801|Capability not supported.|
  |14600101|Device operation failed.|

**示例：**

按照指定持续时间触发马达振动：

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
    AppLog.error("test_startVibration :${e.message.toString()}")
}
```

按照预置振动效果触发马达振动：

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
```

按照自定义振动配置文件触发马达振动：

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.SensorServiceKit.*

let resourceManager = Global.getAbilityContext().resourceManager // 需获取Context应用上下文，详见本文使用说明
let rawfd = resourceManager.getRawFd("vib.json")
let vibrateFile = VibrateFromFile("file",
    HapticFileDescriptor(rawfd.fd, offSet: rawfd.offset, length: rawfd.length))
let attribute = VibrateAttribute(ALARM, id: 0)
try {
    startVibration(vibrateFile, attribute)
} catch (e: Exception) {
    AppLog.error("test_startVibration_time :${e.message.toString()}")
}
resourceManager.closeRawFd("vib.json")
```

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.CoreFileKit.*
import ohos.base.*

let file = FileFs.open("/data/storage/el2/base/haps/entry/files/vib.json")
let vibrateFile = VibrateFromFile("file", HapticFileDescriptor(file.fd))
let attribute = VibrateAttribute(ALARM, id: 0)
try {
    startVibration(vibrateFile, attribute)
} catch (e: Exception) {
    AppLog.error("test_startVibration_VibrateFromFile :${e.message.toString()}")
}
FileFs.close(file)
```