## enum AvoidAreaType

```cangjie
public enum AvoidAreaType {
    | TYPE_SYSTEM
    | TYPE_CUTOUT
    | TYPE_SYSTEM_GESTURE
    | TYPE_KEYBOARD
    | TYPE_NAVIGATION_INDICATOR
}
```

**功能：** 窗口内容需要规避区域的类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### TYPE_SYSTEM

```cangjie
TYPE_SYSTEM
```

**功能：** 表示系统默认区域。一般包括状态栏、导航栏，各设备系统定义可能不同。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### TYPE_CUTOUT

```cangjie
TYPE_CUTOUT
```

**功能：** 表示刘海屏区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### TYPE_SYSTEM_GESTURE

```cangjie
TYPE_SYSTEM_GESTURE
```

**功能：** 表示手势区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### TYPE_KEYBOARD

```cangjie
TYPE_KEYBOARD
```

**功能：** 表示软键盘区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### TYPE_NAVIGATION_INDICATOR

```cangjie
TYPE_NAVIGATION_INDICATOR
```

**功能：** 表示导航条区域。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

## enum ColorSpace

```cangjie
public enum ColorSpace {
    | DEFAULT
    | WIDE_GAMUT
}
```

**功能：** 色域模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 默认SRGB色域模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### WIDE_GAMUT

```cangjie
WIDE_GAMUT
```

**功能：** 广色域模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

## enum MaximizePresentation

```cangjie
public enum MaximizePresentation {
    | FOLLOW_APP_IMMERSIVE_SETTING
    | EXIT_IMMERSIVE
    | ENTER_IMMERSIVE
}
```

**功能：** 窗口最大化时的布局枚举。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### FOLLOW_APP_IMMERSIVE_SETTING

```cangjie
FOLLOW_APP_IMMERSIVE_SETTING
```

**功能：** 最大化时，跟随应用app当前设置的沉浸式布局。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### EXIT_IMMERSIVE

```cangjie
EXIT_IMMERSIVE
```

**功能：** 最大化时，如果当前窗口设置了沉浸式布局会退出沉浸式布局。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### ENTER_IMMERSIVE

```cangjie
ENTER_IMMERSIVE
```

**功能：** 最大化时，进入沉浸式布局。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19