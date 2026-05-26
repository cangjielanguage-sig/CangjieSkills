## 添加属性

给Image组件设置属性可以使图片显示更灵活，达到一些自定义的效果。以下是几个常用属性的使用示例，完整属性信息详见[Image](../../API_Reference/source_zh_cn/arkui-cj/cj-image-video-image.md)。

### 设置图片缩放类型

通过objectFit属性使图片缩放到高度和宽度确定的框内。

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.resource_manager.*

@Entry
@Component
class EntryView {
    let scroller: Scroller = Scroller()
    func build() {
        Scroll(this.scroller) {
            Column() {
                Row() {
                    Image(@r(app.media.example)).width(160).height(120).border(width: 1)
                        // 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。
                        .objectFit(ImageFit.Contain).
                        margin(15).overlay(title: 'Contain', align: Alignment.Bottom,
                        offset: ContentOffset(x: 0.0, y: 20.0))
                    Image(@r(app.media.example)).width(160).height(120).border(width: 1)
                        // 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。
                        .objectFit(ImageFit.Cover).
                        margin(15).overlay(title: 'Cover', align: Alignment.Bottom,
                        offset: ContentOffset(x: 0.0, y: 20.0))
                }
                Row() {
                    Image(@r(app.media.example)).width(160).height(120).border(width: 1)
                        // 自适应显示。
                        .objectFit(ImageFit.Auto).margin(
                        15).overlay(title: 'Auto', align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0))
                    Image(@r(app.media.example)).width(160).height(80).border(width: 1)
                        // 不保持宽高比进行放大缩小，使得图片充满显示边界。
                        .objectFit(ImageFit.Fill).margin(
                        15).overlay(title: 'Fill', align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0))
                }
                Row() {
                    Image(@r(app.media.example)).width(160).height(120).border(width: 1)
                        // 保持宽高比显示，图片缩小或者保持不变。
                        .objectFit(ImageFit.ScaleDown).
                        margin(15).overlay(title: 'ScaleDown', align: Alignment.Bottom,
                        offset: ContentOffset(x: 0.0, y: 20.0))
                    Image(@r(app.media.example)).width(160).height(80).border(width: 1)
                        // 保持原有尺寸显示。
                        .objectFit(ImageFit.None).margin(
                        15).overlay(title: 'None', align: Alignment.Bottom, offset: ContentOffset(x: 0.0, y: 20.0))
                }
            }
        }
    }
}
```

![image1](figures/image1.png)