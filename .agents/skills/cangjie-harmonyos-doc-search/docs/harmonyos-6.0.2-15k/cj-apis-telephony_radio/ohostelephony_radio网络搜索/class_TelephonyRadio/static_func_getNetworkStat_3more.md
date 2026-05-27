### static func getNetworkState(Int32)

```cangjie
public static func getNetworkState(slotId!: Int32 = 0): NetworkState
```

**功能：** 获取网络状态。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|否|0| **命名参数。** 卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|[NetworkState](#class-networkstate)|返回网络状态。|

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

let ret = TelephonyRadio.getNetworkState()
AppLog.info("TelephonyRadio.getNetworkState suceess: longOperatorName->${ret.longOperatorName}, shortOperatorName->${ret.shortOperatorName}, plmnNumeric->${ret.plmnNumeric}")
```

### static func getOperatorName(Int32)

```cangjie
public static func getOperatorName(slotId: Int32): String
```

**功能：** 获取运营商名称。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回运营商名称，例如：中国移动。|

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

let ret = TelephonyRadio.getOperatorName(0)
AppLog.info("TelephonyRadio.getOperatorName suceess: data -> ${ret}")
```

### static func getPrimarySlotId()

```cangjie
public static func getPrimarySlotId(): Int32
```

**功能：** 获取主卡所在卡槽的索引号。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回获取设备主卡所在卡槽的索引号的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonyRadio.getPrimarySlotId()
AppLog.info("TelephonyRadio.getPrimarySlotId suceess: data->${ret}")
```