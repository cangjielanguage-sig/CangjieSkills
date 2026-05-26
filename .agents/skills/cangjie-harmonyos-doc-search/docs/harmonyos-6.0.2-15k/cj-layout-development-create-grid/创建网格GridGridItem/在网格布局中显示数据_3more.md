## 在网格布局中显示数据

网格布局采用二维布局的方式组织其内部元素，如下图5所示。

**图5** 通用办公服务

![GridItem4](figures/GridItem4.png)

Grid组件可以通过二维布局的方式显示一组GridItem子组件。

```cangjie
Grid() {
    GridItem() {
        Text("会议")
          ...
    }

    GridItem() {
        Text("签到")
          ...
    }

    GridItem() {
        Text("投票")
          ...
    }

    GridItem() {
        Text("打印")
          ...
    }
}
.rowsTemplate("1fr 1fr")
.columnsTemplate("1fr 1fr")
```

对于内容结构相似的多个GridItem，通常更推荐使用ForEach语句中嵌套GridItem的形式，来减少重复代码。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    @State
    var services: Array<String> = ["会议", "投票", "签到", "打印"]
    func build() {
        Column() {
            Grid() {
                ForEach(
                    this.services,
                    itemGeneratorFunc: {
                        service: String, _: Int64 => GridItem() {
                            Text(service)
                        }
                    }
                )
            }.rowsTemplate("1fr 1fr").columnsTemplate("1fr 1fr")
        }
    }
}
```

## 设置行列间距

在两个网格单元之间的网格横向间距称为行间距，网格纵向间距称为列间距，如下图6所示。

**图6** 网格的行列间距

![GridItem5](figures/GridItem5.png)

通过Grid的rowsGap和columnsGap可以设置网格布局的行列间距。在图5所示的计算器中，行间距为15.vp，列间距为10.vp。

```cangjie
Grid() {
  ...
}
.columnsGap(10)
.rowsGap(15)
```

## 构建可滚动的网格布局

可滚动的网格布局常用在文件管理、购物或视频列表等页面中，如下图7所示。在设置Grid的行列数量与占比时，如果仅设置行、列数量与占比中的一个，即仅设置rowsTemplate或仅设置columnsTemplate属性，网格单元按照设置的方向排列，超出Grid显示区域后，Grid拥有可滚动能力。

**图7** 横向可滚动网格布局

![GridItem6](figures/GridItem6.gif)

如果设置的是columnsTemplate，Grid的滚动方向为垂直方向；如果设置的是rowsTemplate，Grid的滚动方向为水平方向。

如上图7所示的横向可滚动网格布局，只要设置rowsTemplate属性的值且不设置columnsTemplate属性，当内容超出Grid组件宽度时，Grid可横向滚动进行内容展示。

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    @State
    var services: Array<String> = ["直播", "进口"]
    func build() {
        Column(5) {
            Grid() {
                ForEach(
                    this.services,
                    itemGeneratorFunc: {
                        service: String, _: Int64 => GridItem() {
                        // 添加内容
                        }.width(25.percent)
                    }
                )
            }.rowsTemplate("1fr 1fr").rowsGap(15)
        }
    }
}
```