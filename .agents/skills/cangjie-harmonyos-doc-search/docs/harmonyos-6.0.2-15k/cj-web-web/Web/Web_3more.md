# Web

提供具有网页显示能力的Web组件，[@ohos.web.webview](../apis/ArkWeb/cj-apis-webview.md)提供web控制能力。

## 子组件

无

## 创建组件

### init(String, WebviewController)

```cangjie
public init(
    src!: String = "",
    controller!: WebviewController = WebviewController()
)
```

**功能：** 创建一个Web组件。

> **说明：**
>
> - 不支持转场动画。
> - 同一页面的多个Web组件，必须绑定不同的WebviewController。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|否|""| **命名参数。** src不能通过状态变量（例如：@State）动态更改地址。|
|controller|[WebviewController](../apis/ArkWeb/cj-apis-webview.md#class-webviewcontroller)|否|WebviewController()| **命名参数。** 设置Web控制器。|

### init(AppResource, WebviewController)

```cangjie
public init(
    src!: AppResource,
    controller!: WebviewController = WebviewController()
)
```

**功能：** 创建一个Web组件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 网页资源地址。如果访问本地资源文件，请使用@rawfile或者resource协议。如果加载应用包外沙箱路径的本地资源文件，请使用file://沙箱文件路径。|
|controller|[WebviewController](../apis/ArkWeb/cj-apis-webview.md#class-webviewcontroller)|否|WebviewController()| **命名参数。**  设置Web控制器。|