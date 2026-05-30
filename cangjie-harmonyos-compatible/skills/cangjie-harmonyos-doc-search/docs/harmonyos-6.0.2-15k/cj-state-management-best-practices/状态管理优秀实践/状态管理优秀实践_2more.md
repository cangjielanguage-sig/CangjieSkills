# 状态管理优秀实践

为了帮助应用程序开发人员提高其应用程序质量，特别是在高效的状态管理方面。本章节面向开发者提供了多个在开发ArkUI应用中常见的低效开发的场景，并给出了对应的解决方案。此外，还提供了同一场景下，推荐用法和不推荐用法的对比和解释说明，更直观地展示两者区别，从而帮助开发者学习如何正确地在应用开发中使用状态变量，进行高性能开发。

## 不使用状态变量强行更新非状态变量关联组件

【反例】

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import kit.LocalizationKit.*
import std.collection.*

@Entry
@Component
class EntryView {
    @State
    var needsUpdate: Bool = true
    var realStateArr: ArrayList<Int64> = ArrayList<Int64>([4, 1, 3, 2])
    var realState: Color = Color.YELLOW

    func updateUIArr(param: ArrayList<Int64>): ArrayList<Int64> {
        let triggerAGet: Bool = this.needsUpdate
        return param
    }

    func updateUI(param: Color): Color {
        let triggerAGet: Bool = this.needsUpdate
        return param
    }

    func build() {
        Column(20) {
            ForEach(this.updateUIArr(this.realStateArr), {item: Int64, _: Int64 => Text("${item}")})
            Text("add item").onClick(
                {
                    event =>
                    // 改变realStateArr不会触发UI视图更新
                    this.realStateArr.add(this.realStateArr[this.realStateArr.size - 1] + 1)

                    // 触发UI视图更新
                    this.needsUpdate = !this.needsUpdate
                }
            )

            Text("chg color").onClick(
                {
                    event =>
                    // 改变realState不会触发UI视图更新
                    match {
                        case this.realState.toUInt32() == Color.YELLOW.toUInt32() => this.realState = Color.RED
                        case this.realState.toUInt32() == Color.RED.toUInt32() => this.realState = Color.YELLOW
                        case _ => AppLog.error("realState invalid")
                    }

                    // 触发UI视图更新
                    this.needsUpdate = !this.needsUpdate
                }
            )
        }.backgroundColor(this.updateUI(this.realState)).width(200).height(500)
    }
}
```

上述示例存在以下问题：

- 应用程序希望控制UI更新逻辑，但在ArkUI中，UI更新的逻辑应该是由框架来检测应用程序状态变量的更改去实现。
- this.needsUpdate是一个自定义的UI状态变量，应该仅应用于其绑定的UI组件。变量this.realStateArr、this.realState没有被装饰，他们的变化将不会触发UI刷新。
- 但是在该应用中，用户试图通过this.needsUpdate的更新来带动常规变量this.realStateArr、this.realState的更新，此方法不合理且更新性能较差。

【正例】

要解决此问题，应将realStateArr和realState成员变量用@State装饰。一旦完成此操作，就不再需要变量needsUpdate。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var realStateArr: ObservedArrayList<Int64> = ObservedArrayList<Int64>([4, 1, 3, 2])
    @State
    var realState: Color = Color.YELLOW

    func build() {
        Column(20) {
            ForEach(this.realStateArr, {item: Int64, _: Int64 => Text("${item}")})

            Text("add item").onClick(
                {
                event =>
                // 改变realStateArr触发UI视图更新
                this.realStateArr.append((this.realStateArr[this.realStateArr.size - 1] + 1))
            })

            Text("chg color").onClick(
                {
                event =>
                // 改变realState触发UI视图更新
                match {
                    case this.realState.toUInt32() == Color.YELLOW.toUInt32() => this.realState = Color.RED
                    case this.realState.toUInt32() == Color.RED.toUInt32() => this.realState = Color.YELLOW
                    case _ => AppLog.error("realState invalid")
                }
            }).backgroundColor(this.realState).width(200).height(500)
        }
    }
}
```