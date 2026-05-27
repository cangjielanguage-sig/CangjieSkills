### func setString(String)

```cangjie
public func setString(message: String): Unit
```

**功能：** 设置数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|String|是|-|字符串类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func setType(WebMessageType)

```cangjie
public func setType(msgType: WebMessageType): Unit
```

**功能：** 设置数据对象的类型。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|msgType|[WebMessageType](#enum-webmessagetype)|是|-|[WebMessagePort](#class-webmessageport)所支持的数据类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|