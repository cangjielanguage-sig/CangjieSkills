# 固定样式弹出框

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

固定样式弹出框采用固定的布局格式，这使得开发者无需关心具体的显示布局细节，只需输入所需显示的文本内容，从而简化了使用流程，提升了便捷性。

## 使用约束

- 操作菜单（showActionMenu）、对话框（showDialog）需先使用[getPromptAction](../reference/arkui-cj/cj-apis-uicontext-uicontext.md#func-getpromptaction)方法获取到PromptAction对象，再通过该对象调用对应方法。

- 操作菜单（showActionMenu）、对话框（showDialog）、列表选择弹出框（ActionSheet）、警告弹出框（AlertDialog）可以设置isModal为false，变成非模态弹窗。

## 操作菜单（showActionMenu）

操作菜单通过[UIContext](../reference/arkui-cj/cj-apis-uicontext-uicontext.md#class-uicontext)中的[getPromptAction](../reference/arkui-cj/cj-apis-uicontext-uicontext.md#func-getpromptaction)方法获取到PromptAction对象，支持在回调或开发者自定义类中使用。

创建并显示操作菜单后，菜单的响应结果会异步返回选中按钮在buttons数组中的索引。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.arkui.component.*
import ohos.arkui.state_management.*
import ohos.arkui.state_macro_manage.*
import std.collection.*
import ohos.arkui.ui_context.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.*

@Entry
@Component
class EntryView {
    @State var index1: Int32 = 0
    func build() {
         Column {
            Button("showActionMenu").onClick(
                {
                    evt =>
                    let buttons: Array<ButtonInfo> = [ButtonInfo(text: "item1", color: Color.Gray), ButtonInfo(text: "item2", color: Color.Black)]
                    getUIContext().getPromptAction().showActionMenu(ActionMenuOptions(title: "showActionMenu Title Info", buttons: buttons),
                        callback: {
                            err: Option<BusinessException>, i: Option<Int32> => try {
                                match (err) {
                                    case Some(e) => Hilog.info(0, "cangjie", "error: errcode is ${e.code}")
                                    case _ => index1 = i.getOrThrow()
                                }
                            } catch (e: Exception) {
                                Hilog.info(0, "cangjie", e.toString())
                            }
                        })
                }
            )
        }.width(100.percent).padding(top: 5)
    }
}
```

![image](figures/UIContextShowMenu.gif)

## 对话框（showDialog）

对话框通过[getPromptAction](../reference/arkui-cj/cj-apis-uicontext-uicontext.md#func-getpromptaction)方法获取到PromptAction对象，支持在回调或开发者自定义类中使用。

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.arkui.component.*
import ohos.arkui.state_management.*
import ohos.arkui.state_macro_manage.*
import std.collection.*
import ohos.arkui.ui_context.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.*

@Entry
@Component
class EntryView {
    @State var index1: Int32 = 0
    func build() {
         Column {
            Button("showDialog").onClick(
                {
                    evt =>
                    getUIContext().getPromptAction().showDialog(
                        ShowDialogOptions(
                            title: "showDialog Title Info",
                            buttons: [
                                ButtonInfo(text: 'button1', color: Color(0X000000)),
                                ButtonInfo(text: 'button2', color: Color(0X000000))
                            ]
                        ),
                        callback: {
                            err: Option<BusinessException>, i: Option<Int32> => try {
                                match (err) {
                                    case Some(e) => Hilog.info(0, "cangjie", "error: errcode is ${e.code}")
                                    case _ => ()
                                }
                            } catch (e: Exception) {
                                Hilog.info(0, "cangjie", e.toString())
                            }
                        }
                    )
                }
            )
        }.width(100.percent).padding(top: 5)
    }
}
```

![showdialog](figures/showdialog.gif)