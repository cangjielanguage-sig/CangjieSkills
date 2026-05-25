### 不允许在build里改状态变量

不允许在build里改变状态变量，状态管理框架会在运行时报出Error级别日志。

下面的示例，渲染的流程是：

1. 创建Index自定义组件。

2. 执行Index的build方法：

    a. 创建Column组件。

    b. 创建Text组件。创建Text组件的过程中，触发this.count++。

    c. count的改变再次触发Text组件的刷新。

    d. Text最终渲染。

```cangjie
@Entry
@Component
class EntryView {
    @State
    var count: Int64 = 1
    func build() {
        Column() {
            // 应避免直接在Text组件内改变count的值
            Text("${this.count++}").width(50).height(50)
        }
    }
}
```

在上面的例子中，这个错误行为不会造成很严重的后果。

但这个行为是严重错误的，会随着工程的复杂度升级，隐患越来越大。见下一个例子。

```cangjie
@Entry
@Component
class EntryView {
    @State
    var message: Int = 20;
    func build() {
        Column() {
            Text("${this.message++}")
            Text("${this.message++}")
        }.width(50).height(100)
    }
}
```

上面示例渲染过程：

1. 创建第一个Text组件，触发this.message改变。

2. this.message改变又触发第二个Text组件的刷新。

3. 第二个Text组件的刷新又触发this.message的改变，触发第一个Text组件刷新。

4. 循环重新渲染。

5. 系统长时间无响应，appfreeze。

所以，在build里面改变状态变量的这种行为是完全错误的。

### 用注册回调的方式更改状态变量需要执行解注册

开发者可以在onPageShow中注册箭头函数，并以此来改变组件中的状态变量。但需要注意的是在aboutToDisappear中将之前注册的函数置空，否则会因为箭头函数捕获了自定义组件的this实例，导致自定义组件无法被释放，从而造成内存泄漏。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Model {
    @Publish
    var callback: () -> Unit
    func add(callback: () -> Unit) {
        this.callback = callback
    }
    func delete() {
        this.callback = Option<() -> Unit>.None.getOrThrow()
    }
    func call() {
        if (true) {
            this.callback()
        }
    }
}

let model = Model(callback: {=>})

@Entry
@Component
class EntryView {
    @State
    var count: Int64 = 10

    public override func onPageShow() {
        model.add({=> this.count++})
    }
    func build() {
        Column() {
            Text("count值: ${this.count}")
            Button('change').onClick({
                evt => model.call()
            })
        }
    }
    public func aboutToDisappear() {
        model.delete()
    }
}
```

此外，也可以使用[LocalStorage](./cj-localstorage.md#自定义组件改变状态变量)的方式在自定义组件外改变状态变量。