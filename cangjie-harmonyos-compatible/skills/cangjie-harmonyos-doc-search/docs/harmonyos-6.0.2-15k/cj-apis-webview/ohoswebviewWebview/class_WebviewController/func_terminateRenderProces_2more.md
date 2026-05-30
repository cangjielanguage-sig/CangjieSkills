### func terminateRenderProcess()

```cangjie
public func terminateRenderProcess(): Bool
```

**功能：** 销毁渲染进程。

调用该接口将会主动销毁相关联的渲染进程。如果渲染进程尚未启动，或者已销毁则没有任何影响。此外销毁渲染进程会同时影响所有与该渲染进程关联的其他实例。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回销毁渲染进程的结果，如果渲染进程可以被销毁则返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100001|Init error. The WebviewController must be associated with a Web component.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("terminateRenderProcess").onClick {
                evt =>
                AppLog.info("terminateRenderProcess")
                let result = webController.terminateRenderProcess()
                AppLog.info("terminateRenderProcess result: ${result}")
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```

### func webPageSnapshot(SnapshotInfo, AsyncCallback\<SnapshotResult>)

```cangjie
public func webPageSnapshot(info: SnapshotInfo, callback: AsyncCallback<SnapshotResult>): Unit
```

**功能：** 获取网页全量绘制结果。（本地资源网页暂不支持）。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[SnapshotInfo](#class-snapshotinfo)|是|-|全量绘制结果入参。|
|callback|[AsyncCallback](../BasicServicesKit/cj-apis-base.md#type-asynccallback)\<[SnapshotResult](#class-snapshotresult)>|是|-|全量绘制回调结果。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*

@Entry
@Component
class EntryView {
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("webPageSnapshot").onClick {
                => try {
                    controller.webPageSnapshot(
                        SnapshotInfo(id: "1234", size: SizeOptions(width: 2.px, height: 2.px)),
                        {
                            error, result =>
                            match (result) {
                                case Some(res) =>
                                    AppLog.info(res.id.getOrThrow())
                                    AppLog.info(res.size.getOrThrow().width.value)
                                    AppLog.info(res.size.getOrThrow().height.value)
                                    AppLog.info(res.size.getOrThrow().width.unitType.getValue())
                                    AppLog.info(res.size.getOrThrow().height.unitType.getValue())
                                    AppLog.info(res.status.getOrThrow())
                                case _ => ()
                            }
                            AppLog.info("callback")
                        }
                    )
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
        }
    }
}
```