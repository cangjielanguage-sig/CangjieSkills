### 使用全局和局部的@Builder传入customBuilder类型

当某个参数类型为customBuilder的时候，可以把定义的@Builder函数传入，因为customBuilder实际是一个Function类型或者是Unit类型，而@Builder实际也是一个Function类型。此场景中通过把@Builder传入已实现特定的效果

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Builder
func myBuilder2() {
    Column {
        Text("全局 Builder")
    }.width(100.percent).height(100.percent).align(Alignment.Center)
}

@Entry
@Component
class EntryView {
    @State
    var isShow: Bool = false
    @State
    var isShow2: Bool = false

    @Builder
    func myBuilder() {
        Column {
            Text("局部 Builder")
        }.width(100.percent).height(100.percent).align(Alignment.Center)
    }

    func build() {
        Column {
            Button("局部 Builder").onClick({
                => this.isShow = true
            }).fontSize(20).margin(10).bindSheet(this.isShow, myBuilder,
                options: SheetOptions(onDisappear: {=> this.isShow = false}))

            Button("全局 Builder").onClick({
                => this.isShow2 = true
            }).fontSize(20).margin(10).bindSheet(this.isShow2, myBuilder2,
                options: SheetOptions(onDisappear: {=> this.isShow2 = false}))
        }.justifyContent(FlexAlign.Center).backgroundColor(Color.WHITE).width(100.percent).height(100.percent)
    }
}
```

### 多层@Builder方法嵌套使用

在@Builder方法内调用自定义组件或者其他@Builder方法，以实现多个@Builder嵌套使用的场景，要想实现最里面的@Builder动态UI刷新功能，必须要保证每层调用@Builder的地方使用按引用传递的方式。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Tmp {
    @Publish
    var paramA1: String = ""
}

@Builder
func parentBuilder(params: Tmp) {
    Row {
        Text("parentBuilder: ${params.paramA1}")
    }
    childBuilder(params)
}

@Builder
func childBuilder(params: Tmp) {
    Row {
        Text("childBuilder: ${params.paramA1}")
    }
    grandsonBuilder(params)
}

@Builder
func grandsonBuilder(params: Tmp) {
    Row {
        Text("grandsonBuilder: ${params.paramA1}")
    }
}

@Entry
@Component
class EntryView {
    @State
    var tmp: Tmp = Tmp(paramA1: "Hello")

    func build() {
        Column {
            parentBuilder(this.tmp)
            Text(this.tmp.paramA1)
            Button("Click me").onClick({
                _ => this.tmp.paramA1 = "ArkUI"
            })
        }
    }
}
```