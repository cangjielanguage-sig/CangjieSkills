### if使用场景

示例代码将OneMoment自定义组件标记为复用组件，List上下滑动，触发OneMoment复用;

 <!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.ArkUI.*
import ohos.arkui.state_management.*
import ohos.arkui.state_macro_manage.*
import std.collection.ArrayList
import kit.PerformanceAnalysisKit.Hilog
import kit.LocalizationKit.*
import ohos.resource.__GenerateResource__

class MyDataSource <: IDataSource<FriendMoment> {
    public MyDataSource(let data_: ArrayList<FriendMoment>) {}
    public var listenerOp: Option<DataChangeListener> = None
    public func totalCount(): Int64 {
        return data_.size
    }
    public func getData(index: Int64): FriendMoment {
        return data_[index]
    }

    public func pushData(val: FriendMoment): Unit {
        data_.add(val)
    }

    public func registerDataChangeListener(listener: DataChangeListener): Unit {
        listenerOp = listener
    }

    public func unregisterDataChangeListener(listener: DataChangeListener): Unit {
        listenerOp = None
    }
}

public class FriendMoment {
    public var text: String = ""
    public var title: String = ""
    public var image: ?AppResource = None
    public init(text: String, title: String, image: ?AppResource) {
        this.text = text
        this.title = title
        this.image = image
    }

}

@Reusable
@Component
public class OneMoment {
    @State var moment: FriendMoment = FriendMoment("", "", @r(app.media.startIcon))
    protected override func aboutToReuse(params: ReuseParams) {
        if (let Some(value) <- params.get<FriendMoment>("moment")) {
            let pVal = value
            this.moment = pVal
            Hilog.info(0, "cangjie", "====aboutToReuse====OnMoment==复用了==== ${pVal.text}")
        }
    }
    public func build() {
        Column() {
            Text(moment.text)
            if (moment.image.isSome()) {
                Flex(wrap: FlexWrap.Wrap) {
                    Image((moment.image) ?? @r(app.media.background)).height(50).width(50)
                    Image((moment.image) ?? @r(app.media.background)).height(50).width(50)
                    Image((moment.image) ?? @r(app.media.background)).height(50).width(50)
                    Image((moment.image) ?? @r(app.media.background)).height(50).width(50)
                }
            }
        }
    }
}

@Entry
@Component
public class EntryView {
    let data: MyDataSource = MyDataSource(ArrayList<FriendMoment>([]))
    protected override func aboutToAppear() {
        for (i in 0..20) {
            let title = "${i+1}test+if"
            data.pushData(FriendMoment("${i}", title, @r(app.media.startIcon)))
        }
        for (i in 0..50) {
            let title = "${i+1}test+if"
            data.pushData(FriendMoment("${i}", title, Option<AppResource>.None))
        }
    }

    public func build(): Unit {
        Column() {
            List() {
                LazyForEach(
                    data,
                    itemGeneratorFunc: {
                        item: FriendMoment, idx: Int64 => ListItem() {
                            OneMoment(moment: item)
                        }
                    }
                )
            }
        }
    }
}
```