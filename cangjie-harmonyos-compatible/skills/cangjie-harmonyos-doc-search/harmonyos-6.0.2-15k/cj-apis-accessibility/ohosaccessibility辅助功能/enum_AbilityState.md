## enum AbilityState

```cangjie
public enum AbilityState <: Equatable<AbilityState> & ToString {
    | ABILITYSTATE_ENABLE
    | ABILITYSTATE_DISABLE
    | ABILITYSTATE_INSTALL
    | ...
}
```

**功能：** 辅助应用状态类型。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**父类型：**

- Equatable\<AbilityState>
- ToString

### ABILITYSTATE_DISABLE

```cangjie
ABILITYSTATE_DISABLE
```

**功能：** 表示辅助应用已禁用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ABILITYSTATE_ENABLE

```cangjie
ABILITYSTATE_ENABLE
```

**功能：** 表示辅助应用已启用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ABILITYSTATE_INSTALL

```cangjie
ABILITYSTATE_INSTALL
```

**功能：** 表示辅助应用已安装。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### func !=(AbilityState)

```cangjie
public operator func !=(other: AbilityState): Bool
```

**功能：** 对应用状态类型进行判不等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AbilityState](#enum-abilitystate)|是|-|应用状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果应用状态类型不同，返回true，否则返回false。|

### func ==(AbilityState)

```cangjie
public operator func ==(other: AbilityState): Bool
```

**功能：** 对应用状态类型进行判等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AbilityState](#enum-abilitystate)|是|-|应用状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果应用状态类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将应用状态转换为字符串。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|应用状态的字符串表示。|