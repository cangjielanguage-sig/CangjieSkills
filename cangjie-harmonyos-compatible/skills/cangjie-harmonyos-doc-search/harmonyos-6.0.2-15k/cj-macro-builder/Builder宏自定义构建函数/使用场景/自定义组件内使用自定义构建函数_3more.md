### 自定义组件内使用自定义构建函数

创建私有的@Builder方法，在Column里面使用this.builder()方式调用，通过aboutToAppear生命周期函数和按钮的点击事件改变builder_value的内容，实现动态渲染UI。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var builder_value: String = "Hello"

    @Builder
    func builder() {
        Column {
            Text(this.builder_value).fontSize(30).fontWeight(FontWeight.Bold)
        }
    }

    protected override func aboutToAppear() {
        this.builder_value = "Hello World"
    }

    func build() {
        Row {
            Column {
                Text(this.builder_value).fontSize(30).fontWeight(FontWeight.Bold)

                this.builder()
                Button("点击改变builder_value内容").onClick({
                    => this.builder_value = "builder_value被点击了"
                })
            }
        }
    }
}
```

### 使用全局自定义构建函数

创建全局的@Builder方法，在Column里面使用overBuilder()方式调用，通过以对象字面量的形式传递参数，无论是简单类型还是复杂类型，值的改变都会引起UI界面的刷新。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

@Observed
class ChildTmp {
    @Publish
    var val: Int64 = 1
}

@Observed
class Tmp {
    @Publish
    var tmp_value: ChildTmp = ChildTmp()
    @Publish
    var str_value: String = "Hello"
    @Publish
    var num_value: Int64 = 0
    @Publish
    var arrayTmp_value: ObservedArrayList<ChildTmp> = ObservedArrayList<ChildTmp>()
}

@Builder
func overBuilder(param: Tmp) {
    Column {
        Text("str_value: ${param.str_value}")
        Text("num_value: ${param.num_value}")
        Text("tmp_value: ${param.tmp_value.val}")
        ForEach(
            param.arrayTmp_value,
            itemGeneratorFunc: {
                item: ChildTmp, idx: Int64 => Text("arrayTmp_value: ${item.val}")
            }
        )
    }
}

@Entry
@Component
class EntryView {
    @State
    var objParam: Tmp = Tmp()

    func build() {
        Column {
            Text("通过调用@Builder渲染UI界面").fontSize(20)
            overBuilder(this.objParam)

            Line().width(100.percent).height(10).backgroundColor(0x000000).margin(10)

            Button("点击改变参数值").onClick(
                {
                    _ =>
                    this.objParam.str_value = "Hello World"
                    this.objParam.num_value = 1
                    this.objParam.tmp_value.val = 8
                    let child_value: ChildTmp = ChildTmp(val: 2)
                    this.objParam.arrayTmp_value.append(child_value)
                }
            )
        }
    }
}
```

### 修改宏修饰的变量触发UI刷新

此种场景@Builder只是用来展示Text组件，没有参与动态UI刷新的功能，Text组件中值的变化是使用了宏的特性，监听到值的改变触发的UI刷新，而不是通过@Builder的能力触发的。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Tmp {
    @Publish
    var str_value: String = "Hello"
}

@Entry
@Component
class EntryView {
    @State
    var objParam: Tmp = Tmp()
    @State
    var label: String = "World"

    @Builder
    func privateBuilder() {
        Column {
            Text("wrapBuilder str_value: ${this.objParam.str_value}")
            Text("wrapBuilder num: ${this.label}")
        }
    }

    func build() {
        Column {
            Text("通过调用@Builder渲染UI界面").fontSize(20)
            this.privateBuilder()
            Line().width(100.percent).height(10).backgroundColor(0x000000).margin(10)

            Button("点击改变参数值").onClick(
                {
                    _ =>
                    this.objParam.str_value = "str_value: Hello World"
                    this.label = "label Hello World"
                }
            )
        }
    }
}
```