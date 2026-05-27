## enum ListenerType

```cangjie
public enum ListenerType <: ToString {
    | LISTNER_TYPE_ADD
    | LISTNER_TYPE_REMOVE
    | LISTNER_TYPE_CHANGE
    | LISTNER_TYPE_FOLD_STATUS_CHANGE
    | LISTNER_TYPE_FOLD_ANGLE_CHANGE
    | LISTNER_TYPE_CAPTURE_STATUS_CHANGE
    | LISTNER_TYPE_FOLD_DISPLAY_MODE_CHANGE
    | LISTNER_TYPE_AVAILABLE_AREA_CHANGE
    | ...
}
```

**功能：** 设置监听事件类型。

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 19

### LISTNER_TYPE_ADD

```cangjie
LISTNER_TYPE_ADD
```

**功能：** 表示增加显示设备事件。

**起始版本：** 19

### LISTNER_TYPE_AVAILABLE_AREA_CHANGE

```cangjie
LISTNER_TYPE_AVAILABLE_AREA_CHANGE
```

**功能：** 表示折叠设备屏幕显示模式发生变化。

**起始版本：** 19

### LISTNER_TYPE_CAPTURE_STATUS_CHANGE

```cangjie
LISTNER_TYPE_CAPTURE_STATUS_CHANGE
```

**功能：** 表示设备截屏、投屏或者录屏状态发生变化。

**起始版本：** 19

### LISTNER_TYPE_CHANGE

```cangjie
LISTNER_TYPE_CHANGE
```

**功能：** 表示改变显示设备事件。

**起始版本：** 19

### LISTNER_TYPE_FOLD_ANGLE_CHANGE

```cangjie
LISTNER_TYPE_FOLD_ANGLE_CHANGE
```

**功能：** 表示折叠设备折叠角度发生变化。

**起始版本：** 19

### LISTNER_TYPE_FOLD_DISPLAY_MODE_CHANGE

```cangjie
LISTNER_TYPE_FOLD_DISPLAY_MODE_CHANGE
```

**功能：** 表示折叠设备屏幕显示模式发生变化。

**起始版本：** 19

### LISTNER_TYPE_FOLD_STATUS_CHANGE

```cangjie
LISTNER_TYPE_FOLD_STATUS_CHANGE
```

**功能：** 表示折叠设备折叠状态发生变化。

**起始版本：** 19

### LISTNER_TYPE_REMOVE

```cangjie
LISTNER_TYPE_REMOVE
```

**功能：** 表示移除显示设备事件。

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回枚举值字符串。

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值字符串。|

**示例:**

```cangjie
import ohos.display.*

let ret = ListenerType.LISTNER_TYPE_ADD.toString()
```