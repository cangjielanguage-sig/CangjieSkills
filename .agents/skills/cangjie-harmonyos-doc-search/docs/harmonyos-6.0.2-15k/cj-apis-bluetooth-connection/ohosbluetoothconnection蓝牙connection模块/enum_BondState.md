## enum BondState

```cangjie
public enum BondState <: Equatable<BondState> & ToString {
    | BOND_STATE_INVALID
    | BOND_STATE_BONDING
    | BOND_STATE_BONDED
    | ...
}
```

**功能：** 配对状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<BondState>
- ToString

### BOND_STATE_BONDED

```cangjie
BOND_STATE_BONDED
```

**功能：** 已配对。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### BOND_STATE_BONDING

```cangjie
BOND_STATE_BONDING
```

**功能：** 正在配对。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### BOND_STATE_INVALID

```cangjie
BOND_STATE_INVALID
```

**功能：** 无效的配对。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(BondState)

```cangjie
public operator func !=(other: BondState): Bool
```

**功能：** 对配对状态进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BondState](#enum-bondstate)|是|配对状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个配对状态不同返回 true，否则返回 false。|

### func ==(BondState)

```cangjie
public operator func ==(other: BondState): Bool
```

**功能：** 对配对状态进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BondState](#enum-bondstate)|是|配对状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果配对状态相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回配对状态的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|配对状态的字符串表示。|