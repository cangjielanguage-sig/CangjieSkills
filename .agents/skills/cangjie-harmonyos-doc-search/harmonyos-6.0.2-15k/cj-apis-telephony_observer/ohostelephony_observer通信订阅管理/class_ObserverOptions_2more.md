## class ObserverOptions

```cangjie
public class ObserverOptions {
    public ObserverOptions(
        public var slotId!: Int32 = 0
    )
}
```

**功能：** 电话相关事件订阅参数。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

### var slotId

```cangjie
public var slotId: Int32 = 0
```

**功能：** 卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### ObserverOptions(Int32)

```cangjie
public ObserverOptions(
    public var slotId!: Int32 = 0
)
```

**功能：** 构造ObserverOptions实例。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slotId|Int32|否|0| **命名参数。** 卡槽ID。<br>- 0：卡槽1<br>- 1：卡槽2|

## class SimStateData

```cangjie
public class SimStateData {
    public SimStateData(
        public let cardType: CardType,
        public let state: SimState,
        public let reason: LockReason
    )
}
```

**功能：** SIM卡类型和状态。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

### let cardType

```cangjie
public let cardType: CardType
```

**功能：** SIM卡类型。

**类型：** [CardType](cj-apis-telephony_sim.md#enum-cardtype)

**读写能力：** 只读

**起始版本：** 19

### let reason

```cangjie
public let reason: LockReason
```

**功能：** SIM卡锁类型。

**类型：** [LockReason](#enum-lockreason)

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: SimState
```

**功能：** SIM卡状态。

**类型：** [SimState](cj-apis-telephony_sim.md#enum-simstate)

**读写能力：** 只读

**起始版本：** 19

### SimStateData(CardType, SimState, LockReason)

```cangjie
public SimStateData(
    public let cardType: CardType,
    public let state: SimState,
    public let reason: LockReason
)
```

**功能：** 构造SimStateData实例。

**系统能力：** SystemCapability.Telephony.StateRegistry

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cardType|[CardType](cj-apis-telephony_sim.md#enum-cardtype)|是|-|SIM卡类型。|
|state|[SimState](cj-apis-telephony_sim.md#enum-simstate)|是|-|SIM卡状态。|
|reason|[LockReason](#enum-lockreason)|是|-|SIM卡锁类型。|