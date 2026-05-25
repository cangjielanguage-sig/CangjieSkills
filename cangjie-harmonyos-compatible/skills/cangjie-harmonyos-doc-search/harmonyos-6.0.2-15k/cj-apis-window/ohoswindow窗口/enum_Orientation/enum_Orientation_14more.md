## enum Orientation

```cangjie
public enum Orientation {
    | UNSPECIFIED
    | PORTRAIT
    | LANDSCAPE
    | PORTRAIT_INVERTED
    | LANDSCAPE_INVERTED
    | AUTO_ROTATION
    | AUTO_ROTATION_PORTRAIT
    | AUTO_ROTATION_LANDSCAPE
    | AUTO_ROTATION_RESTRICTED
    | AUTO_ROTATION_PORTRAIT_RESTRICTED
    | AUTO_ROTATION_LANDSCAPE_RESTRICTED
    | LOCKED
    | AUTO_ROTATION_UNSPECIFIED
    | USER_ROTATION_PORTRAIT
    | USER_ROTATION_LANDSCAPE
    | USER_ROTATION_PORTRAIT_INVERTED
    | USER_ROTATION_LANDSCAPE_INVERTED
    | FOLLOW_DESKTOP
}
```

**功能：** 窗口显示方向类型枚举。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### UNSPECIFIED

```cangjie
UNSPECIFIED
```

**功能：** 表示未定义方向模式，由系统判定。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### PORTRAIT

```cangjie
PORTRAIT
```

**功能：** 表示竖屏显示模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### LANDSCAPE

```cangjie
LANDSCAPE
```

**功能：** 表示横屏显示模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### PORTRAIT_INVERTED

```cangjie
PORTRAIT_INVERTED
```

**功能：** 表示反向竖屏显示模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### LANDSCAPE_INVERTED

```cangjie
LANDSCAPE_INVERTED
```

**功能：** 表示反向横屏显示模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### AUTO_ROTATION

```cangjie
AUTO_ROTATION
```

**功能：** 跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### AUTO_ROTATION_PORTRAIT

```cangjie
AUTO_ROTATION_PORTRAIT
```

**功能：** 调用时临时旋转到竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### AUTO_ROTATION_LANDSCAPE

```cangjie
AUTO_ROTATION_LANDSCAPE
```

**功能：** 跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### AUTO_ROTATION_RESTRICTED

```cangjie
AUTO_ROTATION_RESTRICTED
```

**功能：** 跟随传感器自动旋转，可以旋转到竖屏、横屏、反向竖屏、反向横屏四个方向，且受控制中心的旋转开关控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### AUTO_ROTATION_PORTRAIT_RESTRICTED

```cangjie
AUTO_ROTATION_PORTRAIT_RESTRICTED
```

**功能：** 跟随传感器自动竖向旋转，可以旋转到竖屏、反向竖屏，无法旋转到横屏、反向横屏，且受控制中心的旋转开关控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### AUTO_ROTATION_LANDSCAPE_RESTRICTED

```cangjie
AUTO_ROTATION_LANDSCAPE_RESTRICTED
```

**功能：** 跟随传感器自动横向旋转，可以旋转到横屏、反向横屏，无法旋转到竖屏、反向竖屏，且受控制中心的旋转开关控制。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### LOCKED

```cangjie
LOCKED
```

**功能：** 表示锁定模式。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### AUTO_ROTATION_UNSPECIFIED

```cangjie
AUTO_ROTATION_UNSPECIFIED
```

**功能：** 跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定（如在某种设备，可以旋转到竖屏、横屏、反向横屏三个方向，无法旋转到反向竖屏）。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19