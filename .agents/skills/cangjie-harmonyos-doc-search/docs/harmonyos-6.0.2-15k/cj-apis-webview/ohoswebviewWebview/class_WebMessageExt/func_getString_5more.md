### func getString()

```cangjie
public func getString(): String
```

**功能：** 获取数据对象的字符串类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

| 类型           | 说明          |
| :--------------| :------------- |
| String | 返回字符串类型的数据。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  | 错误码ID | 错误信息                              |
  | :-------- | :------------------------------------- |
  | 17100014 | The type does not match with the value of the message. |

### func getType()

```cangjie
public func getType(): WebMessageType
```

**功能：** 获取数据对象的类型。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

| 类型           | 说明                                                      |
| :--------------| :--------------------------------------------------------- |
| [WebMessageType](#enum-webmessagetype) | [webMessagePort](#class-webmessageport)接口所支持的数据类型。 |

### func setArray(Array\<String>)

```cangjie
public func setArray(message: Array<String>): Unit
```

**功能：** 设置数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|Array\<String>|是|-|数组类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func setArray(Array\<Int64>)

```cangjie
public func setArray(message: Array<Int64>): Unit
```

**功能：** 设置数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|Array\<Int64>|是|-|数组类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100014|The type does not match with the value of the message.|

### func setArray(Array\<Float64>)

```cangjie
public func setArray(message: Array<Float64>): Unit
```

**功能：** 设置数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|Array\<Float64>|是|-|数组类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100014|The type does not match with the value of the message.|