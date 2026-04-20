## class NetworkState

```cangjie
public class NetworkState {
    public NetworkState(
        public let longOperatorName: String,
        public let shortOperatorName: String,
        public let plmnNumeric: String,
        public let isRoaming: Bool,
        public let regState: RegState,
        public let cfgTech: RadioTechnology,
        public let nsaState: NsaState,
        public let isCaActive: Bool,
        public let isEmergency: Bool
    )
}
```

**功能：** 网络注册状态。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

### let cfgTech

```cangjie
public let cfgTech: RadioTechnology
```

**功能：** 设备的无线接入技术。

**类型：** [RadioTechnology](#enum-radiotechnology)

**读写能力：** 只读

**起始版本：** 19

### let isCaActive

```cangjie
public let isCaActive: Bool
```

**功能：** CA的状态。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isEmergency

```cangjie
public let isEmergency: Bool
```

**功能：** 此设备是否只允许拨打紧急呼叫。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let isRoaming

```cangjie
public let isRoaming: Bool
```

**功能：** 是否处于漫游状态。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let longOperatorName

```cangjie
public let longOperatorName: String
```

**功能：** 注册网络的长运营商名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let nsaState

```cangjie
public let nsaState: NsaState
```

**功能：** 设备的NSA网络注册状态。

**类型：** [NsaState](#enum-nsastate)

**读写能力：** 只读

**起始版本：** 19

### let plmnNumeric

```cangjie
public let plmnNumeric: String
```

**功能：** 注册网络的PLMN码。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let regState

```cangjie
public let regState: RegState
```

**功能：** 设备的网络注册状态。

**类型：** [RegState](#enum-regstate)

**读写能力：** 只读

**起始版本：** 19

### let shortOperatorName

```cangjie
public let shortOperatorName: String
```

**功能：** 注册网络的短运营商名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### NetworkState(String, String, String, Bool, RegState, RadioTechnology, NsaState, Bool, Bool)

```cangjie
public NetworkState(
    public let longOperatorName: String,
    public let shortOperatorName: String,
    public let plmnNumeric: String,
    public let isRoaming: Bool,
    public let regState: RegState,
    public let cfgTech: RadioTechnology,
    public let nsaState: NsaState,
    public let isCaActive: Bool,
    public let isEmergency: Bool
)
```

**功能：** 构造NetworkState实例。

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|longOperatorName|String|是|-|注册网络的长运营商名称。|
|shortOperatorName|String|是|-|注册网络的短运营商名称。|
|plmnNumeric|String|是|-|注册网络的PLMN码。|
|isRoaming|Bool|是|-|是否处于漫游状态。|
|regState|[RegState](#enum-regstate)|是|-|设备的网络注册状态。|
|cfgTech|[RadioTechnology](#enum-radiotechnology)|是|-|设备的无线接入技术。|
|nsaState|[NsaState](#enum-nsastate)|是|-|设备的NSA网络注册状态。|
|isCaActive|Bool|是|-|CA的状态。|
|isEmergency|Bool|是|-|此设备是否只允许拨打紧急呼叫。|