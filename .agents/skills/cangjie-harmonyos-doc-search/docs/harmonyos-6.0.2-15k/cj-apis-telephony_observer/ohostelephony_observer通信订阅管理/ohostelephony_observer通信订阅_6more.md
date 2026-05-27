# ohos.telephony_observer（通信订阅管理）

本模块提供订阅管理功能，可以订阅/取消订阅的事件包括：网络状态变化、信号状态变化、通话状态变化、蜂窝数据链路连接状态、蜂窝数据业务的上下行数据流状态、SIM状态变化。

## 导入模块

```cangjie
import kit.TelephonyKit.*
```

## 权限列表

ohos.permission.GET_NETWORK_INFO

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class CallStateInfo

```cangjie
public class CallStateInfo {
    public CallStateInfo(
        public let state: CallState,
        public let number: String
    )
}
```

**功能：** 通话状态相关信息。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

### let number

```cangjie
public let number: String
```

**功能：** 电话号码。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: CallState
```

**功能：** 通话类型。

**类型：** [CallState](cj-apis-telephony_call.md#enum-callstate)

**读写能力：** 只读

**起始版本：** 19

### CallStateInfo(CallState, String)

```cangjie
public CallStateInfo(
    public let state: CallState,
    public let number: String
)
```

**功能：** 构造CallStateInfo实例。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[CallState](cj-apis-telephony_call.md#enum-callstate)|是|-|通话类型。|
|number|String|是|-|电话号码。|

## class DataConnectionStateInfo

```cangjie
public class DataConnectionStateInfo {
    public DataConnectionStateInfo(
        public let state: DataConnectState,
        public let network: RadioTechnology
    )
}
```

**功能：** 数据连接状态相关信息。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

### let network

```cangjie
public let network: RadioTechnology
```

**功能：** 网络类型。

**类型：** [RadioTechnology](cj-apis-telephony_radio.md#enum-radiotechnology)

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: DataConnectState
```

**功能：** 数据连接状态。

**类型：** [DataConnectState](cj-apis-telephony_data.md#enum-dataconnectstate)

**读写能力：** 只读

**起始版本：** 19

### DataConnectionStateInfo(DataConnectState, RadioTechnology)

```cangjie
public DataConnectionStateInfo(
    public let state: DataConnectState,
    public let network: RadioTechnology
)
```

**功能：** 构造DataConnectionStateInfo实例。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[DataConnectState](cj-apis-telephony_data.md#enum-dataconnectstate)|是|-|数据连接状态。|
|network|[RadioTechnology](cj-apis-telephony_radio.md#enum-radiotechnology)|是|-|网络类型。|