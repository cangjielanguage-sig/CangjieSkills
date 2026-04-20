## class WindowFilter

```cangjie
public class WindowFilter {
    public var bundleName:?String
    public var title:?String
    public var focused:?Bool
    public var active:?Bool
    public var displayId:?Int32
    public init(bundleName!: ?String = None, title!: ?String = None, focused!: ?Bool = None, active!: ?Bool = None, displayId!: ?Int32 = None)
}
```

**功能：** 窗口的标志属性信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var active

```cangjie
public var active:?Bool
```

**功能：** 窗口是否正与用户进行交互，true：交互状态，false：未交互状态。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var bundleName

```cangjie
public var bundleName:?String
```

**功能：** 窗口归属应用的包名。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var displayId

```cangjie
public var displayId:?Int32
```

**功能：** 窗口所属的屏幕ID。取值大于或等于0的整数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var focused

```cangjie
public var focused:?Bool
```

**功能：** 窗口是否处于获焦状态，true：获焦状态，false：未获焦状态。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var title

```cangjie
public var title:?String
```

**功能：** 窗口的标题信息。

**类型：** ?String

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### init(?String, ?String, ?Bool, ?Bool, ?Int32)

```cangjie
public init(bundleName!: ?String = None, title!: ?String = None, focused!: ?Bool = None, active!: ?Bool = None, displayId!: ?Int32 = None)
```

**功能：** 创建[WindowFilter](#class-windowfilter)实例。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|?String|否|None| **命名参数。** 窗口归属应用的包名，默认值为空。|
|title|?String|否|None| **命名参数。** 窗口的标题信息，默认值为空。|
|focused|?Bool|否|None| **命名参数。** 窗口是否处于获焦状态，true：获焦状态，false：未获焦状态，默认值为false。|
|active|?Bool|否|None| **命名参数。** 窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。|
|displayId|?Int32|否|None| **命名参数。** 窗口所属的屏幕ID。取值大于或等于0的整数。默认值为设备默认屏ID。|