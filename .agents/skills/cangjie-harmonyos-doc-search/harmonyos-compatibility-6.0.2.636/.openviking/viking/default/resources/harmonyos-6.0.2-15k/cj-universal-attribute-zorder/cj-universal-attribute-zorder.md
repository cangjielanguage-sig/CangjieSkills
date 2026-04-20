# Z序控制

组件的Z序，设置组件的堆叠顺序。

## func zIndex(Int32)

```cangjie
public func zIndex(value: Int32): This
```

**功能：** 设置组件的堆叠顺序。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。初始值：0。|

## 示例代码

### 示例1（设置组件堆叠顺序）

该示例通过zIndex设置组件堆叠顺序。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column {
            Stack() {
                // stack会重叠组件, 默认后定义的在最上面，具有较高zIndex值的元素在zIndex较小的元素前面
                Text("1, zIndex(2)").size(width: 40.percent, height: 30.percent).backgroundColor(0xbbb2cb).zIndex(2)
                Text("2, default zIndex(1)").size(width: 70.percent, height: 50.percent).backgroundColor(0xd2cab3).align(
                    Alignment.TopStart).zIndex(1)
                Text("3, zIndex(0)").size(width: 90.percent, height: 80.percent).backgroundColor(0xc1cbac).align(
                    Alignment.TopStart)
            }.width(100.percent).height(200)
        }
    }
}
```

![uni_zindex](figures/uni_zindex.png)

### 示例2（动态修改zIndex属性）

该示例使用Button组件动态修改zIndex属性。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    @State
    var zIndex_: Int32 = 0

    func build() {
        Column() {
            Button("change Text2 zIndex").onClick({
                => this.zIndex_ = (this.zIndex_ + 1) % 3
            })
            Stack() {
                // 点击Button改变zIndex后，在点击Button前的层级顺序上根据zIndex进行稳定排序。
                Text("1, zIndex(1)").size(width: 70.percent, height: 50.percent).backgroundColor(0xbbb2cb).zIndex(1)
                Text("2, default zIndex(0), now zIndex:" + this.zIndex_.toString()).size(width: 90.percent,
                    height: 80.percent).backgroundColor(0xd2cab3).align(Alignment.TopStart).zIndex(this.zIndex_)
            }.width(100.percent).height(200)
        }
    }
}
```

不点击Button修改zIndex值的效果。

![zIndex_1](figures/zIndex_1.png)

点击Button动态修改zIndex，使Text1和Text2的zIndex相等，因为在点击Button前的层级顺序上根据zIndex进行稳定排序，层级顺序不发生改变。

![zIndex_2](figures/zIndex_2.png)

点击Button动态修改zIndex，使Text1的zIndex大于Text2，层级发生改变。

![zIndex_3](figures/zIndex_3.png)
