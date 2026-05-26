## enum HapticFeedback

```cangjie
public enum HapticFeedback <: ToString & Equatable<HapticFeedback> {
    | EFFECT_SOFT
    | EFFECT_HARD
    | EFFECT_SHARP
    | ...
}
```

**功能：** 简单而通用的振动效果。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<HapticFeedback>

### EFFECT_HARD

```cangjie
EFFECT_HARD
```

**功能：** 较沉重的振动效果，频率居中。

**起始版本：** 19

### EFFECT_SHARP

```cangjie
EFFECT_SHARP
```

**功能：** 较尖锐的振动效果，频率偏高。

**起始版本：** 19

### EFFECT_SOFT

```cangjie
EFFECT_SOFT
```

**功能：** 较松散的振动效果，频率偏低。

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回简单而通用的振动效果的字符串表示。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**返回值：**

| 类型 | 说明                                                |
| :--- | :-------------------------------------------------- |
| String | 简单而通用的振动效果的字符串表示。 |

### func !=(HapticFeedback)

```cangjie
public operator func !=(that: HapticFeedback): Bool
```

**功能：** 对简单而通用的振动效果进行判不等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                                   | 必填 | 说明                   |
| :----- | :------------------------------------- | :--- | :--------------------- |
| that   | [HapticFeedback](#enum-hapticfeedback) | 是   | 简单而通用的振动效果。 |

**返回值：**

| 类型 | 说明                                                      |
| :--- | :-------------------------------------------------------- |
| Bool | 如果两个简单而通用的振动效果不同返回true，否则返回false。 |

### func ==(HapticFeedback)

```cangjie
public operator func ==(that: HapticFeedback): Bool
```

**功能：** 对简单而通用的振动效果进行判等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                                   | 必填 | 说明                   |
| :----- | :------------------------------------- | :--- | :--------------------- |
| that   | [HapticFeedback](#enum-hapticfeedback) | 是   | 简单而通用的振动效果。 |

**返回值：**

| 类型 | 说明                                                      |
| :--- | :-------------------------------------------------------- |
| Bool | 如果两个简单而通用的振动效果相同返回true，否则返回false。 |