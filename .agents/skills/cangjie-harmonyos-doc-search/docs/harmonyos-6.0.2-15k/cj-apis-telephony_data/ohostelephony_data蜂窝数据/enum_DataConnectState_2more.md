## enum DataConnectState

```cangjie
public enum DataConnectState {
    | DATA_STATE_UNKNOWN
    | DATA_STATE_DISCONNECTED
    | DATA_STATE_CONNECTING
    | DATA_STATE_CONNECTED
    | DATA_STATE_SUSPENDED
    | ...
}
```

**功能：** 描述蜂窝数据链路连接状态。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

### DATA_STATE_CONNECTED

```cangjie
DATA_STATE_CONNECTED
```

**功能：** 表示蜂窝数据链路已连接。

**起始版本：** 19

### DATA_STATE_CONNECTING

```cangjie
DATA_STATE_CONNECTING
```

**功能：** 表示正在连接蜂窝数据链路。

**起始版本：** 19

### DATA_STATE_DISCONNECTED

```cangjie
DATA_STATE_DISCONNECTED
```

**功能：** 表示蜂窝数据链路断开。

**起始版本：** 19

### DATA_STATE_SUSPENDED

```cangjie
DATA_STATE_SUSPENDED
```

**功能：** 表示蜂窝数据链路被挂起。

**起始版本：** 19

### DATA_STATE_UNKNOWN

```cangjie
DATA_STATE_UNKNOWN
```

**功能：** 表示蜂窝数据链路未知。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举类型对应的数值。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|枚举类型对应的数值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let i = DataConnectState.DATA_STATE_CONNECTING.getValue()
```

## enum DataFlowType

```cangjie
public enum DataFlowType {
    | DATA_FLOW_TYPE_NONE
    | DATA_FLOW_TYPE_DOWN
    | DATA_FLOW_TYPE_UP
    | DATA_FLOW_TYPE_UP_DOWN
    | DATA_FLOW_TYPE_DORMANT
    | ...
}
```

**功能：** 描述蜂窝数据流类型。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

### DATA_FLOW_TYPE_DORMANT

```cangjie
DATA_FLOW_TYPE_DORMANT
```

**功能：** 表示没有上下行数据，底层链路处于休眠状态。

**起始版本：** 19

### DATA_FLOW_TYPE_DOWN

```cangjie
DATA_FLOW_TYPE_DOWN
```

**功能：** 表示只有下行数据。

**起始版本：** 19

### DATA_FLOW_TYPE_NONE

```cangjie
DATA_FLOW_TYPE_NONE
```

**功能：** 表示没有上行或下行数据。

**起始版本：** 19

### DATA_FLOW_TYPE_UP

```cangjie
DATA_FLOW_TYPE_UP
```

**功能：** 表示只有上行数据。

**起始版本：** 19

### DATA_FLOW_TYPE_UP_DOWN

```cangjie
DATA_FLOW_TYPE_UP_DOWN
```

**功能：** 表示有上下行数据。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举类型对应的数值。

**系统能力：** SystemCapability.Telephony.CellularData

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|枚举类型对应的数值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let i = DataFlowType.DATA_FLOW_TYPE_DORMANT.getValue()
```