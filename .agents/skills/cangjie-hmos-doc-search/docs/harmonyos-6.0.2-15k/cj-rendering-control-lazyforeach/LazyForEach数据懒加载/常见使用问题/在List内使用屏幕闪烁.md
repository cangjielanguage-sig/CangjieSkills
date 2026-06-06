### 在List内使用屏幕闪烁

在List的onScrollIndex方法中调用onDataReloaded有产生屏幕闪烁的风险。

```cangjie
/** BasicDataSource代码见文档末尾附件: 泛型类型数组的BasicDataSource代码 **/

class MyDataSource <: BasicDataSource<String> {
    public MyDataSource(let data: ArrayList<String>) {
        super(data)
    }

    public func pushData(stringData: String): Unit {
        this.data.add(stringData)
        this.notifyDataAdd(this.data.size - 1)
    }

    public func operateData(): Unit {
        let totalCount = this.data.size
        let batch = 5
        for (i in totalCount..totalCount + batch) {
            this.data.add("Hello ${i}")
        }
        this.notifyDataReload()
    }
}

@Entry
@Component
public class EntryView {
    let dataSource: MyDataSource = MyDataSource(ArrayList<String>())

    protected override func aboutToAppear() {
        for (i in 0..10) {
            this.dataSource.pushData("Hello ${i}")
        }
    }

    public func build(): Unit {
        Column() {
            List(space: 3) {
                LazyForEach(
                    dataSource,
                    itemGeneratorFunc: {
                        item: String, index: Int64 => ListItem() {
                            Text(item).width(100.percent).height(80).backgroundColor(Color.GREY).fontSize(30)
                        }.margin(left: 10, right: 10)
                    }
                )
            }.cachedCount(10).onScrollIndex(
                {
                start: Int32, end: Int32, center: Int32 => if (Int64(end) == this.dataSource.totalCount() - 1) {
                    this.dataSource.operateData()
                }
            })
        }.height(100.percent).height(100.percent)
    }
}
```

当List下拉到底的时候，屏闪效果如下图。

![lazyforeach](figures/lazyforeach-13.gif)

用onDatasetChange代替onDataReloaded，不仅可以修复闪屏的问题，还能提升加载性能。

```cangjie
/** BasicDataSource代码见文档末尾附件: 泛型类型数组的BasicDataSource代码 **/

class MyDataSource <: BasicDataSource<String> {
    public MyDataSource(let data: ArrayList<String>) {
        super(data)
    }

    public func pushData(stringData: String): Unit {
        this.data.add(stringData)
        this.notifyDataAdd(this.data.size - 1)
    }

    public func operateData(): Unit {
        let totalCount = this.data.size
        let batch = 5
        for (i in totalCount..totalCount + batch) {
            this.data.add("Hello ${i}")
        }
        this.notifyDatasetChange(
            ArrayList<DataOperation>([DataAddOperation(Int32(totalCount - 1), count: Int32(batch), key: "", keys: [""])]
        ))
    }
}

@Entry
@Component
public class EntryView {
    let dataSource: MyDataSource = MyDataSource(ArrayList<String>())

    protected override func aboutToAppear() {
        for (i in 0..10) {
            this.dataSource.pushData("Hello ${i}")
        }
    }

    public func build(): Unit {
        Column() {
            List(space: 3) {
                LazyForEach(
                    dataSource,
                    itemGeneratorFunc: {
                        item: String, index: Int64 => ListItem() {
                            Text(item).width(100.percent).height(80).backgroundColor(Color.GREY).fontSize(30)
                        }.margin(left: 10, right: 10)
                    }
                )
            }.cachedCount(10).onScrollIndex(
                {
                start: Int32, end: Int32, center: Int32 => if (Int64(end) == this.dataSource.totalCount() - 1) {
                    this.dataSource.operateData()
                }
            })
        }.height(100.percent).height(100.percent)
    }
}
```

![lazyforeach](figures/lazyforeach-14.gif)