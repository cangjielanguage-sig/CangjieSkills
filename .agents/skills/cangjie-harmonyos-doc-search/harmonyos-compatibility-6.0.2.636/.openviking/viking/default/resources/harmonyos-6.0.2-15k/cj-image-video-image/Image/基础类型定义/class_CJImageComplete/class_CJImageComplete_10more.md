### class CJImageComplete

```cangjie
public class CJImageComplete {
    public var width: Float64 = 0.0
    public var height: Float64 = 0.0
    public var componentWidth: Float64 = 0.0
    public var componentHeight: Float64 = 0.0
    public var loadingStatus: Int32 = 0
    public var contentWidth: Float64 = 0.0
    public var contentHeight: Float64 = 0.0
    public var contentOffsetX: Float64 = 0.0
    public var contentOffsetY: Float64 = 0.0

    public init(
        width: Float64,
        height: Float64,
        componentWidth: Float64,
        componentHeight: Float64,
        loadingStatus: Int32
    )
    public init(
        width: Float64,
        height: Float64,
        componentWidth: Float64,
        componentHeight: Float64,
        loadingStatus: Int32,
        contentWidth: Float64,
        contentHeight: Float64,
        contentOffsetX: Float64,
        contentOffsetY: Float64
    )
    public init()
}
```

**功能：** 图片加载成功类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var componentHeight

```cangjie
public var componentHeight: Float64 = 0.0
```

**功能：** 组件的高度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var componentWidth

```cangjie
public var componentWidth: Float64 = 0.0
```

**功能：** 组件的宽度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var contentHeight

```cangjie
public var contentHeight: Float64 = 0.0
```

**功能：** 图片实际绘制的高度，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var contentOffsetX

```cangjie
public var contentOffsetX: Float64 = 0.0
```

**功能：** 实际绘制内容相对于组件自身的x轴偏移，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var contentOffsetY

```cangjie
public var contentOffsetY: Float64 = 0.0
```

**功能：** 实际绘制内容相对于组件自身的y轴偏移，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var contentWidth

```cangjie
public var contentWidth: Float64 = 0.0
```

**功能：** 图片实际绘制的宽度，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var height

```cangjie
public var height: Float64 = 0.0
```

**功能：** 图片的高度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var loadingStatus

```cangjie
public var loadingStatus: Int32 = 0
```

**功能：** 图片加载成功的状态。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var width

```cangjie
public var width: Float64 = 0.0
```

**功能：** 图片的宽度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12