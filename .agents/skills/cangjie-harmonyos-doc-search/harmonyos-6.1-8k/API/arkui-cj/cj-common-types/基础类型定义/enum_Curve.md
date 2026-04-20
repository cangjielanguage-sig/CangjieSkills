## enum Curve

```cangjie
public enum Curve <: Equatable<Curve> {
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
    | ...
}
```

**功能：** 动画曲线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[Curve](#enum-curve)>

### Linear

```cangjie
Linear
```

**功能：** 表示动画从头到尾的速度都是相同的。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Ease

```cangjie
Ease
```

**功能：** 表示动画以低速开始，然后加快，在结束前变慢，CubicBezier(0.25, 0.1, 0.25, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### EaseIn

```cangjie
EaseIn
```

**功能：** 表示动画以低速开始，CubicBezier(0.42, 0.0, 1.0, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### EaseOut

```cangjie
EaseOut
```

**功能：** 表示动画以低速结束，CubicBezier(0.0, 0.0, 0.58, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### EaseInOut

```cangjie
EaseInOut
```

**功能：** 表示动画以低速开始和结束，CubicBezier(0.42, 0.0, 0.58, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### FastOutSlowIn

```cangjie
FastOutSlowIn
```

**功能：** 标准曲线，cubic-bezier(0.4, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### LinearOutSlowIn

```cangjie
LinearOutSlowIn
```

**功能：** 减速曲线，cubic-bezier(0.0, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### FastOutLinearIn

```cangjie
FastOutLinearIn
```

**功能：** 加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### ExtremeDeceleration

```cangjie
ExtremeDeceleration
```

**功能：** 急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Sharp

```cangjie
Sharp
```

**功能：** 锐利曲线，CubicBezier(0.4, 0.0, 0.6, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Rhythm

```cangjie
Rhythm
```

**功能：** 节奏曲线，CubicBezier(0.7, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Smooth

```cangjie
Smooth
```

**功能：** 平滑曲线，CubicBezier(0.4, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Friction

```cangjie
Friction
```

**功能：** 阻尼曲线，CubicBezier(0.2, 0.0, 0.2, 1.0)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func ==(Curve)

```cangjie
public operator func ==(other: Curve): Bool
```

**功能：** 判断两个Curve枚举是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Curve](#enum-curve)|是|-|要比较的另一个Curve枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举相等则返回true，否则返回false。|

### operator func !=(Curve)

```cangjie
public operator func !=(other: Curve): Bool
```

**功能：** 判断两个Curve枚举是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[Curve](#enum-curve)|是|-|要比较的另一个Curve枚举。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举不相等则返回true，否则返回false。|