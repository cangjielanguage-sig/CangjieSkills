# CanvasRenderingContext2D

使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。

> **说明**
>
> - 本文绘制接口在调用时会存入被关联的Canvas组件的指令队列中。仅在当前帧进入渲染阶段且关联的Canvas组件处于可见状态时，这些指令才会从队列中被提取并执行。因此，在Canvas组件不可见的情况下，应尽量避免频繁调用绘制接口，以防止指令在队列中堆积，从而避免内存占用过大的问题。
> - Canvas组件的宽或高超过8000px时使用CPU渲染，会导致性能明显下降。

## 导入模块

```cangjie
import kit.UIKit.*
```