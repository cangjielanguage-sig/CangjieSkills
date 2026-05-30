### class WebResourceResponse

```cangjie
public class WebResourceResponse {}
```

**功能：** Web组件资源响应对象。示例代码参考[onHttpErrorReceive](#class-onhttperrorreceiveevent)事件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### func getReasonMessage()

```cangjie
public func getReasonMessage(): String
```

**功能：** 获取资源响应的状态码描述。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回资源响应的状态码描述。|

#### func getResponseCode()

```cangjie
public func getResponseCode(): Int32
```

**功能：** 获取资源响应的状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回资源响应的状态码。|

#### func getResponseData()

```cangjie
public func getResponseData(): String
```

**功能：** 获取资源响应数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回资源响应数据。|

#### func getResponseEncoding()

```cangjie
public func getResponseEncoding(): String
```

**功能：** 获取资源响应的编码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回资源响应的编码。|

#### func getResponseHeader()

```cangjie
public func getResponseHeader(): Array<Header>
```

**功能：** 获取资源响应头。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Header](#class-header)>|返回资源响应头。|

### class WebResult

```cangjie
public class WebResult {}
```

**功能：** 描述Web组件返回的弹窗确认或弹窗取消信息的参数结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func handleCancel()

```cangjie
public func handleCancel(): Unit
```

**功能：** 通知Web组件取消此请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

#### func handleConfirm()

```cangjie
public func handleConfirm(): Unit
```

**功能：** 通知Web组件继续使用SSL证书。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

#### func handlePromptConfirm(String)

```cangjie
public func handlePromptConfirm(result: String): Unit
```

**功能：** 通知Web组件用户确认弹窗操作及对话框内容。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|result|String|是|-|用户输入的对话框内容|