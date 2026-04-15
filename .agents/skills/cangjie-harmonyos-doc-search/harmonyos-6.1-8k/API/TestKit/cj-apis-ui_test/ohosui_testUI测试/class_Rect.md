## class Rect

```cangjie
public class Rect {
    public var left: Int32
    public var top: Int32
    public var right: Int32
    public var bottom: Int32
    public var displayId:?Int32
    public init(left: Int32, top: Int32, right: Int32, bottom: Int32, displayId!: ?Int32 = None)
}
```

**功能：** 控件的边框信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var bottom

```cangjie
public var bottom: Int32
```

**功能：** 控件边框的右下角的Y坐标，取值大于0的整数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var displayId

```cangjie
public var displayId:?Int32
```

**功能：** 控件边框所属的屏幕ID，取值大于或等于0的整数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var left

```cangjie
public var left: Int32
```

**功能：** 控件边框的左上角的X坐标，取值大于0的整数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var right

```cangjie
public var right: Int32
```

**功能：** 控件边框的右下角的X坐标，取值大于0的整数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var top

```cangjie
public var top: Int32
```

**功能：** 控件边框的左上角的Y坐标，取值大于0的整数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### init(Int32, Int32, Int32, Int32, ?Int32)

```cangjie
public init(left: Int32, top: Int32, right: Int32, bottom: Int32, displayId!: ?Int32 = None)
```

**功能：** 创建[Rect](#class-rect)实例。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|left|Int32|是|-|控件边框的左上角的X坐标，取值大于0的整数。|
|top|Int32|是|-|控件边框的左上角的Y坐标，取值大于0的整数。|
|right|Int32|是|-|控件边框的右下角的X坐标，取值大于0的整数。|
|bottom|Int32|是|-|控件边框的右下角的Y坐标，取值大于0的整数。|
|displayId|?Int32|否|None| **命名参数。** 控件边框所属的屏幕ID，取值大于或等于0的整数。默认值为设备默认屏幕ID。|