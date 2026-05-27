# 基础自定义弹出框（CustomDialog）（不推荐）

CustomDialog是自定义弹出框，可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过CustomDialogController类显示自定义弹出框。具体用法请参见[自定义弹出框](../../API_Reference/source_zh_cn/arkui-cj/cj-dialog-customdialog.md)。

> **说明：**
>
> ArkUI弹出框默认为非页面级弹出框，在页面路由跳转时，如果开发者未调用close方法将其关闭，弹出框将不会自动关闭。若需实现在跳转页面时覆盖弹出框的场景，建议使用Navigation。具体使用方法，请参见[组件导航子页面显示类型的弹窗类型](./cj-navigation-navigation.md)。

弹出框（CustomDialog）可以通过配置[isModal](../../API_Reference/source_zh_cn/arkui-cj/cj-dialog-customdialog.md#var-ismodal)来实现模态和非模态弹窗。isModal为true时，弹出框为模态弹窗。isModal为false时，弹出框为非模态弹窗。

## 创建自定义弹出框

1. 使用@CustomDialog宏装饰自定义弹出框，可在此宏内自定义弹出框内容。CustomDialogController需在@Component内定义。

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @CustomDialog
    class MyDialog {
        var controller: Option<CustomDialogController> = Option.None
        func build() {
            Column() {
                Text("我是内容").fontSize(20)
            }.height(60).justifyContent(FlexAlign.Center)
        }
    }
    ```

2. 创建构造器，与宏呼应相连。点击与onClick事件绑定的组件使弹出框弹出。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @CustomDialog
    class MyDialog {
        var controller: Option<CustomDialogController> = Option.None
        func build() {
            Column() {
                Text("我是内容").fontSize(20)
            }.height(60).justifyContent(FlexAlign.Center)
        }
    }

    @Entry
    @Component
    class EntryView {
        var dialogController: CustomDialogController = CustomDialogController(
            CustomDialogControllerOptions(builder: MyDialog()))
        func build() {
            Column {
                Button("click me").onClick({
                    evt => dialogController.`open`()
                })
            }
        }
    }
    ```

    ![gouzao](figures/zidingyi.jpg)

## 弹出框的交互

弹出框可用于数据交互，完成用户一系列响应操作。

1. 在@CustomDialog宏内添加按钮，同时添加数据函数。

    ```cangjie
    @CustomDialog
    class MyDialog {
        var controller: Option<CustomDialogController> = Option.None
        func build() {
            Flex(FlexParams(justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center)) {
                Text("我是内容").fontSize(20)

                Button("cancel").onClick {
                    evt => controller?.close()
                }
                Button("confirm").onClick {
                    evt => controller?.close()
                }
            }.height(500.px)
        }
    }
    ```

2. 弹出框页面页面需要在构造器内进行接收，同时创建相应的函数操作。

    <!-- run -->

    ```cangjie
    package ohos_app_cangjie_entry

    import kit.UIKit.*
    import ohos.state_macro_manage.*

    @CustomDialog
    class MyDialog {
        var controller: Option<CustomDialogController> = Option.None
        func build() {
            Flex(FlexParams(justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center)) {
                Text("我是内容").fontSize(20)

                Button("cancel").onClick {
                    evt => controller?.close()
                }
                Button("confirm").onClick {
                    evt => controller?.close()
                }
            }.height(500.px)
        }
    }

    @Entry
    @Component
    class EntryView {
        var dialogController: CustomDialogController = CustomDialogController(
            CustomDialogControllerOptions(builder: MyDialog()))
        func build() {
            Column {
                Button("click me").onClick({
                    evt => dialogController.`open`()
                })
            }
        }
    }
    ```

    ![dialog-interaction](figures/dialog-interaction.jpg)