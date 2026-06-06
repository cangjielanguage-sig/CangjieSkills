# 线程控制

## 背景

仓颉开发HarmonyOS应用的过程中，代码逻辑主要分为两部分：UI 相关逻辑代码和 UI 无关逻辑代码。

- UI 相关逻辑代码：UI 布局描述代码，UI 状态声明及修改代码。
- UI 无关逻辑代码：除 UI 相关逻辑代码以外的其他代码。

UI 相关逻辑代码必须运行在拥有独立 OS 线程的 UI 线程中，UI 无关逻辑代码可以跑在任意 OS 线程中。由于仓颉代码运行于仓颉用户态线程，与 OS 线程不存在显式的绑定关系，进而无法保证 UI 代码逻辑运行在 UI 线程上，容易引发应用卡顿和安全风险等问题。

## 开发范式

支持指定代码逻辑可以自定义调度到UI线程或者非UI线程上运行。

### 导入模块

```cangjie
import kit.UIKit.Main
```

### 创建仓颉线程

使用仓颉的 spawn 关键字可以创建一个新的仓颉线程。支持使用变量 Main 和一个无形参的 lambda 表达式，该 lambda 表达式即为在新线程中执行的代码。

Main 实际为 MainThreadContext 类型的对象，表示此上下文中的 thread 将会与主线程（UI线程）绑定。

## 函数

### func launch(()->Unit)

```cangjie
public func launch(task: ()->Unit): Unit
```

**功能：** 将任务提交到主线程进行执行。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名     | 参数类型  | 必填 | 默认值 | 描述  |
|:--------|:------|:---|:----|:------------|
| task | ()->Unit | 是  | -  | 执行任务。 |

## 示例代码

### 示例1

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.time.*
import std.sync.*

@Entry
@Component
class EntryView {
    @State
    var isRefreshing: Bool = false
    @State
    var arr: Array<String> = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    func build() {
        Column() {
            Refresh(RefreshParams(refreshing: @Binder(this.isRefreshing))) {
                List {
                    ForEach(
                        this.arr,
                        itemGeneratorFunc: {
                            item: String, idx: Int64 => ListItem() {
                                Text("item, this.isRefreshing is : ${this.isRefreshing}").width(100.percent).height(100).
                                    fontSize(16).textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
                            }
                        },
                        keyGeneratorFunc: {
                            item: String, idx: Int64 => return item
                        }
                    )
                }.onScrollIndex(
                    {
                        first: Int32, last: Int32 =>
                        AppLog.info("list onScrollIndex")
                        AppLog.info("fist:" + first.toString())
                        AppLog.info("last:" + last.toString())
                    }
                ).width(100.percent).height(100.percent).divider(strokeWidth: 1.vp, color: Color(0X808080),
                    startMargin: 10.vp, endMargin: 10.vp).scrollBar(BarState.Off)
            }.onStateChange(
                {
                refreshStatus: RefreshStatus => AppLog.info(
                    "Refresh onStatueChange this.isRefreshing is is======= ${this.isRefreshing}")
            }).onRefreshing(
                {
                    =>
                    AppLog.info("onRefreshing this.isRefreshing is is======= ${this.isRefreshing}")
                    Timer.once(2000 * Duration.millisecond) {
                        => spawn (Main) {
                            this.isRefreshing = false
                            AppLog.info("setTimeout this.isRefreshing is======= ${this.isRefreshing}")
                        }
                    }

                    AppLog.info("onRefreshing test")
                }
            ).backgroundColor(0x89CFF0)
        }
    }
}
```

![img1](figures/thread.png)
