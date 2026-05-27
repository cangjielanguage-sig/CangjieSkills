## enum HoverModeAreaType

```cangjie
public enum HoverModeAreaType {
    | TOP_SCREEN
    | BOTTOM_SCREEN
}
```

**功能：** 悬停态显示区域类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### BOTTOM_SCREEN

```cangjie
BOTTOM_SCREEN
```

**功能：** 下半屏。

**起始版本：** 19

### TOP_SCREEN

```cangjie
TOP_SCREEN
```

**功能：** 上半屏。

**起始版本：** 19

## enum KeyboardAvoidMode

```cangjie
public enum KeyboardAvoidMode {
    | DEFAULT
    | NONE
}
```

**功能：** 弹窗是否在拉起软键盘时进行自动避让。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 默认避让软键盘并在到达极限高度之后进行高度压缩。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NONE

```cangjie
NONE
```

**功能：** 不避让软键盘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ShadowStyle

```cangjie
public enum ShadowStyle {
    | OUTER_DEFAULT_XS
    | OUTER_DEFAULT_SM
    | OUTER_DEFAULT_MD
    | OUTER_DEFAULT_LG
    | OUTER_FLOATING_SM
    | OUTER_FLOATING_MD
}
```

**功能：** 阴影类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_LG

```cangjie
OUTER_DEFAULT_LG
```

**功能：** 大阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_MD

```cangjie
OUTER_DEFAULT_MD
```

**功能：** 中阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_SM

```cangjie
OUTER_DEFAULT_SM
```

**功能：** 小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_DEFAULT_XS

```cangjie
OUTER_DEFAULT_XS
```

**功能：** 超小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_FLOATING_MD

```cangjie
OUTER_FLOATING_MD
```

**功能：** 浮动中阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### OUTER_FLOATING_SM

```cangjie
OUTER_FLOATING_SM
```

**功能：** 浮动小阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum ToastShowMode

```cangjie
public enum ToastShowMode {
    | Default
    | TopMost
}
```

**功能：** 设置弹窗显示模式，默认显示在应用内，支持显示在应用之上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Default

```cangjie
Default
```

**功能：** Toast 显示在应用内。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### TopMost

```cangjie
TopMost
```

**功能：** Toast 显示在应用之上。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## type ShowActionMenuCallBack

```cangjie
public type ShowActionMenuCallBack = AsyncCallback<Int32>
```

**功能：** 菜单响应结果回调。Int32类型参数为选中按钮在buttons数组中的索引，从0开始。

## type ShowDialogCallBack

```cangjie
public type ShowDialogCallBack = AsyncCallback<Int32>
```

**功能：** 对话框响应结果回调。Int32类型参数为选中按钮在buttons数组中的索引。