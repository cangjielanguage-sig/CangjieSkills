### static func get(String, SnapshotRetCallBack, CJSnapshotOptions)

```cangjie
public static func get(id: String, callback: SnapshotRetCallBack, options!: CJSnapshotOptions = CJSnapshotOptions(1.0, false)): Unit
```

**功能：** 获取已加载的组件的截图，传入组件的[组件标识](./cj-universal-attribute-componentid.md)，找到对应组件进行截图。通过回调返回结果。

> **说明：**
>
> 截图会获取最近一帧的绘制内容。如果在组件触发更新的同时调用截图，更新的渲染内容不会被截取到，截图会返回上一帧的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|String|是|-|目标组件的[组件标识](./cj-universal-attribute-componentid.md)。|
|callback|[SnapshotRetCallBack](#type-snapshotretcallback)|是|-|截图返回结果的回调。|
|options|[CJSnapshotOptions](#class-cjsnapshotoptions)|否|CJSnapshotOptions(1.0, false)| **命名参数。** 截图相关的自定义参数。|

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
    var pixmap1: PixelMap = createPixelMap(color, opts)
    @State
    var errcode1: Int32 = 0
    var inx: Int64 = 0

    func build() {
        Column {
            Row() {
                Image(@r(app.media.startIcon)).autoResize(true).width(100).height(100).margin(5).id("root")
                Image(this.pixmap1).width(100).height(100).border(width: 1.vp).margin(5)
            }

            Button("click to generate UI snapshot").id("generate_UI_snapshot").onClick(
                {
                    =>
                    componentSnapshot.get(
                        componentIdList[inx],
                        {
                            optAsyncError, optPixelMap => match (optAsyncError) {
                                case Some(v) =>
                                    this.errcode1 = v.code
                                    this.pixmap1 = try {
                                        optPixelMap.getOrThrow()
                                    } catch (e: NoneValueException) {
                                        createPixelMap(Array<UInt8>(96, repeat: 100), opts)
                                    }
                                case None =>
                                    this.errcode1 = 0
                                    this.pixmap1 = optPixelMap.getOrThrow()
                            }
                        },
                        options: CJSnapshotOptions(2.0, true)
                    )
                    this.inx = (this.inx + 1) % 2
                }
            ).margin(10)
            Text("${this.errcode1}")
        }
    }
}
```

![componentsnapshot2](figures/componentSnapshot2.gif)