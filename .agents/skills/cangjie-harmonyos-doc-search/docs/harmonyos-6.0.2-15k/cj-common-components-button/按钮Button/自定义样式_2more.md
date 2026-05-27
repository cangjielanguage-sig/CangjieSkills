## 自定义样式

- 设置边框弧度。

    使用通用属性来自定义按钮样式。例如通过borderRadius属性设置按钮的边框弧度。

    ```cangjie
    Button('circle border', ButtonOptions(shape: ButtonType.Normal))
        .borderRadius(20)
        .height(40)
    ```

    ![Button6](figures/Button6.png)

- 设置文本样式。

    通过添加文本样式设置按钮文本的展示样式。

    ```cangjie
    Button('font style', ButtonOptions(shape: ButtonType.Normal))
        .fontSize(20)
        .fontColor(Color.PINK)
        .fontWeight(W800)
    ```

    ![Button7](figures/Button7.png)

- 设置背景颜色。

    添加backgroundColor属性设置按钮的背景颜色。

    ```cangjie
    Button('background color').backgroundColor(0xF55A42)
    ```

    ![Button8](figures/Button8.png)

- 创建功能型按钮。

    为删除操作创建一个按钮。

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

Button组件通常用于触发某些操作，可以绑定onClick事件来响应点击操作后的自定义行为。

```cangjie
Button('Ok', ButtonOptions(shape: ButtonType.Normal, stateEffect: true))
    .onClick{ evt =>
    AppLog.info('Button onClick')
}
```