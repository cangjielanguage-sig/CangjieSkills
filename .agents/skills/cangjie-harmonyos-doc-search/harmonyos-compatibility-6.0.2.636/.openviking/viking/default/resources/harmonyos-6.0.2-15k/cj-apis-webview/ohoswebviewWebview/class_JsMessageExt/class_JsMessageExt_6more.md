## class JsMessageExt

```cangjie
public class JsMessageExt {}
```

**功能：** [runJavaScirptExt](#func-runjavascriptextstring-asynccallbackjsmessageext)执行脚本返回的数据对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func getArray()

```cangjie
public func getArray(): MessageArrayValue
```

**功能：** 获取数据对象的数组类型。完整示例代码参考[runJavaScirptExt](#func-runjavascriptextstring-asynccallbackjsmessageext)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[MessageArrayValue](#enum-messagearrayvalue)|返回数组类型的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func getArrayBuffer()

```cangjie
public func getArrayBuffer(): Array<UInt8>
```

**功能：** 获取数据对象的原始二进制数据。完整示例代码参考[runJavaScirptExt](#func-runjavascriptextstring-asynccallbackjsmessageext)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|返回原始二进制数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func getBoolean()

```cangjie
public func getBoolean(): Bool
```

**功能：** 获取数据对象的布尔类型数据。完整示例代码参考[runJavaScirptExt](#func-runjavascriptextstring-asynccallbackjsmessageext)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回布尔类型的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func getNumber()

```cangjie
public func getNumber(): Float64
```

**功能：** 获取数据对象的数值类型数据。完整示例代码参考[runJavaScirptExt](#func-runjavascriptextstring-asynccallbackjsmessageext)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float64|返回数值类型的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func getString()

```cangjie
public func getString(): String
```

**功能：** 获取数据对象的字符串类型数据。完整示例代码参考[runJavaScirptExt](#func-runjavascriptextstring-asynccallbackjsmessageext)。

**系统能力：** SystemCapability.Web.Webview.Co1re

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串类型的数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|