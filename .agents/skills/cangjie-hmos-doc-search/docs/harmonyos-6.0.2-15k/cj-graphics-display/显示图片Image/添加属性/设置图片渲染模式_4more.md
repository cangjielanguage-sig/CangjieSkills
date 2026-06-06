### 设置图片渲染模式

通过renderMode属性设置图片的渲染模式为原色或黑白。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    func build() {
        Column(10) {
            Row(50) {
                Image(@r(app.media.example))
                    // 设置图片的渲染模式为原色
                    .renderMode(ImageRenderMode.Original).width(100).height(100).border(
                    width: 1)
                        // overlay是通用属性，用于在组件上显示说明文字
                        .overlay(title: 'Original', align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0)
                )
                Image(@r(app.media.example))
                    // 设置图片的渲染模式为黑白
                    .renderMode(ImageRenderMode.Template).width(100).height(100).border(
                    width: 1).overlay(title: 'Template', align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0)
                )
            }
        }.height(150).width(100.percent).padding(top: 20, right: 10)
    }
}
```

![image4](figures/image4.png)

### 设置图片解码尺寸

通过sourceSize属性设置图片解码尺寸，降低图片的分辨率。

原图尺寸为1280\*960，该示例将图片解码为40\*40和90\*90。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Row(50) {
                Image(@r(app.media.example)).sourceSize(40, 40).objectFit(ImageFit.ScaleDown).aspectRatio(1).width(
                    25.percent).border(width: 1).overlay(title: 'width:40 height:40', align: Alignment.Bottom,
                    offset: ContentOffset(x: 0.0, y: 40.0))
                Image(@r(app.media.example)).sourceSize(90, 90).objectFit(ImageFit.ScaleDown).width(25.percent).
                    aspectRatio(1).border(width: 1).overlay(title: 'width:90 height:90', align: Alignment.Bottom,
                    offset: ContentOffset(x: 0.0, y: 40.0))
            }.height(150).width(100.percent).padding(20)
        }
    }
}
```

![image5](figures/image5.png)

### 为图片添加滤镜效果

通过colorFilter修改图片的像素颜色，为图片添加滤镜。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    let colorFilter = ColorFilter([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0])
    func build() {
        Column() {
            Row() {
                Image(@r(app.media.example)).width(40.percent).margin(10)
                Image(@r(app.media.example)).width(40.percent).colorFilter(colorFilter).margin(10)
            }.width(100.percent).justifyContent(FlexAlign.Center)
        }
    }
}
```

![image6](figures/image6.png)

### 同步加载图片

一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。但是特定情况下，图片刷新时会出现闪烁，这时可以使用syncLoad属性，使图片同步加载，从而避免出现闪烁。不建议图片加载较长时间时使用，会导致页面无法响应。

```cangjie
Image(@r(app.media.icon))
  .syncLoad(true)
```