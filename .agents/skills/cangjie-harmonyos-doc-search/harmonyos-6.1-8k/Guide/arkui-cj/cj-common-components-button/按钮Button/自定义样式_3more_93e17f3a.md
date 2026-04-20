## 自定义样式

- 设置边框弧度。

  使用通用属性来自定义按钮样式。例如通过[borderRadius](../reference/arkui-cj/cj-common-types.md#class-borderradiuses)属性设置按钮的边框弧度。

  <!-- code_check_manual -->

  ```cangjie
  Button('circle border', ButtonOptions(shape: ButtonType.Normal))
      .borderRadius(20)
      .height(40)
  ```

  ![Button6](figures/Button6.png)

- 设置文本样式。

  通过添加文本样式设置按钮文本的展示样式。

  <!-- code_check_manual -->

  ```cangjie
  Button('font style', ButtonOptions(shape: ButtonType.Normal))
      .fontSize(20)
      .fontColor(0xffffc0cb)
  ```

  ![Button7](figures/Button7.png)

- 设置背景颜色。

  添加[backgroundColor](../reference/arkui-cj/cj-universal-attribute-background.md#func-backgroundcolorresourcecolor)属性设置按钮的背景颜色。

  <!-- code_check_manual -->

  ```cangjie
  Button('background color').backgroundColor(0xF55A42)
  ```

  ![Button8](figures/Button8.png)

- 创建功能型按钮。

  为删除操作创建一个按钮。

  <!-- code_check_manual -->

  ```cangjie
  Button(ButtonOptions(shape: ButtonType.Circle, stateEffect: true)) {
      Image(@r(app.media.ic_public_delete_filled))
        .width(30)
        .height(30)
  }
  .width(55)
  .height(55)
  .margin(left:20)
  .backgroundColor(0xF55A42)
  ```

  ![Button9](figures/Button9.png)

## 添加事件

Button组件通常用于触发某些操作，可以绑定[onClick](../reference/arkui-cj/cj-universal-event-click.md#func-onclickclickevent---unit)事件来响应点击操作后的自定义行为。

<!-- code_check_manual -->

```cangjie
  Button('Ok', ButtonOptions(shape: ButtonType.Normal, stateEffect: true))
      .onClick({ evt =>
      Hilog.info(0, '', 'Button onClick')
  })
```

## 场景示例

- 用于提交表单。

  在用户登录/注册页面，使用按钮进行登录或注册操作。

     <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry
  import kit.ArkUI.*
  import ohos.arkui.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      func build() {
          Column() {
              TextInput(placeholder: 'input your username')
                .margin(top: 20)
              TextInput(placeholder: 'input your password')
                .margin(top: 20)
              Button('Register')
                .width(300)
                .margin(top: 20)
                .onClick({ evt =>
                    // 需要执行的操作
                    })
          }
          .padding(20)
      }
  }
  ```

  ![Button10](figures/Button10.png)

- 悬浮按钮。

  在可以滑动的界面，滑动时按钮始终保持悬浮状态。

     <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry
  import kit.ArkUI.*
  import ohos.arkui.state_macro_manage.*
  import kit.LocalizationKit.AppResource
  import ohos.resource.__GenerateResource__

  @Entry
  @Component
  class EntryView {
      private var arr: Array<Int64> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
      func build() {
          Stack() {
              List(space: 20, initialIndex: 0) {
                  ForEach(
                      this.arr,
                      itemGeneratorFunc: {
                          item: Int64, _: Int64 => ListItem() {
                              Text("${item}")
                                  .width(100.percent)
                                  .height(100)
                                  .fontSize(16)
                                  .textAlign(TextAlign.Center)
                                  .borderRadius(10)
                                  .backgroundColor(0xFFFFFF)
                          }
                      }
                  )
              }.width(90.percent)

              Button() {
                  Image(@r(app.media.startIcon))
                      .width(50)
                      .height(50)
              }
              .shape(ButtonType.Circle)
              .width(60)
              .height(60)
              .position(x: 80.percent, y: 600)
              .shadow(radius: 10.0)
              .onClick ({
                  evt =>
                  // 需要执行的操作
              })
          }
          .width(100.percent)
          .height(100.percent)
          .backgroundColor(0xDCDCDC)
          .padding(top: 5)
      }
  }
  ```

  ![floating_button](figures/floating_button.gif)