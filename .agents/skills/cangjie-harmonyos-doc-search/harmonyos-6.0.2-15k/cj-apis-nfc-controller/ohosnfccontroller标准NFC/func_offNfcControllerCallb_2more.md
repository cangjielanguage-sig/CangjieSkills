## func off(NfcControllerCallbackType)

```cangjie
public func off(`type`: NfcControllerCallbackType): Unit
```

**功能：** 取消NFC开关状态事件关联的所有回调函数。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[NfcControllerCallbackType](#enum-nfccontrollercallbacktype)|是|要订阅的回调类型，固定填NfcStateChange。|

**示例：**

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*

class StateChangeCallback <: Callback1Argument<NfcState> {
    public func invoke(state: NfcState): Unit {
        AppLog.error("StateChangeCallback: ${toString(getNfcState())}")
    }
}

let cb = StateChangeCallback()
on(NfcControllerCallbackType.NfcStateChange, cb)
off(NfcControllerCallbackType.NfcStateChange)
```

## enum NfcState

```cangjie
public enum NfcState <: Equatable<NfcState> & ToString {
    | StateOff
    | StateTurningOn
    | StateOn
    | StateTurningOff
    | ...
}
```

**功能：** 定义不同的NFC状态值。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**父类型：**

- Equatable\<NfcState>
- ToString

### StateOff

```cangjie
StateOff
```

**功能：** NFC已关闭状态。

**起始版本：** 20

### StateOn

```cangjie
StateOn
```

**功能：** NFC已打开状态。

**起始版本：** 20

### StateTurningOff

```cangjie
StateTurningOff
```

**功能：** NFC正在关闭状态。

**起始版本：** 20

### StateTurningOn

```cangjie
StateTurningOn
```

**功能：** NFC正在打开状态。

**起始版本：** 20

### func !=(NfcState)

```cangjie
public operator func !=(other: NfcState): Bool
```

**功能：** 对NFC状态值进行判不等。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[NfcState](#enum-nfcstate)|是|NFC状态值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果NFC状态值不同，返回true，否则返回false。|

### func ==(NfcState)

```cangjie
public operator func ==(other: NfcState): Bool
```

**功能：** 对NFC状态值进行判等。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[NfcState](#enum-nfcstate)|是|NFC状态值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果NFC状态值相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回NFC状态值的字符串表示。

**系统能力：** SystemCapability.Communication.NFC.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|NFC状态值的字符串表示。|