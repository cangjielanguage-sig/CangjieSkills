## class Point

```cangjie
public class Point {
    public var x: Int32
    public var y: Int32
    public var displayId:?Int32
    public init(x: Int32, y: Int32, displayId!: ?Int32 = None)
}
```

**功能：** 坐标点信息。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var displayId

```cangjie
public var displayId:?Int32
```

**功能：** 坐标点所属的屏幕ID，取值范围：大于等于0的整数。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var x

```cangjie
public var x: Int32
```

**功能：** 坐标点的横坐标，取值大于0的整数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### var y

```cangjie
public var y: Int32
```

**功能：** 坐标点的纵坐标，取值大于0的整数。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

### init(Int32, Int32, ?Int32)

```cangjie
public init(x: Int32, y: Int32, displayId!: ?Int32 = None)
```

**功能：** 创建Point实例。

**系统能力：** SystemCapability.Test.UiTest

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Int32|是|-|坐标点的横坐标，取值大于0的整数。|
|y|Int32|是|-|坐标点的纵坐标，取值大于0的整数。|
|displayId|?Int32|否|None| **命名参数。** 坐标点所属的屏幕ID，取值范围：大于等于0的整数。默认值为设备默认屏幕ID。|