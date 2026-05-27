## class TelephonyData

```cangjie
public class TelephonyData {}
```

**功能：** 蜂窝数据类，提供各种静态方法如[TelephonyData.getDefaultCellularDataSlotId()](#static-func-getdefaultcellulardataslotid)以获取移动数据SIM卡各种状态信息。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

### static func getCellularDataFlowType()

```cangjie
public static func getCellularDataFlowType(): DataFlowType
```

**功能：** 获取蜂窝数据业务的上下行状态。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataFlowType](#enum-dataflowtype)|返回获取蜂窝数据业务的上下行状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result = TelephonyData.getCellularDataFlowType()
```

### static func getCellularDataState()

```cangjie
public static func getCellularDataState(): DataConnectState
```

**功能：** 获取分组交换域(PS域)的连接状态。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DataConnectState](#enum-dataconnectstate)|返回获取PS域的连接状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result = TelephonyData.getCellularDataState()
```

### static func getDefaultCellularDataSimId()

```cangjie
public static func getDefaultCellularDataSimId(): Int32
```

**功能：** 获取默认移动数据的SIM卡ID。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|获取默认移动数据的SIM卡ID。<br>与SIM卡绑定，从1开始递增。<br>注意：若无数据卡，则默认是0。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result = TelephonyData.getDefaultCellularDataSimId()
```

### static func getDefaultCellularDataSlotId()

```cangjie
public static func getDefaultCellularDataSlotId(): Int32
```

**功能：** 获取默认移动数据的SIM卡。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回获取默认移动数据的SIM卡。<br>0：卡槽1。<br>1：卡槽2。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result = TelephonyData.getDefaultCellularDataSlotId()
```

### static func isCellularDataEnabled()

```cangjie
public static func isCellularDataEnabled(): Bool
```

**功能：** 检查蜂窝数据业务是否启用。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回检查蜂窝数据业务是否启用。<br>true：蜂窝数据业务已启用。<br>false：蜂窝数据业务已禁用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

try {
    let result1 = TelephonyData.isCellularDataEnabled()
    AppLog.info("isCellularDataEnabled : ${result1}")
} catch (e: Exception) {
    AppLog.info("Exception: ${e.toString()}")
}
```