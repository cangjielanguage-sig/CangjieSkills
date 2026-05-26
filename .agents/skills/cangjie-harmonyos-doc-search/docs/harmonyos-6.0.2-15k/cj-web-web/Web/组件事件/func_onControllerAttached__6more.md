### func onControllerAttached(() -> Unit)

```cangjie
public func onControllerAttached(callback: () -> Unit): This
```

**功能：** 当Controller成功绑定到Web组件时触发该回调，并且该Controller必须为WebviewController，且禁止在该事件回调前调用Web组件相关的接口，否则会抛出异常。因该回调调用时网页还未加载，无法在回调中使用有关操作网页的接口，例如[zoomIn](../apis/ArkWeb/cj-apis-webview.md)、[zoomOut](../apis/ArkWeb/cj-apis-webview.md)等，可以使用[loadUrl](../apis/ArkWeb/cj-apis-webview.md)、[getWebId](../apis/ArkWeb/cj-apis-webview.md)等操作网页不相关的接口。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，当Controller成功绑定到Web组件时触发该回调。|

### func onDownloadStart((OnDownloadStartEvent) -> Unit)

```cangjie
public func onDownloadStart(callback: (OnDownloadStartEvent) -> Unit): This
```

**功能：** 通知主应用开始下载一个文件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnDownloadStartEvent](#class-ondownloadstartevent))->Unit|是|-|开始下载时触发。|

### func onErrorReceive((OnErrorReceiveEvent) -> Unit)

```cangjie
public func onErrorReceive(callback: (OnErrorReceiveEvent) -> Unit): This
```

**功能：** 网页加载遇到错误时触发该回调。主资源与子资源出错都会回调该接口，可以通过request.isMainFrame来判断是否是主资源报错。出于性能考虑，建议此回调中尽量执行简单逻辑。在无网络的情况下，触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnErrorReceiveEvent](#class-onerrorreceiveevent))->Unit|是|-|回调函数，网页收到 Web 资源加载错误时触发。|

### func onLoadIntercept((WebResourceRequest) -> Bool)

```cangjie
public func onLoadIntercept(callback: (WebResourceRequest) -> Bool): This
```

**功能：** 当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。默认允许加载。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([WebResourceRequest](#class-webresourcerequest))->Bool|是|-|回调函数，截获资源加载时触发的回调。<br> 返回值boolean。返回true表示阻止此次加载，否则允许此次加载。|

### func onPageBegin((OnPageEvent) -> Unit)

```cangjie
public func onPageBegin(callback: (OnPageEvent) -> Unit): This
```

**功能：** 网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnPageEvent](#class-onpageevent))->Unit|是|-|回调函数，网页加载开始时触发回调。|

### func onPageEnd((OnPageEvent) -> Unit)

```cangjie
public func onPageEnd(callback: (OnPageEvent) -> Unit): This
```

**功能：** 网页加载完成时触发该回调，且只在主frame触发。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OnPageEvent](#class-onpageevent))->Unit|是|-|网页加载结束时触发。|