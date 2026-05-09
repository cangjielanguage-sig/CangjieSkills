## class CanvasRenderingContext2D

```cangjie
public class CanvasRenderingContext2D {
    public init(settings: ?RenderingContextSettings)
}
```

**功能：** Canvas组件的绘制上下文对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?RenderingContextSettings)

```cangjie
public init(settings: ?RenderingContextSettings)
```

**功能：** canvas绘制上下文对象的初始化函数，用于创建绘制上下文对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|settings|?[RenderingContextSettings](./cj-canvas-drawing-canvas.md#class-renderingcontextsettings)|是|-|初始化设置。|

### prop fillStyle

```cangjie
public mut prop fillStyle: Option<FillStyle>
```

**功能：** 指定绘制的填充色。

**类型：** Option\<[FillStyle](#interface-fillstyle)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop lineWidth

```cangjie
public mut prop lineWidth: Option<Float64>
```

**功能：** 线粗细属性。

**类型：** Option\<Float64>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop strokeStyle

```cangjie
public mut prop strokeStyle: Option<StrokeStyle>
```

**功能：** 设置描边的颜色。

**类型：** Option\<[StrokeStyle](#interface-strokestyle)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop lineCap

```cangjie
public mut prop lineCap: Option<String>
```

**功能：** 线段端点属性。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop lineJoin

```cangjie
public mut prop lineJoin: Option<String>
```

**功能：** 线段连接点属性。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop miterLimit

```cangjie
public mut prop miterLimit: Option<Float64>
```

**功能：** 设置斜接面限制值，该参数的值不能为0或负数。

**类型：** Option\<Float64>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop font

```cangjie
public mut prop font: Option<String>
```

**功能：** 设置字体样式。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop textAlign

```cangjie
public mut prop textAlign: Option<String>
```

**功能：** 文本对齐模式。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop textBaseline

```cangjie
public mut prop textBaseline: Option<String>
```

**功能：** 文本基线。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop globalAlpha

```cangjie
public mut prop globalAlpha: Option<Float64>
```

**功能：** 透明度。

**类型：** Option\<Float64>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop lineDashOffset

```cangjie
public mut prop lineDashOffset: Option<Float64>
```

**功能：** 虚线偏移属性。

**类型：** Option\<Float64>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### prop globalCompositeOperation

```cangjie
public mut prop globalCompositeOperation: Option<String>
```

**功能：** 绘制新形状时应用的合成操作类型。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22