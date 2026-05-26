## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](../../API_Reference/source_zh_cn/arkui-cj/cj-blank-divider-blank.md)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Row() {
                Text('Bluetooth').fontSize(18)
                Blank()
                Toggle(ToggleType.SwitchType, isOn: true)
            }.backgroundColor(0xFFFFFF).borderRadius(15).padding(left: 12).width(100.percent)
        }.backgroundColor(0xEFEFEF).padding(20).width(100.percent)
    }
}
```

**图9** 自适应拉伸下的竖屏

![Column19](figures/Column19.PNG)

**图10** 自适应拉伸下的横屏

![Column20](figures/Column20.png)

## 自适应缩放

自适应缩放是指子元素随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

- 父容器尺寸确定时，使用layoutWeight属性设置子元素和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

  <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      func build() {
          Column() {
              Text('1:2:3').width(100.percent)
              Row() {
                  Column() {
                      Text('layoutWeight(1)').textAlign(TextAlign.Center)
                  }.layoutWeight(1).backgroundColor(0xF5DEB3).height(100.percent)
                  Column() {
                      Text('layoutWeight(2)').textAlign(TextAlign.Center)
                  }.layoutWeight(2).backgroundColor(0xD2B48C).height(100.percent)
                  Column() {
                      Text('layoutWeight(3)').textAlign(TextAlign.Center)
                  }.layoutWeight(3).backgroundColor(0xF5DEB3).height(100.percent)
              }.backgroundColor(0xffd306).height(30.percent)
              Text('2:5:3').width(100.percent)
              Row() {
                  Column() {
                      Text('layoutWeight(2)').textAlign(TextAlign.Center)
                  }.layoutWeight(2).backgroundColor(0xF5DEB3).height(100.percent)
                  Column() {
                      Text('layoutWeight(5)').textAlign(TextAlign.Center)
                  }.layoutWeight(5).backgroundColor(0xD2B48C).height(100.percent)
                  Column() {
                      Text('layoutWeight(3)').textAlign(TextAlign.Center)
                  }.layoutWeight(3).backgroundColor(0xF5DEB3).height(100.percent)
              }.backgroundColor(0xffd306).height(30.percent)
          }
      }
  }
  ```

  **图11** 自定义缩放下使用layoutWeight属性设置的横屏

  ![Column21](figures/Column21.png)

  **图12** 自定义缩放下使用layoutWeight属性设置的竖屏

  ![Column22](figures/Column22.png)

- 父容器尺寸确定时，使用百分比设置子元素和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。

  <!-- run -->

  ```cangjie
  package ohos_app_cangjie_entry

  import kit.UIKit.*
  import ohos.state_macro_manage.*

  @Entry
  @Component
  class EntryView {
      func build() {
          Column() {
              Row() {
                  Column() {
                      Text('left width 20%').textAlign(TextAlign.Center)
                  }.width(20.percent).backgroundColor(0xF5DEB3).height(100.percent)
                  Column() {
                      Text('center width 50%').textAlign(TextAlign.Center)
                  }.width(50.percent).backgroundColor(0xD2B48C).height(100.percent)
                  Column() {
                      Text('right width 30%').textAlign(TextAlign.Center)
                  }.width(30.percent).backgroundColor(0xF5DEB3).height(100.percent)
              }.backgroundColor(0xffd306).height(30.percent)
          }
      }
  }
  ```

  **图13** 自定义缩放下使用百分比设置的横屏

  ![Column23](figures/Column23.png)

  **图14** 自定义缩放下使用百分比设置的竖屏

  ![Column24](figures/Column24.png)