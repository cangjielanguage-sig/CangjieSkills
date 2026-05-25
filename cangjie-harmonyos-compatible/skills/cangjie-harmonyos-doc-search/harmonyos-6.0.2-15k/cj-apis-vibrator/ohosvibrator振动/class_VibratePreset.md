## class VibratePreset

```cangjie
public class VibratePreset <: VibrateEffect {
    public var presetType: String
    public var effectId: String
    public var count: Int32
    public var intensity: Int32
    public init(presetType: String, effectId: String, count!: Int32 = 1, intensity!: Int32 = 100)
}
```

**功能：** 预置振动类型。

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

### var count

```cangjie
public var count: Int32
```

**功能：** 可选参数，振动的重复次数，默认值为1。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var effectId

```cangjie
public var effectId: String
```

**功能：** 预置的振动效果ID。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var intensity

```cangjie
public var intensity: Int32
```

**功能：** 可选参数，振动调节强度，范围为0到100，默认值为100。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var presetType

```cangjie
public var presetType: String
```

**功能：** 值为'preset'，按照预置振动效果触发马达振动。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### init(String, String, Int32, Int32)

```cangjie
public init(presetType: String, effectId: String, count!: Int32 = 1, intensity!: Int32 = 100)
```

**功能：** 用于创建VibratePreset实例的构造函数。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|presetType|String|是|-|值为'preset'，按照预置振动效果触发马达振动。|
|effectId|String|是|-|预置的振动效果ID。|
|count|Int32|否|1| **命名参数。** 可选参数，振动的重复次数，默认值为1。|
|intensity|Int32|否|100| **命名参数。** 可选参数，振动调节强度，范围为0到100，默认值为100。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*

let vPreset = VibratePreset("preset", 0)
```