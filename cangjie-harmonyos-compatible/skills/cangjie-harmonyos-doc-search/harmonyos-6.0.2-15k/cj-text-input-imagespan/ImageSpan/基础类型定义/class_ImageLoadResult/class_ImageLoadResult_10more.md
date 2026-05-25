### class ImageLoadResult

```cangjie
public class ImageLoadResult {
    public ImageLoadResult(
        public var width: Float64,
        public var height: Float64,
        public var componentWidth: Float64,
        public var componentHeight: Float64,
        public var loadingStatus: Int64,
        public var contentWidth: Float64,
        public var contentHeight: Float64,
        public var contentOffsetX: Float64,
        public var contentOffsetY: Float64
    )
}
```

**功能：** 图片加载成功类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var componentHeight

```cangjie
public var componentHeight: Float64
```

**功能：** 表示组件的高。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var componentWidth

```cangjie
public var componentWidth: Float64
```

**功能：** 表示组件的宽。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var contentHeight

```cangjie
public var contentHeight: Float64
```

**功能：** 表示图片实际绘制的高度。仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var contentOffsetX

```cangjie
public var contentOffsetX: Float64
```

**功能：** 表示实际绘制内容相对于组件自身的x轴偏移。仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var contentOffsetY

```cangjie
public var contentOffsetY: Float64
```

**功能：** 表示实际绘制内容相对于组件自身的y轴偏移。仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var contentWidth

```cangjie
public var contentWidth: Float64
```

**功能：** 表示图片实际绘制的宽度。仅在loadingStatus返回1时有效。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var height

```cangjie
public var height: Float64
```

**功能：** 表示图片的高。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12

#### var loadingStatus

```cangjie
public var loadingStatus: Int64
```

**功能：** 表示图片加载成功的状态值。

> **说明：**
>
> 返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

#### var width

```cangjie
public var width: Float64
```

**功能：** 表示图片的宽。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 12