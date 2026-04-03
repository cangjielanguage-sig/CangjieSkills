## 开发布局

### 设置主轴方向

List组件主轴默认是垂直方向，即默认情况下不需要手动设置List方向，就可以构建一个垂直滚动列表。

若是水平滚动列表场景，将List的listDirection属性设置为Axis.Horizontal即可实现。listDirection默认为Axis.Vertical，即主轴默认是垂直方向。

```cangjie
List() {
  // ...
}
.listDirection(Axis.Horizontal)
```

### 设置交叉轴布局

List组件的交叉轴布局可以通过lanes和alignListItem属性进行设置，lanes属性用于确定交叉轴排列的列表项数量，alignListItem用于设置子组件在交叉轴方向的对齐方式。

List组件的lanes属性通常用于在不同尺寸的设备自适应构建不同行数或列数的列表，即一次开发、多端部署的场景。lanes属性的声明方式见[声明方式](../../API_Reference/source_zh_cn/arkui-cj/cj-scroll-swipe-list.md#func-lanesint32)。以垂直列表为例，如果将lanes属性设为2，表示构建的是一个两列的垂直列表，如图2中右图所示。lanes的默认值为1，即默认情况下，垂直列表的列数是1。

```cangjie
List() {
  // ...
}
.lanes(2)
```

当使用".lanes(minLength: Length, maxLength: Length)"声明属性时，表示会根据minLength和maxLength与List组件的尺寸自适应决定行或列数。

```cangjie
List() {
  // ...
}
.lanes(minLength: 200, maxLength: 300)
```

例如，假设在垂直列表中设置了lanes的值为minLength: 200, maxLength: 300。此时：

- 当List组件宽度为300.vp时，由于minLength为200.vp，此时列表为一列。

- 当List组件宽度变化至400.vp时，符合两倍的minLength，则此时列表自适应为两列。

同样以垂直列表为例，当alignListItem属性设置为ListItemAlign.Center表示列表项在水平方向上居中对齐。alignListItem的默认值是ListItemAlign.Start，即列表项在列表交叉轴方向上默认按首部对齐。

```cangjie
List() {
  // ...
}
.alignListItem(ListItemAlign.Center)
```

## 在列表中显示数据

列表视图垂直或水平显示项目集合，在行或列超出屏幕时提供滚动功能，使其适合显示大型数据集合。在最简单的列表形式中，List静态地创建其列表项ListItem的内容。

**图7** 城市列表

![List6](figures/List6.png)

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
public class EntryView {
    func build() {
        List() {
            ListItem() {
                Text('北京').fontSize(24)
            }

            ListItem() {
                Text('杭州').fontSize(24)
            }

            ListItem() {
                Text('上海').fontSize(24)
            }
        }.backgroundColor(0xfff1f3f5).alignListItem(ListItemAlign.Center)
    }
}
```

由于在ListItem中只能有一个根节点组件，不支持以平铺形式使用多个组件。因此，若列表项是由多个组件元素组成的，则需要将这多个元素组合到一个容器组件内或组成一个自定义组件。

**图8** 联系人列表项示例

![List7](figures/List7.png)

如上图8所示，联系人列表的列表项中，每个联系人都有头像和名称。此时，需要将Image和Text封装到一个Row容器内。

```cangjie
List() {
    ListItem() {
        Row() {
            Image(@r(app.media.iconE))
                .width(40)
                .height(40)
                .margin(10)
            Text('小明').fontSize(20)
        }
    }
    ListItem() {
        Row() {
            Image(@r(app.media.iconF))
                .width(40)
                .height(40)
                .margin(10)
            Text('小红').fontSize(20)
        }
    }
}
```