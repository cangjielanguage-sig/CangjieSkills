## class WebHttpBodyStream

```cangjie
public class WebHttpBodyStream  {}
```

**功能：** POST、PUT请求的数据体。支持BYTES、FILE、BLOB、CHUNKED类型的数据。

> **说明：**
>
> 本类中其他方法需要在[initialize()](#func-initialize)成功后才能调用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func getPosition()

```cangjie
public func getPosition(): UInt64
```

**功能：** 读取WebHttpBodyStream中当前的位置。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|WebHttpBodyStream中当前的读取位置。|

### func getSize()

```cangjie
public func getSize(): UInt64
```

**功能：** 获取WebHttpBodyStream中的数据大小，分块传输时总是返回零。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|WebHttpBodyStream中的数据大小。|

### func initialize()

```cangjie
public func initialize(): Unit
```

**功能：** 初始化WebHttpBodyStream。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100022|Failed to initialize the HTTP body stream.|

### func isChunked()

```cangjie
public func isChunked(): Bool
```

**功能：** 判断WebHttpBodyStream是否采用分块传输。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|WebHttpBodyStream是否采用分块传输。|

### func isEof()

```cangjie
public func isEof(): Bool
```

**功能：** 判断WebHttpBodyStream中的所有数据是否都已被读取。

如果所有数据都已被读取，则返回true。

对于分块传输类型的WebHttpBodyStream，在第一次读取尝试之前返回false。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|WebHttpBodyStream中的所有数据是否都已被读取。|

### func isInMemory()

```cangjie
public func isInMemory(): Bool
```

**功能：** 判断WebHttpBodyStream中的上传数据是否在内存中。

如果WebHttpBodyStream中的上传数据完全在内存中，并且所有读取请求都将同步成功，则返回true。

对于分块传输类型的数据，预期返回false。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|WebHttpBodyStream中的上传数据是否在内存中。|

### func read(Int32)

```cangjie
public func read(bufLen: Int32): Unit
```

**功能：** 读取WebHttpBodyStream中的数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bufLen|Int32|是|-|WebHttpBodyStream中的字节数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|