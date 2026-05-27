## enum DisplayOrientation

```cangjie
public enum DisplayOrientation {
    | UNSPECIFIED
    | LANDSCAPE
    | PORTRAIT
    | FOLLOW_RECENT
    | LANDSCAPE_INVERTED
    | PORTRAIT_INVERTED
    | AUTO_ROTATION
    | AUTO_ROTATION_LANDSCAPE
    | AUTO_ROTATION_PORTRAIT
    | AUTO_ROTATION_RESTRICTED
    | AUTO_ROTATION_LANDSCAPE_RESTRICTED
    | AUTO_ROTATION_PORTRAIT_RESTRICTED
    | LOCKED
    | AUTO_ROTATION_UNSPECIFIED
    | FOLLOW_DESKTOP
    | ...
}
```

**功能：** 标识该Ability的显示模式。该标签仅适用于page类型的Ability。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### AUTO_ROTATION

```cangjie
AUTO_ROTATION
```

**功能：** 表示传感器自动旋转模式。

**起始版本：** 12

### AUTO_ROTATION_LANDSCAPE

```cangjie
AUTO_ROTATION_LANDSCAPE
```

**功能：** 表示传感器自动横向旋转模式。

**起始版本：** 12

### AUTO_ROTATION_LANDSCAPE_RESTRICTED

```cangjie
AUTO_ROTATION_LANDSCAPE_RESTRICTED
```

**功能：** 表示受开关控制的自动横向旋转模式。

**起始版本：** 12

### AUTO_ROTATION_PORTRAIT

```cangjie
AUTO_ROTATION_PORTRAIT
```

**功能：** 表示传感器自动竖向旋转模式。

**起始版本：** 12

### AUTO_ROTATION_PORTRAIT_RESTRICTED

```cangjie
AUTO_ROTATION_PORTRAIT_RESTRICTED
```

**功能：** 表示受开关控制的自动竖向旋转模式。

**起始版本：** 12

### AUTO_ROTATION_RESTRICTED

```cangjie
AUTO_ROTATION_RESTRICTED
```

**功能：** 表示受开关控制的自动旋转模式。

**起始版本：** 12

### AUTO_ROTATION_UNSPECIFIED

```cangjie
AUTO_ROTATION_UNSPECIFIED
```

**功能：** 受开关控制和由系统判定的自动旋转模式。

**起始版本：** 19

### FOLLOW_DESKTOP

```cangjie
FOLLOW_DESKTOP
```

**功能：** 跟随桌面的旋转模式。

**起始版本：** 19

### FOLLOW_RECENT

```cangjie
FOLLOW_RECENT
```

**功能：** 表示跟随上一个显示模式。

**起始版本：** 12

### LANDSCAPE

```cangjie
LANDSCAPE
```

**功能：** 表示横屏显示模式。

**起始版本：** 12

### LANDSCAPE_INVERTED

```cangjie
LANDSCAPE_INVERTED
```

**功能：** 表示反向横屏显示模式。

**起始版本：** 12

### LOCKED

```cangjie
LOCKED
```

**功能：** 表示锁定模式。

**起始版本：** 12

### PORTRAIT

```cangjie
PORTRAIT
```

**功能：** 表示竖屏显示模式。

**起始版本：** 12

### PORTRAIT_INVERTED

```cangjie
PORTRAIT_INVERTED
```

**功能：** 表示反向竖屏显示模式。

**起始版本：** 12

### UNSPECIFIED

```cangjie
UNSPECIFIED
```

**功能：** 表示未定义方向模式，由系统判定。

**起始版本：** 12