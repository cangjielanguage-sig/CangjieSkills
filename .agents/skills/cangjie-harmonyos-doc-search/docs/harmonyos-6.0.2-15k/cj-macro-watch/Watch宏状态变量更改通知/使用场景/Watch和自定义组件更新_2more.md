### @Watch和自定义组件更新

以下示例展示组件更新和@Watch的处理步骤。count在CountModifier中由@State装饰，在TotalView中由@Link装饰。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Component
class TotalView {
    @Link
    @Watch[onCountUpdated]
    var count: Int64 = 0
    @State
    var total: Int64 = 0
    // @Watch 回调
    func onCountUpdated(): Unit {
        this.total += this.count
    }
    func build() {
        Text("Total: ${this.total}")
    }
}

@Entry
@Component
class EntryView {
    @State
    var count: Int64 = 0
    func build() {
        Column() {
            Button("add to basket").onClick({
                => this.count++
            })
            TotalView(count: this.count)
        }
    }
}
```

处理步骤如下：

1. EntryView自定义组件的Button.onClick点击事件自增count。
2. 由于@State count变量更改，子组件TotalView中的@Link被更新，其@Watch("onCountUpdated")方法被调用，更新了子组件TotalView 中的total变量。
3. 子组件TotalView中的Text重新渲染。

### @Watch与@Link组合使用

以下示例说明了如何在子组件中观察@Link变量。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.collection.ArrayList
import std.random.*

@Component
class BasketViewer {
    @Link
    @Watch[onBasketUpdated]
    var shopBasket: ArrayList<Float64>
    @State
    var totalPurchase: Float64 = 0.0
    func updateTotal(): Float64 {
        var total: Float64 = 0.0
        for (i in shopBasket) {
            total += i
        }
        if (total >= 100.0) {
            total = 0.9 * total
        }
        return total
    }
    // @Watch 回调
    func onBasketUpdated() {
        this.totalPurchase = this.updateTotal()
    }
    func build() {
        Column() {
            ForEach(
                this.shopBasket,
                itemGeneratorFunc: {
                    item: Float64, index: Int64 =>
                    Text("${index}")
                    Text("Price：${item} €")
                }
            )
            Text("Total: ${this.totalPurchase} €")
        }
    }
}

@Entry
@Component
class EntryView {
    @State
    var shopBasket: ArrayList<Float64> = ArrayList<Float64>([0.0])
    let m: Random = Random()
    func build() {
        Column() {
            Button("Add to basket").onClick(
                {
                    etv =>
                    var temp = this.shopBasket.clone()
                    temp.add(100.0 * m.nextFloat64())
                    this.shopBasket = temp
                }
            )
            BasketViewer(shopBasket: shopBasket)
        }
    }
}
```

处理步骤如下：

1. BasketModifier组件的Button.onClick向BasketModifier shopBasket中添加条目。
2. @Link装饰的BasketViewer shopBasket值发生变化。
3. 状态管理框架调用@Watch函数BasketViewer onBasketUpdated 更新BasketViewer TotalPurchase的值。
4. @Link shopBasket的改变，新增了数组项，ForEach组件会执行item Builder，渲染构建新的Item项；@State totalPurchase改变，对应的Text组件也重新渲染；重新渲染是异步发生的。