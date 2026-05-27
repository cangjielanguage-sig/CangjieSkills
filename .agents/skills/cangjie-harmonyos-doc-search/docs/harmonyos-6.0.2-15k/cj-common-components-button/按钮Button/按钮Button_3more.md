# 按钮（Button）

Button是按钮组件，通常用于响应用户的点击操作，其类型包括胶囊按钮、圆形按钮、普通按钮。Button做为容器使用时可以通过添加子组件实现包含文字、图片等元素的按钮。具体用法请参见[Button](../../API_Reference/source_zh_cn/arkui-cj/cj-button-picker-button.md)。

## 创建按钮

Button通过调用接口来创建，接口调用有以下两种形式：

- 通过label和[ButtonOptions](../../API_Reference/source_zh_cn/arkui-cj/cj-button-picker-button.md#class-buttonoptions)创建不包含子组件的按钮。以ButtonOptions中的shape和stateEffect为例。

    ```cangjie
    init(label: String, options: ButtonOptions)
    ```

    其中，label用来设置按钮文字，type用于设置Button类型，stateEffect属性设置Button是否开启点击效果。

    ```cangjie
    Button('Ok', ButtonOptions(shape: ButtonType.Normal, stateEffect: true))
        .borderRadius(8)
        .backgroundColor(0x317aff)
        .width(90)
        .height(40)
    ```

    ![Button](figures/Button.png)

- 通过[ButtonOptions](../../API_Reference/source_zh_cn/arkui-cj/cj-button-picker-button.md#class-buttonoptions)创建包含子组件的按钮。以ButtonOptions中的shape和stateEffect为例。

    ```cangjie
    init(options: ButtonOptions, content: () -> Unit)
    ```

    只支持包含一个子组件，子组件可以是基础组件或者容器组件。

    ```cangjie
    Button(ButtonOptions(shape: ButtonType.Normal, stateEffect: true)){
        Row() {
            Image(@r(app.media.loading)).width(20).height(40).margin(left: 12)
            Text('loading').fontSize(12).fontColor(0xffffff).margin(left: 5, right: 12)
        }.alignItems(VerticalAlign.Center)
    }
    .borderRadius(8)
    .backgroundColor(0x317aff)
    .width(90)
    .height(40)
    ```

    ![Button2](figures/Button2.png)

## 设置按钮类型

Button有四种可选类型，分别为胶囊类型（Capsule）、圆形按钮（Circle）、普通按钮（Normal）和圆角矩形按钮（ROUNDED_RECTANGLE），通过shape进行设置。

- 胶囊按钮（默认类型）。

    此类型按钮的圆角自动设置为高度的一半，不支持通过borderRadius属性重新设置圆角。

    ```cangjie
    Button('Disable', ButtonOptions(shape: ButtonType.Capsule, stateEffect: false))
        .backgroundColor(0x317aff)
        .width(90)
        .height(40)
    ```

    ![Button3](figures/Button3.png)

- 圆形按钮。

    此类型按钮为圆形，不支持通过borderRadius属性重新设置圆角。

    ```cangjie
    Button('Circle', ButtonOptions(shape: ButtonType.Circle, stateEffect: false))
        .backgroundColor(0x317aff)
        .width(90)
        .height(90)
    ```

    ![Button4](figures/Button4.png)

- 普通按钮。

    此类型的按钮默认圆角为0，支持通过borderRadius属性重新设置圆角。

    ```cangjie
    Button('Ok', ButtonOptions(shape: ButtonType.Normal, stateEffect: true))
        .borderRadius(8)
        .backgroundColor(0x317aff)
        .width(90)
        .height(40)
    ```

    ![Button5](figures/Button5.png)

- 圆角矩形按钮。

    当[controlSize](../../API_Reference/source_zh_cn/arkui-cj/cj-button-picker-button.md#func-controlsizecontrolsize)为NORMAL时，默认圆角大小为20.vp，[controlSize](../../API_Reference/source_zh_cn/arkui-cj/cj-button-picker-button.md#func-controlsizecontrolsize)为SMALL时，圆角大小为14.vp，支持通过borderRadius属性重新设置圆角。

    ```cangjie
    Button('Disable', ButtonOptions(shape: ButtonType.ROUNDED_RECTANGLE, stateEffect: true))
        .backgroundColor(0x317aff)
        .width(90)
        .height(40)
    ```

    ![Button11](figures/Button11.png)