### static func getSync(String, CJSnapshotOptions)

```cangjie
public static func getSync(id: String, options!: CJSnapshotOptions = CJSnapshotOptions(1.0, false)): PixelMap
```

**功能：** 获取已加载的组件的截图，传入组件的[组件标识](./cj-universal-attribute-componentid.md)，找到对应组件进行截图。同步等待截图完成返回[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|目标组件的[组件标识](./cj-universal-attribute-componentid.md)。|
|options|[CJSnapshotOptions](#class-cjsnapshotoptions)|否|CJSnapshotOptions(1.0, false)| **命名参数。** 截图相关的自定义参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|截图返回的结果。|

**异常：**

- 以下错误码的详细介绍请参见[通用错误码](../errorcodes/cj-errorcode-universal.md)。

|错误码ID|错误信息|
|:---|:---|
|401|Component snapshot getSync failed!|
|100001|Component snapshot getSync failed!|
|160002|Component snapshot getSync failed!|

**示例：**

<!-- run -->

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import ohos.component_utils.ComponentUtils
import ohos.resource_manager.__GenerateResource__
import ohos.image.PixelMap
import ohos.image.createPixelMap
import ohos.image.InitializationOptions
import ohos.image.PixelMapFormat
import ohos.image.Size as UniqueImageSize

@Entry
@Component
class EntryView {
    let color = Array<UInt8>(96, repeat: 100)
    let opts = InitializationOptions(editable: true, pixelFormat: BGRA_8888, size: UniqueImageSize(height: 4, width: 6))
    let componentIdList: Array<String> = ["root", "incorrect_id"]
    @State
    var pixmap3: PixelMap = createPixelMap(color, opts)
    @State
    var errMes: String = ""
    var inx3: Int64 = 0

    func build() {
        Column {
            Row() {
                Image(@r(app.media.startIcon)).autoResize(true).width(100).height(100).margin(5).id("root")
                Image(this.pixmap3).width(100).height(100).border(width: 1.vp).margin(5)
            }

            Button("click to generate UI snapshot synchronously").onClick(
                {
                    =>
                    try {
                        let pixmap = componentSnapshot.getSync(
                            componentIdList[inx3],
                            options: CJSnapshotOptions(2.0, true)
                        )
                        this.pixmap3 = pixmap
                        this.errMes = "no error"
                    } catch (e: BusinessException) {
                        this.pixmap3 = createPixelMap(Array<UInt8>(96, {i => UInt8(i + 1)}), opts)
                        this.errMes = "${e.message} code: ${e.code}"
                    }
                    this.inx3 = (this.inx3 + 1) % 2
                }
            ).margin(10)
            Text(this.errMes)
        }
    }
}
```

![componentsnapshot3](figures/componentSnapshot3.gif)