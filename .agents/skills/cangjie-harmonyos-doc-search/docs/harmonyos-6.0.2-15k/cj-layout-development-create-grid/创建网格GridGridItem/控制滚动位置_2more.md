## 控制滚动位置

与新闻列表的返回顶部场景类似，控制滚动位置功能在网格布局中也很常用，例如下图8所示日历的翻页功能。

**图8** 日历翻页

![GridItem7](figures/GridItem7.gif)

Grid组件初始化时，可以绑定一个[Scroller](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-scroll.md#scroll)对象，用于进行滚动控制，例如通过Scroller对象的[scrollPage](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-scroll.md#func-scrollpagebool)方法进行翻页。

```cangjie
var scroller: Scroller = Scroller()
```

在日历页面中，用户在点击“下一页”按钮时，应用响应点击事件，通过指定scrollPage方法的参数next为true，滚动到下一页。

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    var scroller: Scroller = Scroller()
    func build() {
        Column() {
            Grid(this.scroller) {
            // 添加内容
            }.columnsTemplate("1fr 1fr 1fr 1fr 1fr 1fr 1fr").height(85.percent)

            Row() {
                Row() {
                    Button("上一页").onClick {
                        evt => this.scroller.scrollPage(false)
                    }.width(100)
                }.width(50.percent).justifyContent(FlexAlign.Center)

                Row() {
                    Button("下一页").onClick {
                        evt => this.scroller.scrollPage(true)
                    }.width(100)
                }.width(50.percent).justifyContent(FlexAlign.Center)
            }.height(15.percent)
        }.height(100.percent)
    }
}
```

## 性能优化

与长列表的处理类似，[循环渲染](./rendering_control/cj-rendering-control-foreach.md)适用于数据量较小的布局场景，当构建具有大量网格项的可滚动网格布局时，推荐使用[数据懒加载](./rendering_control/cj-rendering-control-lazyforeach.md)方式实现按需迭代加载数据，从而提升列表性能。

关于按需加载优化的具体实现可参考[数据懒加载](./rendering_control/cj-rendering-control-lazyforeach.md)章节中的示例。

当使用懒加载方式渲染网格时，为了更好的滚动体验，减少滑动时出现白块，Grid组件中也可通过cachedCount属性设置GridItem的预加载数量，只在懒加载LazyForEach中生效。

设置预加载数量后，会在Grid显示区域前后各缓存cachedCount\*列数个GridItem，超出显示和缓存范围的GridItem会被释放。

```cangjie
Grid() {
    LazyForEach(this.dataSource, itemGeneratorFunc: {dataSource: T, _: Int64 =>
        GridItem() {
        }
    })
}
.cachedCount(3)
```

> **说明：**
>
> cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。