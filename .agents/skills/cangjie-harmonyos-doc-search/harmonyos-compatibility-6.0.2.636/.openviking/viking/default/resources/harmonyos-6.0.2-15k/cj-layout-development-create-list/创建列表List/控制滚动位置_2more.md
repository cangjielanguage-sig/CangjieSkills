## 控制滚动位置

控制滚动位置在实际应用中十分常见，例如当新闻页列表项数量庞大，用户滚动列表到一定位置时，希望快速滚动到列表底部或返回列表顶部。此时，可以通过控制滚动位置来实现列表的快速定位，如下图13所示。

**图13** 返回列表顶部

![List12](figures/List12.gif)

List组件初始化时，可以通过scroller参数绑定一个[Scroller](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-scroll.md)对象，进行列表的滚动控制。例如，用户在新闻应用中，点击新闻页面底部的返回顶部按钮时，就可以通过Scroller对象的scrollToIndex方法使列表滚动到指定的列表项索引位置。

首先，需要创建一个Scroller的对象listScroller。

```cangjie
var listScroller: Scroller = Scroller()
```

然后，通过将listScroller用于初始化List组件的scroller参数，完成listScroller与列表的绑定。在需要跳转的位置指定scrollToIndex的参数为0，表示返回列表顶部。

```cangjie
Stack(Alignment.Bottom) {
    List(space: 20, scroller: this.listScroller) {
        // ...
    }
}

Button() {
    // ...
}
.onClick({ event =>
    this.listScroller.scrollToIndex(0)
})
```

## 响应滚动位置

许多应用需要监听列表的滚动位置变化并作出响应。例如，在联系人列表滚动时，如果跨越了不同字母开头的分组，则侧边字母索引栏也需要更新到对应的字母位置。

除了字母索引之外，滚动列表结合多级分类索引在应用开发过程中也很常见，例如购物应用的商品分类页面，多级分类也需要监听列表的滚动位置。

**图14** 字母索引响应联系人列表滚动

![List13](figures/List13.gif)

如上图14所示，当联系人列表从A滚动到B时，右侧索引栏也需要同步从选中A状态变成选中B状态。此场景可以通过监听List组件的onScrollIndex事件来实现，右侧索引栏需要使用字母表索引组件[AlphabetIndexer](../../API_Reference/source_zh_cn/arkui-cj/cj-information-display-alphabetindexer.md)。

在列表滚动时，根据列表此时所在的索引值位置firstIndex，重新计算字母索引栏对应字母的位置selectedIndex。由于AlphabetIndexer组件通过selected属性设置了选中项索引值，当selectedIndex变化时会触发AlphabetIndexer组件重新渲染，从而显示为选中对应字母的状态。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
public class EntryView {
    let alphabets = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    @State
    var selectedIndex: UInt32 = 0;
    private var listScroller: Scroller = Scroller()

    func build() {
        Stack(Alignment.End) {
            List(scroller: this.listScroller) {}.onScrollIndex({
                firstIndex, scrollState =>
            // 根据列表滚动到的索引值，重新计算对应联系人索引栏的位置this.selectedIndex
            })

            // 字母表索引组件
            AlphabetIndexer(arrayValue: this.alphabets, selected: 0).selected(this.selectedIndex)
        }
    }
}
```

> **说明：**
>
> 计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。