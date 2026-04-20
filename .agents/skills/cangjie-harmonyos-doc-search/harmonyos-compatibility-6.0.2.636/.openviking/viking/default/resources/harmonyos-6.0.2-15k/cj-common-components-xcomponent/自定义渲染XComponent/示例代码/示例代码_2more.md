## 示例代码

以下步骤以SURFACE类型为例，描述了如何使用XComponent组件在仓颉侧传入SurfaceId，在Native侧创建NativeWindow实例，然后创建EGL/GLES环境，实现在主页面绘制图形，并可以改变图形的颜色。代码分为仓颉部分和Native部分。

### 仓颉代码

```cangjie
package ohos_app_cangjie_entry

import kit.UIKit.*
import ohos.state_macro_manage.*
import std.convert.*

// 仓颉与Native互操作函数，在cpp/exportffi.cpp中定义

foreign {
    func FFIChangeColor(surfaceId: Int64): Unit

    func FFIDrawPattern(surfaceId: Int64): Unit

    func FFISetSurfaceId(surfaceId: Int64): Unit

    func FFIChangeSurface(surfaceId: Int64, width: Float64, height: Float64): Unit

    func FFIDestroySurface(surfaceId: Int64): Unit

    func FFIGetXComponentHasDraw(surface: Int64): Bool

    func FFIXComponentHasChangeColor(surface: Int64): Bool
}

// 重写XComponentController，设置生命周期回调
class MyXComponentController <: XComponentController {
    protected override func onSurfaceCreated(surfaceId: String) {
        unsafe {
            FFISetSurfaceId(Int64.parse(surfaceId))
        }
    }
    protected override func onSurfaceChanged(surfaceId: String, rect: SurfaceRect) {
        // 在onSurfaceChanged中调用ChangeSurface绘制内容
        unsafe {
            FFIChangeSurface(Int64.parse(surfaceId), 1134.0, 1002.0)
        }
    }

    protected override func onSurfaceDestroyed(surfaceId: String) {
    }
}

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello Cangjie"
    @State
    var hasDraw: Bool = false
    @State
    var hasColorChange: Bool = false
    @State
    var surfaceId: String = ""
    var myXComponentController: MyXComponentController = MyXComponentController()
    func build() {
        Column {
            Text("hasDraw: ${hasDraw}")
            Text("surfaceID: ${surfaceId}")
            Column {
                XComponent(id: "cjtest", `type`: XComponentType.SURFACE, controller: myXComponentController).width(
                    90.percent).height(40.percent)
            }

            Button("GetSurfaceId").onClick {
                evt =>
                AppLog.info("GetSurfaceId start")
                surfaceId = myXComponentController.getXComponentSurfaceId()
            }.fontSize(20).height(40)

            Button("DrawStar").onClick {
                evt =>
                AppLog.info("DrawStar start")
                unsafe {
                    FFIDrawPattern(Int64.parse(surfaceId))
                }
            }.fontSize(20).height(40)

            Button("ChangeColor").onClick {
                evt =>
                AppLog.info("Hello Cangjie")
                unsafe {
                    FFIChangeColor(Int64.parse(surfaceId))
                }
            }.fontSize(20).height(40)

            Button("SetSurfaceId").onClick {
                evt => AppLog.info("Hello Cangjie")
            }.fontSize(20).height(40)
        }.width(100.percent)
    }
}
```