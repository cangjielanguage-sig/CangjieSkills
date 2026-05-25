## class WebResourceHandler

```cangjie
public class WebResourceHandler {}
```

**功能：** 通过WebResourceHandler，可以提供自定义的返回头以及返回体给Web组件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func didFail(WebNetErrorList)

```cangjie
public func didFail(code: WebNetErrorList): Unit
```

**功能：** 通知ArkWeb内核被拦截请求应该返回失败。调用前需要优先调用[didReceiveResponse](#func-didreceiveresponsewebschemehandlerresponse)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|[WebNetErrorList](cj-apis-web-net_error_list.md#enum-webneterrorlist)|是|-|网络错误码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Incorrect parameter types.|
  |17100021|The resource handler is invalid.|

### func didFinish()

```cangjie
public func didFinish(): Unit
```

**功能：** 通知Web组件被拦截的请求已经完成，并且没有更多的数据可用。调用前需要优先调用[didReceiveResponse](#func-didreceiveresponsewebschemehandlerresponse)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100021|The resource handler is invalid.|

### func didReceiveResponse(WebSchemeHandlerResponse)

```cangjie
public func didReceiveResponse(response: WebSchemeHandlerResponse): Unit
```

**功能：** 将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|response|[WebSchemeHandlerResponse](#class-webschemehandlerresponse)|是|-|该拦截请求的响应。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.|
  |17100021|The resource handler is invalid.|

### func didReceiveResponseBody(Array\<UInt8>)

```cangjie
public func didReceiveResponseBody(data: Array<UInt8>): Unit
```

**功能：** 将构造的响应体传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<UInt8>|是|-|响应体数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.|
  |17100021|The resource handler is invalid.|