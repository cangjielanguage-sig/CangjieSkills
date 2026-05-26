## enum NestedScrollMode

```cangjie
public enum NestedScrollMode {
    | SELF_ONLY
    | SELF_FIRST
    | PARENT_FIRST
    | PARALLEL
}
```

**功能：** 可滚动组件往末尾端滚动时的嵌套滚动选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### PARALLEL

```cangjie
PARALLEL
```

**功能：** 自身和父组件同时滚动，自身和父组件都到达边缘以后，如果自身有边缘效果，则自身触发边缘效果，否则父组件触发边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### PARENT_FIRST

```cangjie
PARENT_FIRST
```

**功能：** 父组件先滚动，父组件滚动到边缘以后自身滚动。自身滚动到边缘后，如果有边缘效果，会触发自身的边缘效果，否则触发父组件的边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### SELF_FIRST

```cangjie
SELF_FIRST
```

**功能：** 自身先滚动，自身滚动到边缘以后父组件滚动。父组件滚动到边缘以后，如果父组件有边缘效果，则父组件触发边缘效果，否则子组件触发边缘效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### SELF_ONLY

```cangjie
SELF_ONLY
```

**功能：** 只自身滚动，不与父组件联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum ObscuredReasons

```cangjie
public enum ObscuredReasons {
    | PLACEHOLDER
}
```

**功能：** 显示的数据为通用占位符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### PLACEHOLDER

```cangjie
PLACEHOLDER
```

**功能：** 显示的数据为通用占位符。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum OptionWidthMode

```cangjie
public enum OptionWidthMode {
    | FIT_CONTENT
    | FIT_TRIGGER
}
```

**功能：** 下拉菜单宽度设置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### FIT_CONTENT

```cangjie
FIT_CONTENT
```

**功能：** 设置该值时，下拉菜单宽度按默认2栅格显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### FIT_TRIGGER

```cangjie
FIT_TRIGGER
```

**功能：** 设置下拉菜单继承下拉按钮宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum OutlineStyle

```cangjie
public enum OutlineStyle {
    | SOLID
    | DASHED
    | DOTTED
}
```

**功能：** 外描边样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DASHED

```cangjie
DASHED
```

**功能：** 显示为一系列短的方形虚线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### DOTTED

```cangjie
DOTTED
```

**功能：** 显示为一系列圆点，圆点半径为outlineWidth的一半。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### SOLID

```cangjie
SOLID
```

**功能：** 显示为一条实线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum PixelRoundCalcPolicy

```cangjie
public enum PixelRoundCalcPolicy {
    | NO_FORCE_ROUND
    | FORCE_CEIL
    | FORCE_FLOOR
}
```

**功能：** 当前组件边界取整策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### FORCE_CEIL

```cangjie
FORCE_CEIL
```

**功能：** 取上整计算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### FORCE_FLOOR

```cangjie
FORCE_FLOOR
```

**功能：** 取下整计算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### NO_FORCE_ROUND

```cangjie
NO_FORCE_ROUND
```

**功能：** 不取整计算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19