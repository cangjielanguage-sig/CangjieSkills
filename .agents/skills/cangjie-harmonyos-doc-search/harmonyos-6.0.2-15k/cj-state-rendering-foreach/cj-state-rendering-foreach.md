# ForEach

ForEach接口基于数组类型数据来进行循环渲染。

## 导入模块

```cangjie
import kit.UIKit.*
```

## class ForEach

ForEach调用形式如下：

```cangjie
ForEach(dataSource: ArrayList<T>, itemGeneratorFunc!: (T, Int64) -> Unit, keyGeneratorFunc!: (T, Int64) -> String)
```

**功能：** 创建一个循环渲染组件。ForEach接口基于数组类型数据来进行循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，ListItem组件要求ForEach的父容器组件必须为[List组件](./cj-scroll-swipe-list.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dataSource|ArrayList\<T>|是|-|数据源，根据这个ArrayList的大小确定循环的次数和子组件的数据。|
|itemGeneratorFunc|(T,Int64)->Unit|是|-| **命名参数。** 生成子组件的泛型lambda函数，为给定数组项生成一个或多个子组件。lambda函数的第一个泛型参数为数据源类型，第二个参数为当前列表项的index，Int64类型。|
|keyGeneratorFunc|(T,Int64)->String|是|-| **命名参数。** 生成子组件ID的泛型lambda函数，为给定数组项生成对应的ID。lambda函数的第一个泛型参数为数据源类型，第二个参数为当前列表项的index，Int64类型。|

## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.*

@Entry
@Component
public class EntryView {
    let simpleList: Array<String> = ["one", "two", "three"]

    func build(): Unit {
        Row() {
            Column() {
                ForEach(
                    this.simpleList,
                    itemGeneratorFunc: {
                        item: String, _: Int64 => Text(item).fontSize(50)
                    }
                )
            }.width(100.percent)
        }.backgroundColor(0xF1F3F5)
    }
}
```

![foreach](figures/foreach.png)
