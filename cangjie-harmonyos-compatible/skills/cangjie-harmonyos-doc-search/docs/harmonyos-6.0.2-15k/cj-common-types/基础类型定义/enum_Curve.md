## enum Curve

```cangjie
public enum Curve {
    | Linear
    | Ease
    | EaseIn
    | EaseOut
    | EaseInOut
    | FastOutSlowIn
    | LinearOutSlowIn
    | FastOutLinearIn
    | ExtremeDeceleration
    | Sharp
    | Rhythm
    | Smooth
    | Friction
}
```

**功能：** 插值曲线，动效请参考贝塞尔曲线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Ease

```cangjie
Ease
```

**功能：** 表示动画以低速开始，然后加快，在结束前变慢，CubicBezier(0.25, 0.1, 0.25, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### EaseIn

```cangjie
EaseIn
```

**功能：** 表示动画以低速开始，CubicBezier(0.42, 0.0, 1.0, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### EaseInOut

```cangjie
EaseInOut
```

**功能：** 表示动画以低速开始和结束，CubicBezier(0.42, 0.0, 0.58, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### EaseOut

```cangjie
EaseOut
```

**功能：** 表示动画以低速结束，CubicBezier(0.0, 0.0, 0.58, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### ExtremeDeceleration

```cangjie
ExtremeDeceleration
```

**功能：** 急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### FastOutLinearIn

```cangjie
FastOutLinearIn
```

**功能：** 加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### FastOutSlowIn

```cangjie
FastOutSlowIn
```

**功能：** 标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Friction

```cangjie
Friction
```

**功能：** 阻尼曲线，CubicBezier(0.2, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Linear

```cangjie
Linear
```

**功能：** 表示动画从头到尾的速度都是相同的。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LinearOutSlowIn

```cangjie
LinearOutSlowIn
```

**功能：** 标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Rhythm

```cangjie
Rhythm
```

**功能：** 节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Sharp

```cangjie
Sharp
```

**功能：** 锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Smooth

```cangjie
Smooth
```

**功能：** 平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12