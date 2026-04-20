### static func getRadioTech(Int32)

```cangjie
public static func getRadioTech(slotId: Int32): NetworkRadioTech
```

**功能：** 获取当前接入的CS域和PS域无线接入技术。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|[NetworkRadioTech](#class-networkradiotech)|返回当前接入的CS域和PS域技术。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonyRadio.getRadioTech(0)
AppLog.info("TelephonyRadio.getRadioTech suceess: psRadioTech->${ret.psRadioTech.getValue()}, csRadioTech->${ret.csRadioTech.getValue()}")
```

### static func getSignalInformation(Int32)

```cangjie
public static func getSignalInformation(slotId: Int32): Array<SignalInformation>
```

**功能：** 获取指定SIM卡槽对应的注册网络信号强度信息列表。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[SignalInformation](#class-signalinformation)>|返回网络信号强度SignalInformation对象的数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonyRadio.getSignalInformation(0)
AppLog.info("TelephonyRadio.getSignalInformation suceess: size -> ${ret.size}")
for (obj in ret) {
    AppLog.info(
        "signalType: ${obj.signalType.getValue()}, signalLevel: ${obj.signalLevel}, dBm: ${obj.dBm}"
    )
}
```

### static func isNRSupported()

```cangjie
public static func isNRSupported(): Bool
```

**功能：** 判断当前设备是否支持NR(New Radio)。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|- true：支持<br>- false：不支持|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonyRadio.isNRSupported()
AppLog.info("TelephonyRadio.isNRSupported suceess: data -> ${ret}")
```