### class SurfaceRect

```cangjie
public class SurfaceRect {
    public var offsetX: Float32
    public var offsetY: Float32
    public var surfaceWidth: Float32
    public var surfaceHeight: Float32
    public init(offsetX: Float32, offsetY: Float32, surfaceWidth: Float32, surfaceHeight: Float32)
}
```

**功能：** 用于描述XComponent持有Surface的显示区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var offsetX

```cangjie
public var offsetX: Float32
```

**功能：** Surface显示区域相对于XComponent组件左上角的x轴坐标，单位：px。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var offsetY

```cangjie
public var offsetY: Float32
```

**功能：** Surface显示区域相对于XComponent组件左上角的y轴坐标，单位：px。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var surfaceHeight

```cangjie
public var surfaceHeight: Float32
```

**功能：** Surface显示区域的高度，单位：px。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var surfaceWidth

```cangjie
public var surfaceWidth: Float32
```

**功能：** Surface显示区域的宽度，单位：px。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float32, Float32, Float32, Float32)

```cangjie
public init(offsetX: Float32, offsetY: Float32, surfaceWidth: Float32, surfaceHeight: Float32)
```

**功能：** 创建SurfaceRect对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offsetX|Float32|是|-|Surface显示区域相对于XComponent组件左上角的x轴坐标，单位：px。|
|offsetY|Float32|是|-|Surface显示区域相对于XComponent组件左上角的y轴坐标，单位：px。|
|surfaceWidth|Float32|是|-|Surface显示区域的宽度，单位：px。|
|surfaceHeight|Float32|是|-|Surface显示区域的高度，单位：px。|

> **说明：**
>
> - surfaceWidth和surfaceHeight属性在未调用[setXComponentSurfaceRect](#func-setxcomponentsurfacerectsurfacerect)也未设置[border](cj-universal-attribute-border.md#func-borderlength-resourcecolor-length-borderstyle)和[padding](cj-universal-attribute-size.md#func-paddinglength)等属性时，其取值大小为XComponent组件的大小。
> - surfaceWidth和surfaceHeight属性的取值都不可超过8192.px，否则会导致渲染异常。