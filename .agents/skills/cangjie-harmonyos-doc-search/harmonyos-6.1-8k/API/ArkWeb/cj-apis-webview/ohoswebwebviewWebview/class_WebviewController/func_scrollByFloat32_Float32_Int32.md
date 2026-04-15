### func scrollBy(Float32, Float32, ?Int32)

```cangjie
public func scrollBy(deltaX: Float32, deltaY: Float32, duration!: ?Int32 = None): Unit
```

**功能：** 在指定时间内将页面滚动指定的偏移量。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deltaX|Float32|是|-|水平偏移量，其中水平向右为正方向。<br>单位：vp。|
|deltaY|Float32|是|-|垂直偏移量，其中垂直向下为正方向。<br>单位：vp。|
|duration|?Int32|否|None|**命名参数。** 滚动动画时间。<br>单位：ms。<br>不传入为无动画，当传入数值为负数或传入0时，按照不传入处理。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100001 | Init error. The WebviewController must be associated with a Web component. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkUI.LengthProp
import kit.ArkUI.Button
import kit.ArkUI.Column
import kit.ArkUI.CustomView
import kit.ArkUI.CJEntry
import kit.ArkUI.loadNativeView
import kit.ArkUI.SubscriberManager
import kit.ArkUI.LocalStorage
import ohos.arkui.state_macro_manage.Entry
import ohos.arkui.state_macro_manage.Component
import kit.ArkWeb.*
import kit.ArkUI.Web
import kit.PerformanceAnalysisKit.Hilog

@Entry
@Component
class webview_33 {
    let webController = WebviewController()
    func build() {
        Column(space: 10) {
            Button("scrollBy")
            .onClick ({
                evt =>
                Hilog.info(0, "test", "scrollBy")
                webController.scrollBy(50.0, 50.0)
            }).width(400.px).height(150.px)

            Web(src: ("index.html"), controller: webController)
            .onPageBegin({evt =>
                Hilog.info(0, "test", "page begin url: ${evt.url}")
            })
            .onPageEnd({evt =>
                Hilog.info(0, "test", "page end url: ${evt.url}")
            })
        }
    }
}
```

加载的html文件。需要在`entry\src\main\resources\rawfile`目录下新增`index.html`文件。

```html
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Demo</title>
    <style>
        body {
            width:3000px;
            height:3000px;
            padding-right:170px;
            padding-left:170px;
            border:5px solid blueviolet
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```