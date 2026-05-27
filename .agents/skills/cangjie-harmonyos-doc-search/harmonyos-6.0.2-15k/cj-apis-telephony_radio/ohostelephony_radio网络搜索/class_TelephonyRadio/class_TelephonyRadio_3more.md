## class TelephonyRadio

```cangjie
public class TelephonyRadio {}
```

**功能：** 网络搜索类，提供各种静态方法用于获取网络搜索相关的信息。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### static func getISOCountryCodeForNetwork(Int32)

```cangjie
public static func getISOCountryCodeForNetwork(slotId: Int32): String
```

**功能：** 获取注册网络所在国家的ISO国家码。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回注册网络所在国家的ISO国家码，例如cn（中国）。如果设备没有注册任何网络，接口返回空字符串。|

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

let ret = TelephonyRadio.getISOCountryCodeForNetwork(0)
AppLog.info("TelephonyRadio.getISOCountryCodeForNetwork suceess: data->${ret}")
```

### static func getNetworkSelectionMode(Int32)

```cangjie
public static func getNetworkSelectionMode(slotId: Int32): NetworkSelectionMode
```

**功能：** 获取当前选网模式。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|[NetworkSelectionMode](#enum-networkselectionmode)|返回当前选网模式。|

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

let ret = TelephonyRadio.getNetworkSelectionMode(0)
AppLog.info("TelephonyRadio.getNetworkSelectionMode suceess: data->${ret.getValue()}")
```