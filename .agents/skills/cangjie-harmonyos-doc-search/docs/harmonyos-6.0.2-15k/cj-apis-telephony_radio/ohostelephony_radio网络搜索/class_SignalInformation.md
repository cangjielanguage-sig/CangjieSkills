## class SignalInformation

```cangjie
public class SignalInformation {
    public SignalInformation(
        public let signalType: NetworkType,
        public let signalLevel: Int32,
        public let dBm: Int32
    )
}
```

**功能：** 网络信号强度信息对象。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### let dBm

```cangjie
public let dBm: Int32
```

**功能：** 网络信号强度。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let signalLevel

```cangjie
public let signalLevel: Int32
```

**功能：** 网络信号强度等级。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let signalType

```cangjie
public let signalType: NetworkType
```

**功能：** 网络信号强度类型。

**类型：** [NetworkType](#enum-networktype)

**读写能力：** 只读

**起始版本：** 19

### SignalInformation(NetworkType, Int32, Int32)

```cangjie
public SignalInformation(
    public let signalType: NetworkType,
    public let signalLevel: Int32,
    public let dBm: Int32
)
```

**功能：** 构造SignalInformation实例。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|signalType|[NetworkType](#enum-networktype)|是|-|网络信号强度类型。|
|signalLevel|Int32|是|-|网络信号强度等级。|
|dBm|Int32|是|-|网络信号强度。|