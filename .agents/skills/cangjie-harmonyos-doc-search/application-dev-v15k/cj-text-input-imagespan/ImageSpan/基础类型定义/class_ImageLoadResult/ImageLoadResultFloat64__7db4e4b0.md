#### ImageLoadResult(Float64, Float64, Float64, Float64, Int64, Float64, Float64, Float64, Float64)

```cangjie
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
```

**功能：** 创建ImageLoadResult类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|图片的宽。单位：像素(px)。|
|height|Float64|是|-|图片的高。单位：像素(px)。|
|componentWidth|Float64|是|-|组件的宽。单位：像素(px)。|
|componentHeight|Float64|是|-|组件的高。单位：像素(px)。|
|loadingStatus|Int64|是|-|图片加载成功的状态值。返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。|
|contentWidth|Float64|是|-|图片实际绘制的宽度。单位：像素(px)。仅在loadingStatus返回1时有效。|
|contentHeight|Float64|是|-|图片实际绘制的高度。单位：像素(px)。仅在loadingStatus返回1时有效。|
|contentOffsetX|Float64|是|-|实际绘制内容相对于组件自身的x轴偏移。单位：像素(px)。仅在loadingStatus返回1时有效。|
|contentOffsetY|Float64|是|-|实际绘制内容相对于组件自身的y轴偏移。单位：像素(px)。仅在loadingStatus返回1时有效。|