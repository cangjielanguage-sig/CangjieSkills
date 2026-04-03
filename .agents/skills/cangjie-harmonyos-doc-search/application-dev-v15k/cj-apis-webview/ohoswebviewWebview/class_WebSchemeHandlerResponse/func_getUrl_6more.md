### func getUrl()

```cangjie
public func getUrl(): String
```

**功能：** 获取重定向或由于HSTS而更改后的URL。如果想获取url来做JavascriptProxy通信接口认证，请使用[getLastJavascriptProxyCallingFrameUrl](#func-getlastjavascriptproxycallingframeurl)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|获取经过重定向或由于HSTS而更改后的URL。|

### func setEncoding(String)

```cangjie
public func setEncoding(encoding: String): Unit
```

**功能：** 给当前的WebSchemeHandlerResponse设置字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|encoding|String|是|-|字符集。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Incorrect parameter types.|

### func setHeaderByName(String, String, Bool)

```cangjie
public func setHeaderByName(name: String, value: String, overwrite: Bool): Unit
```

**功能：** 给当前的WebSchemeHandlerResponse设置头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|头部（header）的名称。|
|value|String|是|-|头部（header）的值。|
|overwrite|Bool|是|-|如果为true，将覆盖现有的头部，否则不覆盖。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

### func setMimeType(String)

```cangjie
public func setMimeType(mimeType: String): Unit
```

**功能：** 给当前的WebSchemeHandlerResponse设置媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|媒体类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Incorrect parameter types.|

### func setNetErrorCode(WebNetErrorList)

```cangjie
public func setNetErrorCode(code: WebNetErrorList): Unit
```

**功能：** 给当前的WebSchemeHandlerResponse设置网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|[WebNetErrorList](cj-apis-web-net_error_list.md#enum-webneterrorlist)|是|-|网络错误码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

### func setStatus(Int32)

```cangjie
public func setStatus(status: Int32): Unit
```

**功能：** 给当前的WebSchemeHandlerResponse设置HTTP状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|status|Int32|是|-|Http状态码。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Incorrect parameter types.|