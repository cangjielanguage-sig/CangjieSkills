### class ImageLoadResult

```cangjie
public class ImageLoadResult {
    public var width: Float64
    public var height: Float64
    public var componentWidth: Float64
    public var componentHeight: Float64
    public var loadingStatus: Int32
    public var contentWidth: Float64
    public var contentHeight: Float64
    public var contentOffsetX: Float64
    public var contentOffsetY: Float64
}
```

**功能：** 图片加载成功类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var componentHeight

```cangjie
public var componentHeight: Float64
```

**功能：** 组件的高度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var componentWidth

```cangjie
public var componentWidth: Float64
```

**功能：** 组件的宽度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var contentHeight

```cangjie
public var contentHeight: Float64
```

**功能：** 图片实际绘制的高度，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var contentOffsetX

```cangjie
public var contentOffsetX: Float64
```

**功能：** 实际绘制内容相对于组件自身的x轴偏移，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var contentOffsetY

```cangjie
public var contentOffsetY: Float64
```

**功能：** 实际绘制内容相对于组件自身的y轴偏移，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var contentWidth

```cangjie
public var contentWidth: Float64
```

**功能：** 图片实际绘制的宽度，单位为px。

> **说明：**
>
> 仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var height

```cangjie
public var height: Float64
```

**功能：** 图片的高度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var loadingStatus

```cangjie
public var loadingStatus: Int32
```

**功能：** 图片加载成功的状态。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var width

```cangjie
public var width: Float64
```

**功能：** 图片的宽度，单位为px。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22