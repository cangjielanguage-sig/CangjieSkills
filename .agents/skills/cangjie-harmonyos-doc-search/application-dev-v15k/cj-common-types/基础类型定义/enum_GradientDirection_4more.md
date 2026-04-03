## enum GradientDirection

```cangjie
public enum GradientDirection {
    | Left
    | Top
    | Right
    | Bottom
    | LeftTop
    | LeftBottom
    | RightTop
    | RightBottom
    | None
}
```

**功能：** 梯度方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Bottom

```cangjie
Bottom
```

**功能：** 从上向下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Left

```cangjie
Left
```

**功能：** 从右向左。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LeftBottom

```cangjie
LeftBottom
```

**功能：** 左下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LeftTop

```cangjie
LeftTop
```

**功能：** 左上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 无。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Right

```cangjie
Right
```

**功能：** 从左向右。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### RightBottom

```cangjie
RightBottom
```

**功能：** 右下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### RightTop

```cangjie
RightTop
```

**功能：** 右上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Top

```cangjie
Top
```

**功能：** 从下向上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum GridItemStyle

```cangjie
public enum GridItemStyle {
    | NONE
    | PLAIN
}
```

**功能：** 设置GridItem样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 设置为GridItemStyle.NONE时不显示Hover（悬停）和Press（按压）态样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### PLAIN

```cangjie
PLAIN
```

**功能：** 设置为GridItemStyle.PLAIN时，显示Hover（悬停）、Press（按压）态样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum HeightBreakpoint

```cangjie
public enum HeightBreakpoint {
    | HEIGHT_SM
    | HEIGHT_MD
    | HEIGHT_LG
}
```

**功能：** 表示窗口不同高宽比阈值下对应的高度断点枚举值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HEIGHT_LG

```cangjie
HEIGHT_LG
```

**功能：** 窗口高宽比大于等于1.2。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HEIGHT_MD

```cangjie
HEIGHT_MD
```

**功能：** 窗口高宽比大于等于0.8，且小于1.2。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### HEIGHT_SM

```cangjie
HEIGHT_SM
```

**功能：** 窗口高宽比小于0.8。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum HitTestMode

```cangjie
public enum HitTestMode {
    | Default
    | Block
    | Transparent
    | None
}
```

**功能：** 触摸测试效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Block

```cangjie
Block
```

**功能：** 自身节点响应触摸事件的命中测试，但阻止被该节点屏蔽的子节点和其他节点的命中测试。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Default

```cangjie
Default
```

**功能：** 自身节点和子节点都响应触摸事件的命中测试，但会阻止被该节点屏蔽的其他节点的命中测试。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### None

```cangjie
None
```

**功能：** 自身节点不会响应触摸事件的命中测试，但子节点会对触摸事件进行命中测试。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Transparent

```cangjie
Transparent
```

**功能：** 自身节点和子节点响应触摸事件的命中测试，并允许对被该节点屏蔽的其他节点进行命中测试。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19