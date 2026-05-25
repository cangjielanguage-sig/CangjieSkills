## enum PlayMode

```cangjie
public enum PlayMode {
    | Normal
    | Reverse
    | Alternate
    | AlternateReverse
}
```

**功能：** 动画播放方向设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Alternate

```cangjie
Alternate
```

**功能：** 动画在奇数次（1、3、5...）正向播放，在偶数次（2、4、6...）反向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### AlternateReverse

```cangjie
AlternateReverse
```

**功能：** 动画在奇数次（1、3、5...）反向播放，在偶数次（2、4、6...）正向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Normal

```cangjie
Normal
```

**功能：** 动画正向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Reverse

```cangjie
Reverse
```

**功能：** 动画反向播放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ProgressType

```cangjie
public enum ProgressType {
    | Linear
    | Ring
    | Eclipse
    | ScaleRing
    | Capsule
}
```

**功能：** Progress组件的样式类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Capsule

```cangjie
Capsule
```

**功能：** 胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同；中段处的进度展示效果与Linear相同。高度大于宽度的时候自适应垂直显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Eclipse

```cangjie
Eclipse
```

**功能：** 圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Linear

```cangjie
Linear
```

**功能：** 线性样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Ring

```cangjie
Ring
```

**功能：** 环形无刻度样式，环形圆环逐渐显示至完全填充效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### ScaleRing

```cangjie
ScaleRing
```

**功能：** 环形有刻度样式，显示类似时钟刻度形式的进度展示效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum QualityType

```cangjie
public enum QualityType {
    | Low
    | Medium
    | High
}
```

**功能：** 设置图像平滑度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### high

```cangjie
high
```

**功能：** 高画质。

**起始版本：** 12

### low

```cangjie
low
```

**功能：** 低画质。

**起始版本：** 12

### medium

```cangjie
medium
```

**功能：** 中画质。

**起始版本：** 12

## enum RefreshStatus

```cangjie
public enum RefreshStatus {
    | Inactive
    | Drag
    | OverDrag
    | Refresh
    | Done
}
```

**功能：** 下拉状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Inactive

```cangjie
Inactive
```

**功能：** 默认未下拉状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Drag

```cangjie
Drag
```

**功能：** 下拉中，下拉距离小于刷新距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### OverDrag

```cangjie
OverDrag
```

**功能：** 下拉中，下拉距离超过刷新距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Refresh

```cangjie
Refresh
```

**功能：** 下拉结束，回弹至刷新距离，进入刷新状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Done

```cangjie
Done
```

**功能：** 刷新结束，返回初始状态（顶部）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12