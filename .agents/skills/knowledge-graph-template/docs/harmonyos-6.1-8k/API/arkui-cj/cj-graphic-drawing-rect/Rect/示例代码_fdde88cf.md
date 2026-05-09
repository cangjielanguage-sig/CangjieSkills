## 示例代码

<!-- run -->

```cangjie
package ohos_app_cangjie_entry
import ohos.base.*
import ohos.arkui.component.*
import ohos.arkui.state_management.*
import ohos.arkui.state_macro_manage.*

@Entry
@Component
class EntryView {
    func build() {
        Column(space: 10) {
            Text("normal").fontSize(11).fontColor(0xCCCCCC).width(90.percent)
            // 绘制90% * 50的矩形
            Column(space: 5) {
                Text("normal").fontSize(9).fontColor(0xCCCCCC).width(90.percent)
                // 绘制90% * 50矩形
                Rect().width(90.percent).height(50).fill(Color.Green)
                // 绘制90% * 50的矩形框
                Rect()
                .width(90.percent)
                .height(50)
                .fillOpacity(0.0)
                .stroke(Color.Red)
                .strokeWidth(3)

                Text("with rounded corners").fontSize(11).fontColor(0xCCCCCC).width(90.percent)
                // 绘制90% * 80的矩形, 圆角宽高分别为40、20
                Rect()
                .width(90.percent)
                .height(50)
                .radiusHeight(20)
                .radiusWidth(40)
                .fill(Color.Green)
                // 绘制90% * 80的矩形, 圆角宽高为20
                Rect()
                .width(90.percent)
                .height(80)
                .radius(20)
                .fill(Color.Green)
                .stroke(Color.Transparent)
            }.width(100.percent).margin(top: 10)
            // 绘制90% * 50矩形, 左上圆角宽高40,右上圆角宽高20,右下圆角宽高40,左下圆角宽高20
            Rect()
            .width(90.percent)
            .height(80)
            .radius([(40, 40), (20, 20), (40, 40), (20, 20)])
            .fill(Color.Green)
        }.width(100.percent).margin(top: 5)
    }
}
```

![rect2](./figures/rect2.png)