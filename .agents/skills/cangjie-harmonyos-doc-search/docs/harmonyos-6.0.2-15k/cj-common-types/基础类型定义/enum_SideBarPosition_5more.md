## enum SideBarPosition

```cangjie
public enum SideBarPosition {
    | Start
    | End
}
```

**功能：** 设置侧边栏显示位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### End

```cangjie
End
```

**功能：** 侧边栏位于容器右侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Start

```cangjie
Start
```

**功能：** 侧边栏位于容器左侧。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum SourceTool

```cangjie
public enum SourceTool {
    | Unknown
    | Finger
    | Pen
    | Mouse
    | Touchpad
    | Joystick
}
```

**功能：** 事件输入源。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Finger

```cangjie
Finger
```

**功能：** 手指输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Joystick

```cangjie
Joystick
```

**功能：** 手柄输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Mouse

```cangjie
Mouse
```

**功能：** 鼠标输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Pen

```cangjie
Pen
```

**功能：** 手写笔输入。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Touchpad

```cangjie
Touchpad
```

**功能：** 触控板输入。触控板单指输入被视为鼠标输入操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Unknown

```cangjie
Unknown
```

**功能：** 未知输入源。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum SourceType

```cangjie
public enum SourceType {
    | Unknown
    | Mouse
    | TouchScreen
}
```

**功能：** 事件输入设备。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Mouse

```cangjie
Mouse
```

**功能：** 鼠标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### TouchScreen

```cangjie
TouchScreen
```

**功能：** 触摸屏。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Unknown

```cangjie
Unknown
```

**功能：** 未知设备。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum SwiperNestedScrollMode

```cangjie
public enum SwiperNestedScrollMode {
    | SELF_ONLY
    | SELF_FIRST
}
```

**功能：** Swiper组件和父组件的嵌套滚动模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SELF_FIRST

```cangjie
SELF_FIRST
```

**功能：** Swiper自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则Swiper触发边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SELF_ONLY

```cangjie
SELF_ONLY
```

**功能：** Swiper只自身滚动，不与父组件联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum TextAlign

```cangjie
public enum TextAlign {
    | Start
    | Center
    | End
    | JUSTIFY
}
```

**功能：** 文本对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Center

```cangjie
Center
```

**功能：** 水平居中对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### End

```cangjie
End
```

**功能：** 水平对齐尾部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### JUSTIFY

```cangjie
JUSTIFY
```

**功能：** 双端对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Start

```cangjie
Start
```

**功能：** 水平对齐首部。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12