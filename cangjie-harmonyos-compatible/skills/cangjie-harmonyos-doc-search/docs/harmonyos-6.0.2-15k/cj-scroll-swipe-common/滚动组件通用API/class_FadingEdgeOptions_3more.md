## class FadingEdgeOptions

```cangjie
public class FadingEdgeOptions {
    public FadingEdgeOptions(
        public var fadingEdgeLength!: Length = 32.vp
    )
}
```

**功能：** 边缘渐隐参数对象。可以通过该对象定义边缘渐隐效果属性，比如设置渐隐长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var fadingEdgeLength

```cangjie
public var fadingEdgeLength: Length = 32.vp
```

**功能：** 边缘渐隐长度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**起始版本：** 19

### FadingEdgeOptions(Length)

```cangjie
public FadingEdgeOptions(
    public var fadingEdgeLength!: Length = 32.vp
)
```

**功能：** 创建FadingEdgeOptions对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fadingEdgeLength|[Length](./cj-common-types.md#interface-length)|否|32.vp| **命名参数。** 边缘渐隐长度。如果设置小于0的值则取默认值。默认长度为32.vp。<br/>如果设置的长度超过容器高度的一半时，渐隐长度取容器高度的一半。|

## class NestedScrollOptions

```cangjie
public class NestedScrollOptions {
    public NestedScrollOptions(
        public var scrollForward: NestedScrollMode,
        public var scrollBackward: NestedScrollMode
    )
}
```

**功能：** 可滚动组件滚动时的嵌套滚动参数对象。可以通过该对象定义嵌套滚动效果属性，比如设置往末尾端滚动时的嵌套滚动选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var scrollBackward

```cangjie
public var scrollBackward: NestedScrollMode
```

**功能：** 滚动组件往起始端滚动时的嵌套滚动选项。

**类型：** [NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)

**读写能力：** 可读写

**起始版本：** 12

### var scrollForward

```cangjie
public var scrollForward: NestedScrollMode
```

**功能：** 滚动组件往末尾端滚动时的嵌套滚动选项。

**类型：** [NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)

**读写能力：** 可读写

**起始版本：** 12

### NestedScrollOptions(NestedScrollMode, NestedScrollMode)

```cangjie
public NestedScrollOptions(
    public var scrollForward: NestedScrollMode,
    public var scrollBackward: NestedScrollMode
)
```

**功能：** 创建一个NestedScrollOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scrollForward|[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|是|-|滚动组件往末尾端滚动时的嵌套滚动选项。|
|scrollBackward|[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|是|-|滚动组件往起始端滚动时的嵌套滚动选项。|

## class ItemDragInfo

```cangjie
public class ItemDragInfo {
    public ItemDragInfo (
        public let x: Float64,
        public let y: Float64
    )
}
```

**功能：** 拖拽点的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let x

```cangjie
public let x: Float64
```

**功能：** 当前拖拽点的x坐标，单位vp。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### let y

```cangjie
public let y: Float64
```

**功能：** 当前拖拽点的y坐标，单位vp。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

### ItemDragInfo(Float64, Float64)

```cangjie
public ItemDragInfo (
        public let x: Float64,
        public let y: Float64
    )
```

**功能：** 构造一个ItemDragInfo对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|当前拖拽点的x坐标，单位vp。|
|y|Float64|是|-|当前拖拽点的y坐标，单位vp。|