## enum Axis

```cangjie
public enum Axis {
    | Vertical
    | Horizontal
}
```

**功能：** 轴方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Horizontal

```cangjie
Horizontal
```

**功能：** 方向为横向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Vertical

```cangjie
Vertical
```

**功能：** 方向为纵向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum BarrierDirection

```cangjie
public enum BarrierDirection {
    | LEFT
    | RIGHT
    | TOP
    | BOTTOM
}
```

**功能：** 定义屏障线的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### BOTTOM

```cangjie
BOTTOM
```

**功能：** 屏障在其所有referencedId的最下方。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LEFT

```cangjie
LEFT
```

**功能：** 屏障在其所有referencedId的最左侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### RIGHT

```cangjie
RIGHT
```

**功能：** 屏障在其所有referencedId的最右侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### TOP

```cangjie
TOP
```

**功能：** 屏障在其所有referencedId的最上方。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum BarState

```cangjie
public enum BarState {
    | Off
    | Auto
    | On
}
```

**功能：** 滚动条的显示模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Auto

```cangjie
Auto
```

**功能：** 按需显示(触摸时显示，2s后消失)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Off

```cangjie
Off
```

**功能：** 不显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### On

```cangjie
On
```

**功能：** 常驻显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum BlendApplyType

```cangjie
public enum BlendApplyType {
    | FAST
    | OFFSCREEN
}
```

**功能：** 指示如何将指定的混合模式应用于视图的内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### FAST

```cangjie
FAST
```

**功能：** 在目标图像上按顺序混合视图的内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OFFSCREEN

```cangjie
OFFSCREEN
```

**功能：** 将此组件和子组件内容绘制到离屏画布上，然后整体进行混合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19