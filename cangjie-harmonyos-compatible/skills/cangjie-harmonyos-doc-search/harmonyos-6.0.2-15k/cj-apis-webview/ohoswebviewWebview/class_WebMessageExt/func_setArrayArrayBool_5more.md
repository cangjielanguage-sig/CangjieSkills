### func setArray(Array\<Bool>)

```cangjie
public func setArray(message: Array<Bool>): Unit
```

**功能：** 设置数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|Array\<Bool>|是|-|数组类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |17100014|The type does not match with the value of the message.|

### func setArrayBuffer(Array\<UInt8>)

```cangjie
public func setArrayBuffer(message: Array<UInt8>): Unit
```

**功能：** 设置数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|Array\<UInt8>|是|-|原始二进制类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func setBoolean(Bool)

```cangjie
public func setBoolean(message: Bool): Unit
```

**功能：** 设置数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|Bool|是|-|布尔类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func setError(Error)

```cangjie
public func setError(message: Error): Unit
```

**功能：** 设置数据对象的错误对象类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|[Error](#class-error)|是|-|错误对象类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func setNumber(Float64)

```cangjie
public func setNumber(message: Float64): Unit
```

**功能：** 设置数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|Float64|是|-|数值类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|