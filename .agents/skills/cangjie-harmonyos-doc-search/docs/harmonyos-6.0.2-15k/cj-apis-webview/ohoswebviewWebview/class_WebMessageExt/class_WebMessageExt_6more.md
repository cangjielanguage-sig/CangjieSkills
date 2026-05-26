## class WebMessageExt

```cangjie
public class WebMessageExt {
    public init()
}
```

**功能：** [WebMessagePort](#class-webmessageport)接收、发送的数据对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func getError()

```cangjie
public func getError(): Error
```

**功能：** 获取数据对象的错误类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Error](#class-error)|错误类型数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100014|The type does not match with the value of the message.|

### func getArray()

```cangjie
public func getArray(): MessageArrayValue
```

**功能：** 获取数据对象的数组类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

| 类型           | 说明          |
| :--------------| :------------- |
| [MessageArrayValue](#enum-messagearrayvalue) | 返回数组类型的数据。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  | 错误码ID | 错误信息                              |
  | :-------- | :------------------------------------- |
  | 17100014 | The type does not match with the value of the message. |

### func getArrayBuffer()

```cangjie
public func getArrayBuffer(): Array<UInt8>
```

**功能：** 获取数据对象的原始二进制数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

| 类型           | 说明          |
| :--------------| :------------- |
| Array\<UInt8> | 返回原始二进制数据。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  | 错误码ID | 错误信息                              |
  | :-------- | :------------------------------------- |
  | 17100014 | The type does not match with the value of the message. |

### func getBoolean()

```cangjie
public func getBoolean(): Bool
```

**功能：** 获取数据对象的布尔类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

| 类型           | 说明          |
| :--------------| :------------- |
| Bool | 返回布尔类型的数据。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  | 错误码ID | 错误信息                              |
  | :-------- | :------------------------------------- |
  | 17100014 | The type does not match with the value of the message. |

### func getNumber()

```cangjie
public func getNumber(): Float64
```

**功能：** 获取数据对象的数值类型数据。完整示例代码参考[onMessageEventExt](#func-onmessageeventextwebmessageext---unit)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

| 类型           | 说明          |
| :--------------| :------------- |
| Float64 | 返回数值类型的数据。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  | 错误码ID | 错误信息                              |
  | :-------- | :------------------------------------- |
  | 17100014 | The type does not match with the value of the message. |