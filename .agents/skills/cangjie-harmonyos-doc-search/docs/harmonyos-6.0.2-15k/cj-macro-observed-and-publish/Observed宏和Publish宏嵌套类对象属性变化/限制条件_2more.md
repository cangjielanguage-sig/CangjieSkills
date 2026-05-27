## 限制条件

1. \@Observed 所装饰的类，不能在类定义时继承其他类扩展和接口，也不能装饰 open class 作为其他类的父类，否则将产生编译错误。

2. \@Observed 装饰的类不能定义构造函数。被 \@Observed 修饰的类会自动生成带命名参数的构造函数。

3. \@Publish 装饰的变量类型需要为自定义类型拥有的成员变量，且如果未不是 \@Observed 装饰的class成员变量，其内容更新不会触发UI更新。

4. \@Publish 只能修饰仓颉自定义类型由var声明的成员变量，不能修饰let变量和静态变量。

5. 在\@Observed 修饰的类中，\@Publish 修饰的成员变量一定要得到初始化。

## 使用场景

### 成员变量为自定义类型

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Book {
    @Publish
    var name: String
}

@Observed
class Bag {
    @Publish
    var book: Book
}

@Entry
@Component
class EntryView {
    @State
    var bag: Bag = Bag(book: Book(name: "Cangjie"))

    func build() {
        Column {
            Text("Index: ${this.bag.book.name}")
            Button("change book.name").onClick {
                => this.bag.book.name = "ArkUI"
            }
        }
    }
}
```

此例中多层嵌套类属性变化后，可以观察到UI更新触发。如果类中的属性也是类类型，且该属性需要被监听，那么这个类也要被 \@Observed 修饰。