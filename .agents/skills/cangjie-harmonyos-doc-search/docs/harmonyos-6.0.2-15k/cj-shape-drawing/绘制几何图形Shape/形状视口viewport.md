## 形状视口viewport

```cangjie
viewPort(x!: Length, y!: Length, width!: Length, height!: Length)
```

形状视口viewport指定用户空间中的一个矩形，该矩形映射到为关联的SVG元素建立的视区边界。viewport属性的值包含x、y、width和height四个可选参数，x和y表示视区的左上角坐标，width和height表示其尺寸。

以下3个示例讲解viewport具体用法：

- 通过形状视口对图形进行放大与缩小。

<!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      func build() {
          Column() {
              Row() {
                  Column {
                      // 画一个宽高都为75的圆
                      Text('原始尺寸Circle组件')
                      Circle(width: 75, height: 75).fill(0XE87361)
                  }
              }
              Row() {
                  Column {
                      // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为75的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个直径为75的圆。
                      // 绘制结束，viewport会根据组件宽高放大两倍
                      Text('shape内放大的Circle组件')
                      Shape() {
                          Rect().width(100.percent).height(100.percent).fill(0X0097D4)
                          Circle(width: 75, height: 75).fill(0XE87361)
                      }.viewPort(x: 0, y: 0, width: 75, height: 75).width(150).height(150).backgroundColor(0XF5DC62)
                  }
                  Column {
                      // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为300的viewport。用一个绿色的矩形来填充viewport，在viewport中绘制一个直径为75的圆。
                      // 绘制结束，viewport会根据组件宽高缩小两倍。
                      Text('Shape内缩小的Circle组件')
                      Shape() {
                          Rect().width(100.percent).height(100.percent).fill(0XBDDB69)
                          Circle(width: 75, height: 75).fill(0XE87361)
                      }.viewPort(x: 0, y: 0, width: 300, height: 300).width(150).height(150).backgroundColor(0XF5DC62)
                  }
              }
          }.width(100.percent)
      }
  }
  ```

  ![drawing2](figures/drawing2.jpg)

- 创建一个宽高都为300的shape组件，背景色为黄色，一个宽高都为300的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个半径为75的圆。

<!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      func build() {
          Column() {
              Shape() {
                  Rect().width(100.percent).height(100.percent).fill(0X0097D4)
                  Circle(width: 150, height: 150).fill(0XE87361)
              }.viewPort(x: 0, y: 0, width: 300, height: 300).width(300).height(300).backgroundColor(0XF5DC62)
          }.width(100.percent)
      }
  }
  ```

  ![viewport_2](figures/viewport_2.jpg)

- 创建一个宽高都为300的shape组件，背景色为黄色，创建一个宽高都为300的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个半径为75的圆，将viewport向右方和下方各平移150。

<!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      func build() {
          Column() {
              Shape() {
                  Rect().width(100.percent).height(100.percent).fill(0X0097D4)
                  Circle(width: 150, height: 150).fill(0XE87361)
              }.viewPort(x: -150, y: -150, width: 300, height: 300).width(300).height(300).backgroundColor(0XF5DC62)
          }.width(100.percent)
      }
  }
  ```

  ![viewport_3](figures/viewport_3.jpg)