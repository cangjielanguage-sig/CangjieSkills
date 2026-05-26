## enum Display

```cangjie
public enum Display <: ToString {
    | FONT_SCALE
    | SCREEN_BRIGHTNESS_STATUS
    | AUTO_SCREEN_BRIGHTNESS
    | SCREEN_OFF_TIMEOUT
    | DEFAULT_SCREEN_ROTATION
    | ANIMATOR_DURATION_SCALE
    | TRANSITION_ANIMATION_SCALE
    | WINDOW_ANIMATION_SCALE
    | DISPLAY_INVERSION_STATUS
    | ...
}
```

**功能：** 提供设置显示效果的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### ANIMATOR_DURATION_SCALE

```cangjie
ANIMATOR_DURATION_SCALE
```

**功能：** 动画持续时间的比例因子。这会影响所有此类动画的开始延迟和持续时间。值为0，表示动画将立即结束，默认值为1。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### AUTO_SCREEN_BRIGHTNESS

```cangjie
AUTO_SCREEN_BRIGHTNESS
```

**功能：** 启用屏幕的自动旋转时，此属性无效；不启用自动旋转时，以下值可用：值为0，表示屏幕旋转0度；值为1，表示屏幕旋转90度；值为2，表示屏幕旋转180度；值为3，表示屏幕旋转270度。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DEFAULT_SCREEN_ROTATION

```cangjie
DEFAULT_SCREEN_ROTATION
```

**功能：** 启用屏幕的自动旋转时，此属性无效；不启用自动旋转时，以下值可用：值为0，表示屏幕旋转0度；值为1，表示屏幕旋转90度；值为2，表示屏幕旋转180度；值为3，表示屏幕旋转270度。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DISPLAY_INVERSION_STATUS

```cangjie
DISPLAY_INVERSION_STATUS
```

**功能：** 是否启用显示颜色反转。值为1，表示启用显示颜色反转；值为0，表示不启用显示颜色反转。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### FONT_SCALE

```cangjie
FONT_SCALE
```

**功能：** 字体的比例因子，值为浮点数。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### SCREEN_BRIGHTNESS_STATUS

```cangjie
SCREEN_BRIGHTNESS_STATUS
```

**功能：** 屏幕亮度。该值的范围从0到255。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### SCREEN_OFF_TIMEOUT

```cangjie
SCREEN_OFF_TIMEOUT
```

**功能：** 设备在一段时间不活动后进入睡眠状态的等待时间（单位：ms）。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### TRANSITION_ANIMATION_SCALE

```cangjie
TRANSITION_ANIMATION_SCALE
```

**功能：** 过渡动画的比例因子。值为0，表示禁用过渡动画。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### WINDOW_ANIMATION_SCALE

```cangjie
WINDOW_ANIMATION_SCALE
```

**功能：** 通窗口动画的比例因子。值为0，表示禁用窗口动画。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置显示效果的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置显示效果的数据项。 |