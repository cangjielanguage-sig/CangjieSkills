# 固定样式弹出框

固定样式弹出框采用固定的布局格式，这使得开发者无需关心具体的显示布局细节，只需输入所需显示的文本内容，从而简化了使用流程，提升了便捷性。

## 使用约束

- 操作菜单（showActionMenu）、对话框（showDialog）需先使用PromptAction方法获取到PromptAction对象，再通过该对象调用对应方法。

- 操作菜单（showActionMenu）、对话框（showDialog）、列表选择弹出框（ActionSheet）、警告弹出框（AlertDialog）可以设置isModal为false，变成非模态弹窗。

## 操作菜单（showActionMenu）

操作菜单通过PromptAction方法获取到PromptAction对象，再通过该对象调用[showActionMenu](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-promptaction.md#static-func-showactionmenuactionmenuoptions-showactionmenucallback)接口实现，支持在回调或开发者自定义类中使用。

创建并显示操作菜单后，菜单的响应结果会异步返回选中按钮在buttons数组中的索引。

<!-- run -->

```cangjie
// xxx.cj
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.*
import ohos.prompt_action.ButtonInfo
import ohos.prompt_action.PromptAction

@Entry
@Component
class EntryView {
    @State
    var index1: Int32 = 0
    func build() {
        Column {
            Button("showActionMenu").onClick(
                {
                    evt =>
                    let buttons: Array<ButtonInfo> = [ButtonInfo("item1", Color.GRAY), ButtonInfo("item2", Color.BLACK)]
                    PromptAction.showActionMenu(title: "showActionMenu Title Info", buttons: buttons,
                        callback: {
                        err: Option<AsyncError>, i: Option<Int32> => try {
                            match (err) {
                                case Some(e) => AppLog.error("error: errcode is ${e.code}")
                                case _ => index1 = i.getOrThrow()
                            }
                        } catch (e: Exception) {
                            AppLog.error(e.toString())
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

对话框通过PromptAction方法获取到PromptAction对象，再通过该对象调用[showDialog](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-promptaction.md#static-func-showdialogshowdialogoptions-showdialogcallback)接口实现，支持在回调或开发者自定义类中使用。

创建并显示对话框，对话框响应后异步返回选中按钮在buttons数组中的索引。

<!-- run -->

```cangjie
// xxx.cj
package ohos_app_cangjie_entry

import ohos.base.*
import ohos.component.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.*
import ohos.prompt_action.ButtonInfo
import ohos.prompt_action.PromptAction

@Entry
@Component
class EntryView {
    @State
    var index0: Int32 = 0
    func build() {
        Column {
            Button("showDialog").onClick(
                {
                    evt =>
                    let buttons: Array<ButtonInfo> = [ButtonInfo("button1", Color.BLACK),
                        ButtonInfo("button2", Color.BLACK)]
                    PromptAction.showDialog(title: "showDialog Title Info", message: "Message Info", buttons: buttons,
                        callback: {
                        err: Option<AsyncError>, i: Option<Int32> => try {
                            match (err) {
                                case Some(e) => AppLog.error("error: errcode is ${e.code}")
                                case _ => index0 = i.getOrThrow()
                            }
                        } catch (e: Exception) {
                            AppLog.error(e.toString())
                        }
                    })
                }
            )
        }.width(100.percent).padding(top: 5)
    }
}
```

![image](figures/UIShowDialog.gif)