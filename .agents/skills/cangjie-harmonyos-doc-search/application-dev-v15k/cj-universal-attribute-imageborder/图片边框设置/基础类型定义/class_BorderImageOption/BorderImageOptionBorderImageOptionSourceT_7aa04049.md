#### BorderImageOption(BorderImageOptionSourceType, LengthEdgeWidthsType, LengthEdgeWidthsType, LengthEdgeWidthsType, RepeatMode, Bool)

```cangjie
public BorderImageOption (
    public let source!: BorderImageOptionSourceType,
    public let slice!: LengthEdgeWidthsType = LengthType.vp(0.0),
    public let width!: LengthEdgeWidthsType = LengthType.vp(0.0),
    public let outset!: LengthEdgeWidthsType = LengthType.vp(0.0),
    public let repeat!: RepeatMode = RepeatMode.STRETCH,
    public let fill!: Bool = false
)
```

**功能：** 构造一个图片边框设置类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[BorderImageOptionSourceType](#interface-borderimageoptionsourcetype)|是| \- |边框图源或者渐变色设置。参数类型为string类型时，用于设置边框图源，引用方式请参考[加载图片资源](../../../Dev_Guide/arkui-cj/cj-graphics-display.md#加载图片资源)。<br/>**说明**：<br/>边框图源仅适用于容器组件，如[Row](./cj-row-column-stack-row.md)、[Column](./cj-row-column-stack-column.md)、[Flex](./cj-row-column-stack-flex.md)，在非容器组件上使用会失效。|
|slice|[LengthEdgeWidthsType](#interface-lengthedgewidthstype)|否|LengthType.vp(0.0)|设置边框图片左上角、右上角、左下角以及右下角的切割宽度。<br/>**说明**：<br/>设置负数时取默认值。<br/>参数类型为[Length](./cj-common-types.md#interface-length)时，统一设置四个角的宽高。<br/>参数类型为[EdgeWidths](./cj-universal-attribute-border.md#class-edgewidths)时：<br/>- Top：设置图片左上角或者右上角被切割的高。<br/>- Bottom：设置图片左下角或者右下角被切割的高。<br/>- Left：设置图片左上角或者左下角被切割的宽。<br/>- Right：设置图片右上角或者右下角被切割的宽。|
|width|[LengthEdgeWidthsType](#interface-lengthedgewidthstype)|否|LengthType.vp(0.0)|设置图片边框宽度。<br/>**说明**：<br/>参数类型为[Length](./cj-common-types.md#interface-length)时，统一设置四个角的宽高，设置负数时取默认值。<br/>参数类型为[EdgeWidths](./cj-universal-attribute-border.md#class-edgewidths)时：<br/>- Top：设置图片边框上边框的宽。<br/>- Bottom：设置图片边框下边框的宽。<br/>- Left：设置图片边框左边框的宽。<br/>- Right：设置图片边框右边框宽。|
|outset|[LengthEdgeWidthsType](#interface-lengthedgewidthstype)|否|LengthType.vp(0.0)|设置边框图片向外延伸距离。<br/>**说明**：<br/>设置负数时取默认值。<br/>参数类型为[Length](./cj-common-types.md#interface-length)时，统一设置四个角的宽高。<br/>参数类型为[EdgeWidths](./cj-universal-attribute-border.md#class-edgewidths)时：<br/>- Top：设置边框图片上边框向外延伸的距离。<br/>- Bottom：设置边框图片下边框向外延伸的距离。<br/>- Left：设置边框图片左边框向外延伸的距离。<br/>- Right：设置边框图片右边框向外延伸的距离。|
|repeat|[RepeatMode](#enum-repeatmode)|否|RepeatMode.STRETCH|设置被切割的图片在边框上的重复方式。|
|fill|Bool|否|false|设置边框图片是否中心填充。|