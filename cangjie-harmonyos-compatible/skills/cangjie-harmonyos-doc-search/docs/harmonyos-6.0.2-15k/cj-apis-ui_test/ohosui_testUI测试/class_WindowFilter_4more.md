## class WindowFilter

```cangjie
public class WindowFilter {
    public WindowFilter(
        public let bundleName!: ?String = None,
        public let title!: ?String = None,
        public let focused!: ?Bool = None,
        public let active!: ?Bool = None
    )
}
```

**功能：** 窗口的属性信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### let active

```cangjie
public let active: ?Bool = None
```

**功能：** 窗口是否正与用户进行交互。

**类型：** ?Bool

**读写能力：** 只读

**起始版本：** 12

### let bundleName

```cangjie
public let bundleName: ?String = None
```

**功能：** 窗口归属应用的包名。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let focused

```cangjie
public let focused: ?Bool = None
```

**功能：** 窗口是否处于获焦状态。

**类型：** ?Bool

**读写能力：** 只读

**起始版本：** 12

### let title

```cangjie
public let title: ?String = None
```

**功能：** 窗口的标题信息。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### WindowFilter(?String, ?String, ?Bool, ?Bool)

```cangjie
public WindowFilter(
    public let bundleName!: ?String = None,
    public let title!: ?String = None,
    public let focused!: ?Bool = None,
    public let active!: ?Bool = None
)
```

**功能：** 创建[WindowFilter](#class-windowfilter)实例。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|?String|否|None| **命名参数。** 窗口归属应用的包名。|
|title|?String|否|None| **命名参数。** 窗口的标题信息。|
|focused|?Bool|否|None| **命名参数。** 窗口是否处于获焦状态。|
|active|?Bool|否|None| **命名参数。** 窗口是否正与用户进行交互。|

## enum DisplayRotation

```cangjie
public enum DisplayRotation {
    | ROTATION_0
    | ROTATION_90
    | ROTATION_180
    | ROTATION_270
    | ...
}
```

**功能：** 设备显示器的显示方向。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### ROTATION_0

```cangjie
ROTATION_0
```

**功能：** 设备显示器不旋转，初始形态垂直显示。

**起始版本：** 12

### ROTATION_180

```cangjie
ROTATION_180
```

**功能：** 设备显示器顺时针旋转180°，逆向垂直显示。

**起始版本：** 12

### ROTATION_270

```cangjie
ROTATION_270
```

**功能：** 设备显示器顺时针旋转270°，逆向水平显示。

**起始版本：** 12

### ROTATION_90

```cangjie
ROTATION_90
```

**功能：** 设备显示器顺时针旋转90°，水平显示。

**起始版本：** 12

## enum MatchPattern

```cangjie
public enum MatchPattern {
    | EQUALS
    | CONTAINS
    | STARTS_WITH
    | ENDS_WITH
    | ...
}
```

**功能：** 控件属性支持的匹配模式。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### CONTAINS

```cangjie
CONTAINS
```

**功能：** 包含给定值。

**起始版本：** 12

### ENDS_WITH

```cangjie
ENDS_WITH
```

**功能：** 以给定值结束。

**起始版本：** 12

### EQUALS

```cangjie
EQUALS
```

**功能：** 等于给定值。

**起始版本：** 12

### STARTS_WITH

```cangjie
STARTS_WITH
```

**功能：** 以给定值开始。

**起始版本：** 12

## enum MouseButton

```cangjie
public enum MouseButton {
    | MOUSE_BUTTON_LEFT
    | MOUSE_BUTTON_RIGHT
    | MOUSE_BUTTON_MIDDLE
    | ...
}
```

**功能：** 模拟注入的鼠标按钮。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 12

### MOUSE_BUTTON_LEFT

```cangjie
MOUSE_BUTTON_LEFT
```

**功能：** 鼠标左键。

**起始版本：** 12

### MOUSE_BUTTON_MIDDLE

```cangjie
MOUSE_BUTTON_MIDDLE
```

**功能：** 鼠标中间键。

**起始版本：** 12

### MOUSE_BUTTON_RIGHT

```cangjie
MOUSE_BUTTON_RIGHT
```

**功能：** 鼠标右键。

**起始版本：** 12