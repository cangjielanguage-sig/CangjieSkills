## enum Usage

```cangjie
public enum Usage <: ToString & Equatable<Usage> {
    | UNKNOWN
    | ALARM
    | RING
    | NOTIFICATION
    | COMMUNICATION
    | TOUCH
    | MEDIA
    | PHYSICALFEEDBACK
    | SIMULATEREALITY
    | ...
}
```

**功能：** 振动使用场景。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<Usage>

### ALARM

```cangjie
ALARM
```

**功能：** 用于警报场景。

**起始版本：** 19

### COMMUNICATION

```cangjie
COMMUNICATION
```

**功能：** 用于通信场景。

**起始版本：** 19

### MEDIA

```cangjie
MEDIA
```

**功能：** 用于多媒体场景。

**起始版本：** 19

### NOTIFICATION

```cangjie
NOTIFICATION
```

**功能：** 用于通知场景。

**起始版本：** 19

### PHYSICALFEEDBACK

```cangjie
PHYSICALFEEDBACK
```

**功能：** 用于物理反馈场景。

**起始版本：** 19

### RING

```cangjie
RING
```

**功能：** 用于铃声场景。

**起始版本：** 19

### SIMULATEREALITY

```cangjie
SIMULATEREALITY
```

**功能：** 用于模拟现实场景。

**起始版本：** 19

### TOUCH

```cangjie
TOUCH
```

**功能：** 用于触摸场景。

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 没有明确使用场景，最低优先级。

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回振动使用场景的字符串表示。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

### func !=(Usage)

```cangjie
public operator func !=(that: Usage): Bool
```

**功能：** 对振动使用场景进行判不等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                 | 必填 | 说明           |
| :----- | :------------------- | :--- | :------------- |
| that   | [Usage](#enum-usage) | 是   | 振动使用场景。 |

**返回值：**

| 类型 | 说明                                              |
| :--- | :------------------------------------------------ |
| Bool | 如果两个振动使用场景不同返回true，否则返回false。 |

### func ==(Usage)

```cangjie
public operator func ==(that: Usage): Bool
```

**功能：** 对振动使用场景进行判等。

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 19

**参数：**

| 参数名 | 类型                 | 必填 | 说明           |
| :----- | :------------------- | :--- | :------------- |
| that   | [Usage](#enum-usage) | 是   | 振动使用场景。 |

**返回值：**

| 类型 | 说明                                              |
| :--- | :------------------------------------------------ |
| Bool | 如果两个振动使用场景相同返回true，否则返回false。 |