## class Margin

```cangjie
public class Margin {
    public init(top!: Length = 0.vp, right!: Length = 0.vp, bottom!: Length = 0.vp, left!: Length = 0.vp)
}
```

**功能：** 外边距类型，用于描述组件不同方向的外边距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Length, Length, Length, Length)

```cangjie
public init(top!: Length = 0.vp, right!: Length = 0.vp, bottom!: Length = 0.vp, left!: Length = 0.vp)
```

**功能：** 初始化了一个外边距类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 上外边距，组件顶部距组件外元素的尺寸。<br/>初始值：0.vp。|
|right|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 右外边距，组件右边界距组件外元素的尺寸。<br/>初始值：0.vp。|
|bottom|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 下外边距，组件底部距组件外元素的尺寸。<br/>初始值：0.vp。|
|left|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 左外边距，组件左边界距组件外元素的尺寸。<br/>初始值：0.vp。|

## class MenuOffset

```cangjie
public class MenuOffset {
    public var dx: Length
    public var dy: Length
    public init(dx: Length, dy: Length)
}
```

**功能：** 位置坐标偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var dx

```cangjie
public var dx: Length
```

**功能：** 水平方向偏移量。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var dy

```cangjie
public var dy: Length
```

**功能：** 竖直方向偏移量。

**类型：** [Length](./cj-common-types.md#interface-length)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## class Offset

```cangjie
public class Offset {
    public var dx: Length
    public var dy: Length
    public init(dx: Length,  dy: Length)
}
```

**功能：** 相对布局完成位置坐标偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var dx

```cangjie
public var dx: Length
```

**功能：** 水平方向偏移量。

**类型：** [Length](#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var dy

```cangjie
public var dy: Length
```

**功能：** 竖直方向偏移量。

**类型：** [Length](#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(Length, Length)

```cangjie
public init(dx: Length,  dy: Length)
```

**功能：** 构建一个Offset类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dx|[Length](#interface-length)|是|-|x点坐标。|
|dy|[Length](#interface-length)|是|-|y点坐标。|