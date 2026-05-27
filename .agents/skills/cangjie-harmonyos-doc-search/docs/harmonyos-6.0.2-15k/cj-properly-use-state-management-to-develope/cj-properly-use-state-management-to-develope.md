# 状态管理合理使用开发指导

由于对状态管理当前的特性并不了解，许多开发者在使用状态管理进行开发时会遇到UI不刷新、刷新性能差的情况。对此，本篇将从两个方向，对一共五个典型场景进行分析，同时提供相应的正例和反例，帮助开发者学习如何合理使用状态管理进行开发。

## 合理使用属性

## 将简单属性数组合并成对象数组

在开发过程中，我们经常会需要设置多个组件的同一种属性，比如Text组件的内容、组件的宽度、高度等样式信息等。将这些属性保存在一个数组中，配合ForEach进行使用是一种简单且方便的方法。

### 将复杂大对象拆分成多个小对象的集合

在开发过程中，我们有时会定义一个大的对象，其中包含了很多样式相关的属性，并且在父子组件间传递这个对象，将其中的属性绑定在组件上。

### 使用@Observed装饰或被声明为状态变量的类对象绑定组件

在开发过程中，会有“重置数据”的场景，将一个新创建的对象赋值给原有的状态变量，实现数据的刷新。如果不注意新创建对象的类型，可能会出现UI不刷新的现象。

## 合理使用ForEach/LazyForEach

### 减少使用LazyForEach的重建机制刷新UI

### 在ForEach中使用ObservedArrayList

开发过程中经常会使用对象数组和ForEach结合起来使用，但是写法不当的话会出现UI不刷新的情况。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList
import ohos.hilog.Hilog

@Observed
class TextStyles {
    @Publish
    var fontSize: Int64
}

@Entry
@Component
class EntryView {
    @State
    var styleList: ArrayList<TextStyles> = ArrayList<TextStyles>([])

    public override func aboutToAppear() {
        for (i in 1..=35) {
            this.styleList.add(TextStyles(fontSize: i))
        }
    }

    func build() {
        Column {
            Text("Font Size List").fontSize(50).onClick {
                evt =>
                for (i in 0..this.styleList.size) {
                    this.styleList[i].fontSize++
                }
                Hilog.info(0, "test", "change font size")
            }
            List() {
                ForEach(
                    this.styleList,
                    {
                        item: TextStyles, _: Int64 => ListItem() {
                            Text("Hello World").fontSize(item.fontSize)
                        }
                    }
                )
            }
        }
    }
}
```

![developguide51](./figures/developguide51.gif)

由于ForEach中生成的item是一个常量，因此当点击改变item中的内容时，没有办法观测到UI刷新，尽管日志表面item中的值已经改变了(这体现在打印了“change font size”的日志)。因此，需要使用ObservedArrayList，配合 \@Publish 修饰自定义类属性来实现观测的能力。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList
import ohos.hilog.Hilog

@Observed
class TextStyles {
    @Publish
    var fontSize: Int64
}

@Entry
@Component
class EntryView {
    @State
    var styleList: ObservedArrayList<TextStyles> = ObservedArrayList<TextStyles>([])

    public override func aboutToAppear() {
        for (i in 1..=35) {
            this.styleList.append(TextStyles(fontSize: i))
        }
    }

    func build() {
        Column {
            Text("Font Size List").fontSize(50).onClick {
                evt =>
                for (i in 0..this.styleList.size) {
                    this.styleList[i].fontSize++
                }
                Hilog.info(0, "AppLog: info", "change font size")
            }
            List() {
                ForEach(
                    this.styleList,
                    {
                        item: TextStyles, _: Int64 => ListItem() {
                            Text("Hello World").fontSize(item.fontSize)
                        }
                    }
                )
            }
        }
    }
}
```

![developguide52](./figures/developguide52.gif)

使用\@Publish修饰的自定义类属性，使得Text组件内的textStyles变量具有了被观测的能力。在更改styleList中的值时，会观测到styleList每一个textStyles对应item的fontSize值被改变，因此触发UI的刷新。

这是一个较为实用的使用状态管理进行刷新的开发方式。
