## enum AnimatorDirection

```cangjie
public enum AnimatorDirection {
    | Normal
    | Reverse
    | Alternate
    | AlternateReverse
}
```

**功能：** 动画播放模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Alternate

```cangjie
Alternate
```

**功能：** 设置动画交替循环播放，奇数次正向播放，偶数次反向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### AlternateReverse

```cangjie
AlternateReverse
```

**功能：** 设置动画反向循环播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Normal

```cangjie
Normal
```

**功能：** 设置动画正向循环播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Reverse

```cangjie
Reverse
```

**功能：** 设置动画反向循环播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum AnimatorFill

```cangjie
public enum AnimatorFill {
    | None
    | Forwards
    | Backwards
    | Both
}
```

**功能：** 设置动画执行后是否恢复到初始状态，动画执行后，动画结束时的状态（在最后一个关键帧中定义）将保留。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Backwards

```cangjie
Backwards
```

**功能：** 设置动画将在animation-delay期间应用第一个关键帧中定义的值。当animation-direction为Normal或Alternate时应用from关键帧中的值，当animation-direction为Reverse或AlternateReverse时应用to关键帧中的值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Both

```cangjie
Both
```

**功能：** 设置动画将遵循forwards和backwards的规则，从而在两个方向上扩展动画属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Forwards

```cangjie
Forwards
```

**功能：** 设置在动画结束后，目标将保留动画结束时的状态（在最后一个关键帧中定义）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 设置在动画执行之前和之后都不会应用任何样式到目标上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12