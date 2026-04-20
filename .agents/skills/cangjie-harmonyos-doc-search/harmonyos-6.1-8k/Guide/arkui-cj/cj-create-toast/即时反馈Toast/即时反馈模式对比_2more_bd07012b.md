## 即时反馈模式对比

即时反馈提供了两种显示模式，分别为Default（显示在应用内）、TopMost（显示在应用之上）。

在TopMost类型的Toast显示前，会创建一个全屏大小的子窗（终端上子窗大小和主窗大小一致），然后在该子窗上计算Toast的布局位置，最后显示在该子窗上。具体和Default模式Toast的差异如下：

| 差异点| Default | TopMost |
| :--- | :--- | :--- |
| 是否创建子窗 | 否 | 是 |
| 层级 | 显示在主窗内，层级和主窗一致，一般比较低 | 显示在子窗中，一般比主窗层级高，比其他弹窗类组件层级高，比软键盘和权限弹窗层级低。 |
| 是否避让软键盘 | 软键盘抬起时，必定上移软键盘的高度。 | 软键盘抬起时，只有toast被遮挡时，才会避让，且避让后toast底部距离软键盘高度为80.vp。 |

 <!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.ui_context.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView{
    func build(){
        Column(){
            Blank().height(10.percent)
            Button(){
                Text("Default类型Toast")
                .fontSize(20)
                .fontWeight(FontWeight.Bold)
                .fontColor(Color.White)
            }.onClick({
                evt =>
                getUIContext().getPromptAction().showToast(
                        ShowToastOptions(
                            message: "ok，我是Default toast",
                            duration: 2000,
                            bottom: 72.percent,
                            showMode: ToastShowMode.Default
                        )
                    )
            })
            .align(Alignment.Center)
            .backgroundColor(0x0a59f7)
            .width(80.percent)
            .height(30.vp)

            Blank().height(2.percent)
            Button(){
                Text("TopMost类型Toast")
                .fontSize(20)
                .fontWeight(FontWeight.Bold)
                .fontColor(Color.White)
            }.onClick({
                evt =>
                getUIContext().getPromptAction().showToast(
                        ShowToastOptions(
                            message: "ok，我是TopMost toast",
                            duration: 2000,
                            bottom: 70.percent,
                            showMode: ToastShowMode.TopMost
                        )
                    )
            })
            .backgroundColor(0x0a59f7)
            .width(80.percent)
            .height(30.vp)
        }.size(width: 100.percent,height: 100.percent).alignItems(HorizontalAlign.Center)
    }
}
```

![creattoast](./figures/creattoast.gif)

## 创建即时反馈

适用于短时间内提示框自动消失的场景。

 <!--run-->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.ui_context.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView{

    func build(){
        Column(){
            Button("Show toast").fontSize(20)
            .onClick({
                    evt=>
                    getUIContext().getPromptAction().showToast(
                        ShowToastOptions(
                            message: "Hello World",
                            bottom: 35.percent,
                            duration: 2000
                        )
                    )
            })
        }.size(width: 100.percent,height: 100.percent).justifyContent(FlexAlign.Center)
    }
}
```

![image](figures/UIToast1.gif)