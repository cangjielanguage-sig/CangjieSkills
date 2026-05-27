### 动态布局更新

- 示例代码将Child自定义组件标记为复用组件，通过Button点击更新Child，触发Child复用;

- @Reusable：自定义组件被@Reusable宏修饰，即表示其具备组件复用的能力;

- aboutToReuse：当一个可复用的自定义组件从复用缓存中重新加入到节点树时，触发aboutToReuse生命周期回调，并将组件的构造参数传递给aboutToReuse。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_manage.*
import ohos.state_macro_manage.*

public class Message {
    public var value: String
    public init(val: String) {
        value = val
    }
}

@Entry
@Component
public class EntryView {
    @State
    var switch: Bool = true
    public func build() {
        Column() {
            Button("Hello").fontSize(30).fontWeight(FontWeight.Bold).onClick {
                => switch = !switch
            }
            if (switch) {
                Child(message: Message("Child"))
            }
        }.height(100.percent).width(100.percent)
    }
}

@Reusable
@Component
class Child {
    @State
    var message: Message = Message("about to reuse")
    protected override func aboutToReuse(val: ReuseParams) {
        if (val.contains("message")) {
            let msg = val.get("message").getOrThrow()
            message = msg as Message ?? Message("None")
            AppLog.info("Recycle ===Child===")
        }
    }
    func build() {
        Column() {
            Text(this.message.value)
        }.borderWidth(1).height(100)
    }
}
```

### 列表滚动配合LazyForEach使用

- 示例代码将CardView自定义组件标记为复用组件，List上下滑动，触发CardView复用;

- @Reusable：自定义组件被@Reusable装饰器修饰，即表示其具备组件复用的能力;

- 变量item的被@State修饰，才能更新，非@State修饰变量存在无法更新问题。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_manage.*
import ohos.state_macro_manage.*
import std.collection.ArrayList

class MyDataSource <: IDataSource<Int64> {
    public MyDataSource(let data_: ArrayList<Int64>) {}
    public var listenerOp: Option<DataChangeListener> = None
    public func totalCount(): Int64 {
        return data_.size
    }
    public func getData(index: Int64): Int64 {
        return data_[index]
    }

    public func pushData(val: Int64): Unit {
        data_.add(val)
    }

    public func onRegisterDataChangeListener(listener: DataChangeListener): Unit {
        listenerOp = listener
    }

    public func onUnregisterDataChangeListener(listener: DataChangeListener): Unit {
        listenerOp = None
    }
}

@Entry
@Component
public class EntryView {
    let data: MyDataSource = MyDataSource(ArrayList<Int64>([]))
    protected override func aboutToAppear() {
        for (i in 0..1000) {
            data.pushData(i)
        }
    }

    public func build(): Unit {
        Column() {
            List() {
                LazyForEach(
                    data,
                    itemGeneratorFunc: {
                        item: Int64, idx: Int64 => ListItem() {
                            CardView(item: "${item}")
                        }
                    }
                )
            }
        }
    }
}

// 复用组件
@Reusable
@Component
class CardView {
    @State
    var item: String = ""
    protected override func aboutToReuse(val: ReuseParams) {
        if (val.contains("item")) {
            let itemTmp = val.get("item").getOrThrow()
            item = itemTmp as String ?? ""
        }
    }
    func build() {
        Column() {
            Text(item)
        }.borderWidth(1).height(100)
    }
}
```