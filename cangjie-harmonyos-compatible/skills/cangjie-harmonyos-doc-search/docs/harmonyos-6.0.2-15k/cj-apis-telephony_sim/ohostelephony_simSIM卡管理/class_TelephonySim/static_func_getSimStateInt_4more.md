### static func getSimState(Int32)

```cangjie
public static func getSimState(slotId: Int32): SimState
```

**功能：** 获取指定卡槽的SIM卡状态。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|[SimState](#enum-simstate)|返回获取指定卡槽的SIM卡状态。|

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

let ret = TelephonySim.getSimState(0)
```

### static func hasOperatorPrivileges(Int32)

```cangjie
public static func hasOperatorPrivileges(slotId: Int32): Bool
```

**功能：** 检查应用（调用者）是否已被授予运营商权限。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回检查应用（调用者）是否已被授予运营商权限。|

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

let ret = TelephonySim.hasOperatorPrivileges(0)
```

### static func hasSimCard(Int32)

```cangjie
public static func hasSimCard(slotId: Int32): Bool
```

**功能：** 获取指定卡槽SIM卡是否插卡。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回指定卡槽是否插卡，如果插卡返回true。|

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

let ret = TelephonySim.hasSimCard(0)
```

### static func isSimActive(Int32)

```cangjie
public static func isSimActive(slotId: Int32): Bool
```

**功能：** 获取指定卡槽SIM卡是否激活。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|是|-|卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回指定卡槽是否激活，如果激活返回true。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |8300001|Invalid parameter value.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let ret = TelephonySim.isSimActive(0)s
```