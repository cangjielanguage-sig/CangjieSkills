### class BorderImageOption

```cangjie
public class BorderImageOption {
    public BorderImageOption (
        public let source!: BorderImageOptionSourceType,
        public let slice!: LengthEdgeWidthsType = LengthType.vp(0.0),
        public let width!: LengthEdgeWidthsType = LengthType.vp(0.0),
        public let outset!: LengthEdgeWidthsType = LengthType.vp(0.0),
        public let repeat!: RepeatMode = RepeatMode.STRETCH,
        public let fill!: Bool = false
    )
}
```

**功能：** 图片边框或者渐变色边框配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let source

```cangjie
public let source: BorderImageOptionSourceType
```

**功能：** 边框图源或者渐变色设置。参数类型为string类型时，用于设置边框图源，引用方式请参考[加载图片资源](../../../Dev_Guide/arkui-cj/cj-graphics-display.md#加载图片资源)。

**类型：** [BorderImageOptionSourceType](#interface-borderimageoptionsourcetype)

**读写能力：** 只读

**起始版本：** 19

#### let slice

```cangjie
public let slice: LengthEdgeWidthsType = LengthType.vp(0.0)
```

**功能：** 设置边框图片的切割宽度。

**类型：** [LengthEdgeWidthsType](#interface-lengthedgewidthstype)

**读写能力：** 只读

**起始版本：** 19

#### let width

```cangjie
public let width: LengthEdgeWidthsType = LengthType.vp(0.0)
```

**功能：** 设置图片边框宽度。

**类型：** [LengthEdgeWidthsType](#interface-lengthedgewidthstype)

**读写能力：** 只读

**起始版本：** 19

#### let outset

```cangjie
public let outset: LengthEdgeWidthsType = LengthType.vp(0.0)
```

**功能：** 设置边框图片向外延伸距离。

**类型：** [LengthEdgeWidthsType](#interface-lengthedgewidthstype)

**读写能力：** 只读

**起始版本：** 19

#### let repeat

```cangjie
public let repeat: RepeatMode = RepeatMode.STRETCH
```

**功能：** 设置被切割的图片在边框上的重复方式。

**类型：** [RepeatMode](#enum-repeatmode)

**读写能力：** 只读

**起始版本：** 19

#### let fill

```cangjie
public let fill: Bool = false
```

**功能：** 设置边框图片是否中心填充。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19