## enum AbilityType

```cangjie
public enum AbilityType <: Equatable<AbilityType> & ToString {
    | ABILITYTYPE_AUDIBLE
    | ABILITYTYPE_GENERIC
    | ABILITYTYPE_HAPTIC
    | ABILITYTYPE_SPOKEN
    | ABILITYTYPE_VISUAL
    | ABILITYTYPE_ALL
    | ...
}
```

**功能：** 无障碍辅助应用类型。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**父类型：**

- Equatable\<AbilityType>
- ToString

### ABILITYTYPE_ALL

```cangjie
ABILITYTYPE_ALL
```

**功能：** 表示以上所有类别。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ABILITYTYPE_AUDIBLE

```cangjie
ABILITYTYPE_AUDIBLE
```

**功能：** 表示具有听觉反馈。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ABILITYTYPE_GENERIC

```cangjie
ABILITYTYPE_GENERIC
```

**功能：** 表示具有通用反馈。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ABILITYTYPE_HAPTIC

```cangjie
ABILITYTYPE_HAPTIC
```

**功能：** 表示具有触觉反馈。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ABILITYTYPE_SPOKEN

```cangjie
ABILITYTYPE_SPOKEN
```

**功能：** 表示具有语音反馈。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### ABILITYTYPE_VISUAL

```cangjie
ABILITYTYPE_VISUAL
```

**功能：** 表示具有视觉反馈。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

### func !=(AbilityType)

```cangjie
public operator func !=(other: AbilityType): Bool
```

**功能：** 对应用类型进行判不等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AbilityType](#enum-abilitytype)|是|-|应用类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若应用类型不同，返回true，否则返回false。|

### func ==(AbilityType)

```cangjie
public operator func ==(other: AbilityType): Bool
```

**功能：** 对应用类型进行判等。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AbilityType](#enum-abilitytype)|是|-|应用类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|若应用类型相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 将应用类型转换为字符串。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|应用类型的字符串表示。|