## enum VibratorStopMode

```cangjie
public enum VibratorStopMode <: ToString & Equatable<VibratorStopMode> {
    | VIBRATOR_STOP_MODE_TIME
    | VIBRATOR_STOP_MODE_PRESET
    | ...
}
```

**功能：** 停止振动的模式。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<VibratorStopMode>

### VIBRATOR_STOP_MODE_PRESET

```cangjie
VIBRATOR_STOP_MODE_PRESET
```

**功能：** 停止预置EffectId的振动。

**起始版本：** 19

### VIBRATOR_STOP_MODE_TIME

```cangjie
VIBRATOR_STOP_MODE_TIME
```

**功能：** 停止duration模式的振动。

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回停止振动的模式的字符串表示。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

### func !=(VibratorStopMode)

```cangjie
public operator func !=(that: VibratorStopMode): Bool
```

**功能：** 对停止振动的模式进行判不等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                                       | 必填 | 说明             |
| :----- | :----------------------------------------- | :--- | :--------------- |
| that   | [VibratorStopMode](#enum-vibratorstopmode) | 是   | 停止振动的模式。 |

**返回值：**

| 类型 | 说明                                                |
| :--- | :-------------------------------------------------- |
| Bool | 如果两个停止振动的模式不同返回true，否则返回false。 |

### func ==(VibratorStopMode)

```cangjie
public operator func ==(that: VibratorStopMode): Bool
```

**功能：** 对停止振动的模式进行判等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                                       | 必填 | 说明             |
| :----- | :----------------------------------------- | :--- | :--------------- |
| that   | [VibratorStopMode](#enum-vibratorstopmode) | 是   | 停止振动的模式。 |

**返回值：**

| 类型 | 说明                                                |
| :--- | :-------------------------------------------------- |
| Bool | 如果两个停止振动的模式相同返回true，否则返回false。 |