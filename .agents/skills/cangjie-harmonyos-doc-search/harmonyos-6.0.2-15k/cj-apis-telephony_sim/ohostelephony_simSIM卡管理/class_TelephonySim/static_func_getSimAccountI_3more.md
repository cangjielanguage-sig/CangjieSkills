### static func getSimAccountInfo(Int32)

```cangjie
public static func getSimAccountInfo(slotId: Int32): IccAccountInfo
```

**功能：** 获取SIM卡账户信息。

>**说明：**
> 仅需获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|[IccAccountInfo](#class-iccaccountinfo)|返回指定卡槽SIM卡的账户信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300004|Do not have sim card.|
  |8300999|Unknown error code.|
  |8301002|SIM card operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonySim.getSimAccountInfo(0)
```

### static func getSimOperatorNumeric(Int32)

```cangjie
public static func getSimOperatorNumeric(slotId: Int32): String
```

**功能：** 获取指定卡槽SIM卡的归属PLMN（Public Land Mobile Network）号。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回获取指定卡槽SIM卡的归属PLMN号。|

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

let ret = TelephonySim.getSimOperatorNumeric(0)
```

### static func getSimSpn(Int32)

```cangjie
public static func getSimSpn(slotId: Int32): String
```

**功能：** 获取指定卡槽SIM卡的服务提供商名称（Service Provider Name，SPN）。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回获取指定卡槽SIM卡的SPN。|

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

let ret = TelephonySim.getSimSpn(0)
```