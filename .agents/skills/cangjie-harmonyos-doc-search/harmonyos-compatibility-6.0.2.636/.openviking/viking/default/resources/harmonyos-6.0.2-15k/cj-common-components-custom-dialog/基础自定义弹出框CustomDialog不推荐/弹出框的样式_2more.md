## 弹出框的样式

弹出框通过定义宽度、高度、背景色、阴影等参数来控制样式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@CustomDialog
class MyDialog {
    var controller: Option<CustomDialogController> = Option.None
    func build() {
        Row(40) {
            Text("我是内容").fontSize(20).margin(top: 4, right: 4, bottom: 4, left: 4)
        }.height(500.px)
    }
}

@Entry
@Component
class EntryView {
    var dialogController: CustomDialogController = CustomDialogController(
        CustomDialogControllerOptions(
            builder: MyDialog(),
            autoCancel: true,
            alignment: DialogAlignment.Center,
            offset: Offset(0.vp, 0.vp),
            gridCount: 4,
            customStyle: false,
            backgroundColor: 0xd9ffffff,
            isModal: true,
            cornerRadius: 20,
            width: 120,
            height: 120,
            borderWidth: 1,
            borderStyle: EdgeStyle.SOLID, // 使用borderStyle属性，需要和borderWidth属性一起使用
            borderColor: Color.BLUE, // 使用borderColor属性，需要和borderWidth属性一起使用
            shadow: Option<ShadowOptions>.None,
        )
    )
    func build() {
        Column {
            Button("click me").onClick({
                evt => dialogController.`open`()
            })
        }
    }
}
```

![biankuangyangshi](figures/biankuangyangshi.jpg)

## 嵌套自定义弹出框

通过第一个弹出框打开第二个弹出框时，最好将第二个弹出框定义在第一个弹出框的父组件处，通过父组件传给第一个弹出框的回调来打开第二个弹出框。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@CustomDialog
class CustomDialogExampleTwo {
    var controllerTwo: Option<CustomDialogController> = Option.None
    @State
    var message: String = "I'm the second dialog box."
    @State
    var showIf: Bool = false
    func build() {
        Column() {
            if (this.showIf) {
                Text("Text").fontSize(30).height(100)
            }
            Text(this.message).fontSize(30).height(100)
            Button("Create Text").onClick({
                => this.showIf = true
            })
            Button("Close Second Dialog Box").onClick({
                => if (let Some(v) <- this.controllerTwo) {
                    v.close()
                }
            }).margin(20)
        }
    }
}

@CustomDialog
class MyDialog {
    var openSecondBox: () -> Unit
    var controller: Option<CustomDialogController> = Option.None
    func build() {
        Row(600) {
            Button("Open Second Box").onClick(
                {
                    =>
                    this.controller?.close()
                    this.openSecondBox()
                }
            ).margin(20)
        }.borderRadius(10)
    }
}

@Entry
@Component
class EntryView {
    @State
    var inputValue: String = "Click Me"
    var dialogController: CustomDialogController = CustomDialogController(
        CustomDialogControllerOptions(
            builder: MyDialog(openSecondBox: {=> this.dialogControllerTwo.open()}),
            autoCancel: true,
            alignment: DialogAlignment.Bottom,
            offset: Offset(0, -20),
            gridCount: 4,
            customStyle: false
        )
    )
    var dialogControllerTwo: CustomDialogController = CustomDialogController(
        CustomDialogControllerOptions(
            builder: CustomDialogExampleTwo(),
            autoCancel: true,
            alignment: DialogAlignment.Bottom,
            offset: Offset(0, -25)
        )
    )

    func build() {
        Column() {
            Button(this.inputValue).onClick({
                => this.dialogController.`open`()
            }).backgroundColor(0x317aff)
        }.width(100.percent).margin(top: 20)
    }
}
```

![nestedcustomdailog](figures/nestedcustomdailog.gif)

由于自定义弹出框在状态管理侧有父子关系，如果将第二个弹出框定义在第一个弹出框内，那么当父组件（第一个弹出框）被销毁（关闭）时，子组件（第二个弹出框）内无法再继续创建新的组件。