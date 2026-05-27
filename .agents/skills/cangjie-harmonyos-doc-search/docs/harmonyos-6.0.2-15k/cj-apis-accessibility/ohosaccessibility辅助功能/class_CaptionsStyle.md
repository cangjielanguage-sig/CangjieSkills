## class CaptionsStyle

```cangjie
public class CaptionsStyle {
    public CaptionsStyle(
        public var fontFamily: CaptionsFontFamily,
        public var fontScale: Int32,
        public var fontColor: UInt32,
        public var fontEdgeType: CaptionsFontEdgeType,
        public var backgroundColor: UInt32,
        public var windowColor: UInt32
    )
}
```

**功能：** 字幕风格。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**起始版本：** 19

### var backgroundColor

```cangjie
public var backgroundColor: UInt32
```

**功能：** 描述字幕背景颜色，例如red对应#FF0000。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var fontColor

```cangjie
public var fontColor: UInt32
```

**功能：** 描述字幕字体颜色，例如red对应#FF0000。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var fontEdgeType

```cangjie
public var fontEdgeType: CaptionsFontEdgeType
```

**功能：** 描述字幕字体边缘。

**类型：** [CaptionsFontEdgeType](#enum-captionsfontedgetype)

**读写能力：** 可读写

**起始版本：** 19

### var fontFamily

```cangjie
public var fontFamily: CaptionsFontFamily
```

**功能：** 描述字幕字体。

**类型：** [CaptionsFontFamily](#enum-captionsfontfamily)

**读写能力：** 可读写

**起始版本：** 19

### var fontScale

```cangjie
public var fontScale: Int32
```

**功能：** 描述字幕字体缩放系数，单位%，参数范围1~200。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var windowColor

```cangjie
public var windowColor: UInt32
```

**功能：** 描述字幕窗口颜色，例如red对应#FF0000。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### CaptionsStyle(CaptionsFontFamily, Int32, UInt32, CaptionsFontEdgeType, UInt32, UInt32)

```cangjie
public CaptionsStyle(
    public var fontFamily: CaptionsFontFamily,
    public var fontScale: Int32,
    public var fontColor: UInt32,
    public var fontEdgeType: CaptionsFontEdgeType,
    public var backgroundColor: UInt32,
    public var windowColor: UInt32
)
```

**功能：** CaptionsStyle的构造函数。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontFamily|[CaptionsFontFamily](#enum-captionsfontfamily)|是|-|描述字幕字体。|
|fontScale|Int32|是|-|描述字幕字体缩放系数，单位%，参数范围1~200。|
|fontColor|UInt32|是|-|描述字幕字体颜色，例如red对应#FF0000。|
|fontEdgeType|[CaptionsFontEdgeType](#enum-captionsfontedgetype)|是|-|描述字幕字体边缘。|
|backgroundColor|UInt32|是|-|描述字幕背景颜色，例如red对应#FF0000。|
|windowColor|UInt32|是|-|描述字幕窗口颜色，例如red对应#FF0000。|