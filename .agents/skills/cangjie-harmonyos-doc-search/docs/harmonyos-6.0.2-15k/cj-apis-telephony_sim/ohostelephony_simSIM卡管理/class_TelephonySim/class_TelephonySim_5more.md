## class TelephonySim

```cangjie
public class TelephonySim {}
```

**功能：** SIM卡管理类，提供各种静态方法用于获取SIM卡相关信息。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### static func getActiveSimAccountInfoList()

```cangjie
public static func getActiveSimAccountInfoList(): Array<IccAccountInfo>
```

**功能：** 获取激活SIM卡账户信息列表。

>**说明：**
>
> 仅需获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[IccAccountInfo](#class-iccaccountinfo)>|返回激活卡槽SIM卡的账户信息列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300004|Do not have sim card.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let infoList = TelephonySim.getActiveSimAccountInfoList()
```

### static func getCardType(Int32)

```cangjie
public static func getCardType(slotId: Int32): CardType
```

**功能：** 获取指定卡槽SIM卡的卡类型。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|[CardType](#enum-cardtype)|返回指定卡槽SIM卡的卡类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300004|Do not have sim card.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonySim.getCardType(0)
```

### static func getDefaultVoiceSimId()

```cangjie
public static func getDefaultVoiceSimId(): Int32
```

**功能：** 获取默认语音业务的SIM卡ID。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回默认语音业务的SIM卡ID。与SIM卡绑定，从1开始递增。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300004|Do not have sim card.|
  |8300999|Unknown error code.|
  |8301001|SIM card is not activated.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonySim.getDefaultVoiceSimId()
```

### static func getDefaultVoiceSlotId()

```cangjie
public static func getDefaultVoiceSlotId(): Int32
```

**功能：** 获取默认语音业务的卡槽ID。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32| 0：卡槽1 <br> 1：卡槽2 <br>-1：未设置或服务不可用|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonySim.getDefaultVoiceSlotId()
```