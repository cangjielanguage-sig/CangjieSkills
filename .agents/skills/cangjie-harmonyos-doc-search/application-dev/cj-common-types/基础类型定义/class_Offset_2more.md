## class Offset

```cangjie
public class Offset {
    public var dx: ?Length
    public var dy: ?Length
    public init(dx: ?Length, dy: ?Length)
}
```

**功能：** 相对布局完成位置坐标偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var dx

```cangjie
public var dx: ?Length
```

**功能：** 水平方向偏移量。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var dy

```cangjie
public var dy: ?Length
```

**功能：** 竖直方向偏移量。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Length, ?Length)

```cangjie
public init(dx: ?Length, dy: ?Length)
```

**功能：** 构建一个Offset类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dx|?[Length](./cj-common-types.md#interface-length)|是|-|x点坐标。|
|dy|?[Length](./cj-common-types.md#interface-length)|是|-|y点坐标。|

## class ExpectedFrameRateRange

```cangjie
public class ExpectedFrameRateRange {
    public var min: ?Int32
    public var max: ?Int32
    public var expected: ?Int32
    public init(min!: ?Int32, max!: ?Int32, expected!: ?Int32)
}
```

**功能：** 设置动画的期望帧率范围。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var min

```cangjie
public var min: ?Int32
```

**功能：** 最小帧率值。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var max

```cangjie
public var max: ?Int32
```

**功能：** 最大帧率值。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var expected

```cangjie
public var expected: ?Int32
```

**功能：** 期望的帧率值。

**类型：** ?Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?Int32, ?Int32, ?Int32)

```cangjie
public init(min!: ?Int32, max!: ?Int32, expected!: ?Int32)
```

**功能：** 构造一个ExpectedFrameRateRange对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|min|?Int32|是|-|**命名参数。** 最小帧率值。|
|max|?Int32|是|-|**命名参数。** 最大帧率值。|
|expected|?Int32|是|-|**命名参数。** 期望的帧率值。|