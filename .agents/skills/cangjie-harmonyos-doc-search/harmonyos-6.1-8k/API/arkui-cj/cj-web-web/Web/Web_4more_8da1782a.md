# Web

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

提供具有网页显示能力的Web组件，[@ohos.web.webview](../ArkWeb/cj-apis-webview.md)提供web控制能力。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(ResourceStr, WebviewController)

```cangjie
public init(
    src!: ResourceStr,
    controller!: WebviewController
)
```

**功能：** 创建一个Web组件。

> **说明：**
>
> - 不支持转场动画。
> - 同一页面的多个Web组件，必须绑定不同的WebviewController。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| **命名参数。** src不能通过状态变量（例如：@State）动态更改地址。|
|controller|[WebviewController](../ArkWeb/cj-apis-webview.md#class-webviewcontroller)|是|-| **命名参数。** 设置Web控制器。|