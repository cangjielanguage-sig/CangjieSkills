## class VibrateTime

```cangjie
public class VibrateTime <: VibrateEffect {
    public var timeType: String
    public var duration: Int32
    public init(timeType: String, duration: Int32)
}
```

**功能：** 固定时长振动类型。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**父类型：**

- [VibrateEffect](#interface-vibrateeffect)

### prop effectType

```cangjie
public prop effectType: String
```

**功能：** 马达振动效果类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### var duration

```cangjie
public var duration: Int32
```

**功能：** 马达持续振动时长，单位ms。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var timeType

```cangjie
public var timeType: String
```

**功能：** 值为'time'，按照指定持续时间触发马达振动。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### init(String, Int32)

```cangjie
public init(timeType: String, duration: Int32)
```

**功能：** 用于创建VibrateTime实例的构造函数。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeType|String|是|-|值为'time'，按照指定持续时间触发马达振动。|
|duration|Int32|是|-|马达持续振动时长，单位ms。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*

let vTime = VibrateTime("time", 0)
```

## enum EffectId

```cangjie
public enum EffectId <: ToString & Equatable<EffectId> {
    | EFFECT_CLOCK_TIMER
    | ...
}
```

**功能：** 预置的振动效果。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<EffectId>

### EFFECT_CLOCK_TIMER

```cangjie
EFFECT_CLOCK_TIMER
```

**功能：** 描述用户调整计时器时的振动效果。

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回预设振动效果的字符串表示。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**返回值：**

| 类型 | 说明                                                |
| :--- | :-------------------------------------------------- |
| Bool | 如果两个预置的振动效果相同返回true，否则返回false。 |

### func !=(EffectId)

```cangjie
public operator func !=(that: EffectId): Bool
```

**功能：** 对预设振动效果进行判不等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                       | 必填 | 说明             |
| :----- | :------------------------- | :--- | :--------------- |
| that   | [EffectId](#enum-effectid) | 是   | 预置的振动效果。 |

**返回值：**

| 类型 | 说明                                                |
| :--- | :-------------------------------------------------- |
| Bool | 如果两个预置的振动效果不同返回true，否则返回false。 |

### func ==(EffectId)

```cangjie
public operator func ==(that: EffectId): Bool
```

**功能：** 对预设振动效果进行判等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                       | 必填 | 说明             |
| :----- | :------------------------- | :--- | :--------------- |
| that   | [EffectId](#enum-effectid) | 是   | 预置的振动效果。 |

**返回值：**

| 类型 | 说明                                                |
| :--- | :-------------------------------------------------- |
| Bool | 如果两个预置的振动效果相同返回true，否则返回false。 |