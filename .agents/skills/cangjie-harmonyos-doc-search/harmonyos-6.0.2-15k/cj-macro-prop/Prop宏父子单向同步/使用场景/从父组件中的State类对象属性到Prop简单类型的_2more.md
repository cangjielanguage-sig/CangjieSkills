### 从父组件中的\@State类对象属性到\@Prop简单类型的同步

在此示例中，图书类使用\@Observed宏，由于class是引用类型，使用\@Observed修饰时在子组件中对class内部变量的修改会影响父组件。因此其中任意一个ReaderComp内属性的变化都会导致book对象的变化。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Book {
    public var title: String
    public var pages: Int64
    @Publish
    public var readIt: Bool = false
}

@Component
class ReaderComp {
    @Prop
    var book: Book
    func build() {
        Row() {
            Text(this.book.title)
            Text("...has${this.book.pages} pages!")
            Text("${this.book.readIt}").fontSize(50.vp).onClick {
                evt => this.book.readIt = true
            }
        }
    }
}

@Entry
@Component
class EntryView {
    @State
    var book: Book = Book(title: '100 secrets of C++', pages: 765)
    func build() {
        Column {
            ReaderComp(book: this.book)
            ReaderComp(book: this.book)
        }
    }
}
```

![Video-Prop-Book](figures/Video-Prop-Book.gif)

### 从父组件中的\@State数组项到\@Prop class类型的同步

在下面的示例中，更改了\@State装饰的allBooks数组中Book对象上的属性，需要使用\@Observed装饰class Book，Book的属性将被感知，并使用ObservedArrayList来观察Book对象的增删改。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Observed
class Book {
    public var title: String
    public var pages: Int64
    @Publish
    public var readIt: Bool = false
}

@Component
class ReaderComp {
    @Prop
    var book: Book
    func build() {
        Row() {
            Text(this.book.title)
            Text("...has${this.book.pages} pages!")
            Text("${this.book.readIt}").onClick {
                evt => this.book.readIt = true
            }
        }.backgroundColor(0x00ff00).width(312).height(40).padding(left: 20, top: 10).borderRadius(20).margin(10)
    }
}

@Entry
@Component
class EntryView {
    @State
    var allBooks: ObservedArrayList<Book> = ObservedArrayList<Book>(
        [Book(title: "JS", pages: 765), Book(title: "Cangjie", pages: 652), Book(title: "ArkUI", pages: 765)])

    func build() {
        Column {
            Text('library`s all time favorite').width(312).height(40).backgroundColor(0x00ff00).borderRadius(20).margin(
                12).padding(left: 20)
            ReaderComp(book: this.allBooks[2])
            Divider()
            Text('Books on loan to a reader').width(312).height(40).backgroundColor(0x00ff00).borderRadius(20).margin(
                12).padding(left: 20)
            ForEach(
                this.allBooks,
                itemGeneratorFunc: {
                    item: Book, _: Int64 => ReaderComp(book: item)
                },
                keyGeneratorFunc: {
                    item: Book, _: Int64 => item.title
                }
            )
            Button("Add new").width(312).height(40).margin(12).onClick(
                {
                evt => this.allBooks.append(Book(title: "JA", pages: 512))
            })
            Button("Remove first book").width(312).height(40).margin(12).onClick(
                {
                evt => if (this.allBooks.size > 0) {
                    this.allBooks.remove(0)
                } else {
                    AppLog.info("length <= 0")
                }
            })
        }
    }
}
```

\@Observed装饰的类的实例会被不透明的代理对象包装，此代理可以检测到包装对象内的所有属性更改。如果发生这种情况，代理通知\@Prop，\@Prop对象值被更新。

![Video-prop-UsageScenario-one](figures/Video-prop-UsageScenario-one.gif)