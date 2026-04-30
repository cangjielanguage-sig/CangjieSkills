### 非首次渲染

当LazyForEach数据源发生变化，需要再次渲染时，开发者应根据数据源的变化情况调用listener对应的接口，通知LazyForEach做相应的更新，各使用场景如下。

#### 添加数据

```cangjie
/** BasicDataSource代码见文档末尾附件: 泛型类型数组的BasicDataSource代码 **/

class MyDataSource <: BasicDataSource<String> {
    public MyDataSource(let data: ArrayList<String>) {
        super(data)
    }

    public func pushData(str: String): Unit {
        this.data.add(str)
        this.notifyDataAdd(this.data.size - 1)
    }
}

@Entry
@Component
public class EntryView {
    let dataSource: MyDataSource = MyDataSource(ArrayList<String>())
    let random: Random = Random(3)

    public func build(): Unit {
        Column() {
            Row() {
                Button("load Data").onClick({
                    => for (i in 0..10) {
                        dataSource.pushData(i.toString())
                    }
                })

                Button("add Data").onClick({
                    =>
                    // 点击追加子组件
                    dataSource.pushData(dataSource.totalCount().toString())
                })
            }
            List(space: 3) {
                LazyForEach(
                    dataSource,
                    itemGeneratorFunc: {
                        item: String, index: Int64 => ListItem() {
                            Text("item[${index}]: ${item}").fontSize(30)
                        }
                    }
                )
            }.cachedCount(5)
        }.height(100.percent).height(100.percent)
    }
}
```

当我们点击“add Data”按钮时，首先会调用数据源dataSource的pushData方法，该方法会在数据源末尾添加数据并调用notifyDataAdd方法。在notifyDataAdd方法内又会调用listenerItem.onDataAdd方法，该方法会通知LazyForeach在该处有数据添加，LazyForeach便会在该索引处新建子组件。

运行效果如下图所示。

**图3** LazyForEach添加数据

![lazyforeach-1](./figures/lazyforeach-1.gif)

#### 删除数据

```cangjie
/** BasicDataSource代码见文档末尾附件: 泛型类型数组的BasicDataSource代码 **/

class MyDataSource <: BasicDataSource<String> {
    public MyDataSource(let data: ArrayList<String>) {
        super(data)
    }

    public func pushData(str: String): Unit {
        this.data.add(str)
        this.notifyDataAdd(this.data.size - 1)
    }

    public func deleteData(index: Int64): Unit {
        this.data.remove(at: index)
        this.notifyDataDelete(index)
    }

    public func getAllData(): ArrayList<String> {
        return data
    }
}

@Entry
@Component
public class EntryView {
    let dataSource: MyDataSource = MyDataSource(ArrayList<String>())

    func findIndex(arrayList: ArrayList<String>, value: String): Int64 {
        for (i in 0..arrayList.size) {
            if (arrayList[i] == value) {
                return i
            }
        }
        return -1
    }

    public func build(): Unit {
        Column() {
            Row() {
                Button("load Data").onClick({
                    => for (i in 0..100) {
                        dataSource.pushData(i.toString())
                    }
                })
            }
            List(space: 3) {
                LazyForEach(
                    dataSource,
                    itemGeneratorFunc: {
                        item: String, index: Int64 => ListItem() {
                            Text("item[${index}]: ${item}").fontSize(30)
                        }.onClick({
                            _ =>
                            // 点击删除子组件
                            this.dataSource.deleteData(findIndex(this.dataSource.getAllData(), item))
                        })
                    },
                    keyGeneratorFunc: {item: String, index: Int64 => return item}
                )
            }.cachedCount(5)
        }.height(100.percent).height(100.percent)
    }
}
```

当我们点击ListItem元素时，首先会调用数据源dataSource的deleteData方法，该方法会在数据源末尾添加数据并调用notifyDataDelete方法。在notifyDataDelete方法内又会调用listenerItem.onDataDelete方法，该方法会通知LazyForeach在该处有数据添加，LazyForeach便会在该索引处删除子组件。

运行效果如下图所示。

**图4** LazyForEach删除数据

![lazyforeach-4](./figures/lazyforeach-4.gif)