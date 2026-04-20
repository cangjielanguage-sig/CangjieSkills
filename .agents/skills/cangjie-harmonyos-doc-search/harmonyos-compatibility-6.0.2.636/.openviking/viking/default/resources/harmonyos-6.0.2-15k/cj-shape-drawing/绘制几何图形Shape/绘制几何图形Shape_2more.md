# 绘制几何图形（Shape）

绘制组件用于在页面绘制图形，Shape组件是绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。具体用法请参考[Shape](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-shape.md)。

## 创建绘制组件

绘制组件可以由以下两种形式创建：

- 绘制组件使用Shape作为父组件，实现类似SVG的效果。接口调用为以下形式：

  ```cangjie
  init()

  init(target: PixelMap)
  ```

  该接口用于创建带有父组件的绘制组件，其中target用于设置绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则在当前绘制目标中进行绘制。

  ```cangjie
  Shape() {
      Rect().width(300).height(50)
  }
  ```

- 绘制组件单独使用，用于在页面上绘制指定的图形。有7种绘制类型，分别为[Circle](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-circle.md)（圆形）、[Ellipse](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-ellipse.md)（椭圆形）、[Line](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-line.md)（直线）、[Polyline](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-polyline.md)（折线）、[Polygon](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-polygon.md)（多边形）、[Path](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-path.md)（路径）、[Rect](../../API_Reference/source_zh_cn/arkui-cj/cj-graphic-drawing-rect.md)（矩形）。以Circle的接口调用为例：

  ```cangjie
  Circle()

  Circle(width!: Length, height!: Length)
  ```

  该接口用于在页面绘制圆形，其中width用于设置圆形的宽度，height用于设置圆形的高度，圆形直径由宽高最小值确定。

  ```cangjie
  Circle(width: 150, height: 150)
  ```

  ![create2](figures/create2.jpg)