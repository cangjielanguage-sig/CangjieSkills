# CanvasRenderingContext2D

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。

> **说明**
>
> - 本文绘制接口在调用时会存入被关联的Canvas组件的指令队列中。仅在当前帧进入渲染阶段且关联的Canvas组件处于可见状态时，这些指令才会从队列中被提取并执行。因此，在Canvas组件不可见的情况下，应尽量避免频繁调用绘制接口，以防止指令在队列中堆积，从而避免内存占用过大的问题。
> - Canvas组件的宽或高超过8000px时使用CPU渲染，会导致性能明显下降。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## interface FillStyle

```cangjie
public interface FillStyle {}
```

**功能：** 填充样式接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### extend Int64 <: FillStyle

```cangjie
extend Int64 <: FillStyle {}
```

**功能：** 扩展Int64为FillStyle子类。

### extend UInt32 <: FillStyle

```cangjie
extend UInt32 <: FillStyle {}
```

**功能：** 扩展UInt32为FillStyle子类。

### extend Color <: FillStyle

```cangjie
extend Color <: FillStyle {}
```

**功能：** 扩展Color为FillStyle子类。

### extend CanvasGradient <: FillStyle

```cangjie
extend CanvasGradient <: FillStyle {}
```

**功能：** 扩展CanvasGradient为FillStyle子类。

### extend CanvasPattern <: FillStyle

```cangjie
extend CanvasPattern <: FillStyle {}
```

**功能：** 扩展CanvasPattern为FillStyle子类。

## interface StrokeStyle

```cangjie
public interface StrokeStyle {}
```

**功能：** 描边样式接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### extend Int64 <: StrokeStyle

```cangjie
extend Int64 <: StrokeStyle {}
```

**功能：** 扩展Int64为StrokeStyle子类。

### extend UInt32 <: StrokeStyle

```cangjie
extend UInt32 <: StrokeStyle {}
```

**功能：** 扩展UInt32为StrokeStyle子类。

### extend Color <: StrokeStyle

```cangjie
extend Color <: StrokeStyle {}
```

**功能：** 扩展Color为StrokeStyle子类。

### extend CanvasGradient <: StrokeStyle

```cangjie
extend CanvasGradient <: StrokeStyle {}
```

**功能：** 扩展CanvasGradient为StrokeStyle子类。

### extend CanvasPattern <: StrokeStyle

```cangjie
extend CanvasPattern <: StrokeStyle {}
```

**功能：** 扩展CanvasPattern为StrokeStyle子类。