## enum ItemAlign

```cangjie
public enum ItemAlign {
    | Auto
    | Start
    | Center
    | End
    | Stretch
    | Baseline
}
```

**功能：** 元素对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Auto

```cangjie
Auto
```

**功能：** 使用Flex容器中默认配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Baseline

```cangjie
Baseline
```

**功能：** 元素在Flex容器中，交叉轴方向文本基线对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Center

```cangjie
Center
```

**功能：** 元素在Flex容器中，交叉轴方向居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### End

```cangjie
End
```

**功能：** 元素在Flex容器中，交叉轴方向底部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Start

```cangjie
Start
```

**功能：** 元素在Flex容器中，交叉轴方向首部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Stretch

```cangjie
Stretch
```

**功能：** 元素在Flex容器中，交叉轴方向拉伸填充。容器为Flex且设置Wrap为FlexWrap.Wrap或FlexWrap.WrapReverse时，元素拉伸到与当前行/列交叉轴长度最长的元素尺寸。其余情况下，无论元素尺寸是否设置，均拉伸到容器尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum KeyboardAvoidMode

```cangjie
public enum KeyboardAvoidMode {
    | DEFAULT
    | NONE
}
```

**功能：** 弹窗是否在拉起软键盘时进行自动避让。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 默认避让软键盘并在到达极限高度之后进行高度压缩。

**起始版本：** 12

### NONE

```cangjie
NONE
```

**功能：** 不避让软键盘。

**起始版本：** 12

## enum KeySource

```cangjie
public enum KeySource {
    | Unknown
    | Keyboard
}
```

**功能：** 输入设备类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Keyboard

```cangjie
Keyboard
```

**功能：** 输入设备类型为键盘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Unknown

```cangjie
Unknown
```

**功能：** 输入设备类型未知。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum KeyType

```cangjie
public enum KeyType {
    | Down
    | Up
}
```

**功能：** 按键类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Down

```cangjie
Down
```

**功能：** 按键按下。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Up

```cangjie
Up
```

**功能：** 按键松开。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum LayoutSafeAreaEdge

```cangjie
public enum LayoutSafeAreaEdge {
    | TOP
    | BOTTOM
}
```

**功能：** 扩展安全区域的方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### BOTTOM

```cangjie
BOTTOM
```

**功能：** 下方区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### TOP

```cangjie
TOP
```

**功能：** 上方区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum LayoutSafeAreaType

```cangjie
public enum LayoutSafeAreaType {
    SYSTEM
}
```

**功能：** 扩展布局安全区域的枚举类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SYSTEM

```cangjie
SYSTEM
```

**功能：** 系统默认非安全区域，包括状态栏、导航栏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19