### ERR_TRUST_TOKEN_OPERATION_SUCCESS_WITHOUT_SENDING_REQUEST

```cangjie
ERR_TRUST_TOKEN_OPERATION_SUCCESS_WITHOUT_SENDING_REQUEST
```

**功能：** 在处理一个与Trust Tokens协议相关的操作执行请求时，系统能够执行该请求中的Trust Tokens操作，但并没有将请求发送到其指定的目的地。

**起始版本：** 19

### ERR_TUNNEL_CONNECTION_FAILED

```cangjie
ERR_TUNNEL_CONNECTION_FAILED
```

**功能：** 无法建立通过代理的隧道连接。

**起始版本：** 19

### ERR_UNABLE_TO_REUSE_CONNECTION_FOR_PROXY_AUTH

```cangjie
ERR_UNABLE_TO_REUSE_CONNECTION_FOR_PROXY_AUTH
```

**功能：** 在使用AuthController生成凭据之前，尝试重新使用连接发送代理身份验证凭据失败。

**起始版本：** 19

### ERR_UNDOCUMENTED_SECURITY_LIBRARY_STATUS

```cangjie
ERR_UNDOCUMENTED_SECURITY_LIBRARY_STATUS
```

**功能：** 取消文档安全库状态。

**起始版本：** 19

### ERR_UNEXPECTED

```cangjie
ERR_UNEXPECTED
```

**功能：** 遇到了一个未被预期或未被特定处理的问题。

**起始版本：** 19

### ERR_UNEXPECTED_PROXY_AUTH

```cangjie
ERR_UNEXPECTED_PROXY_AUTH
```

**功能：** 意外的代理身份验证。

**起始版本：** 19

### ERR_UNEXPECTED_SECURITY_LIBRARY_STATUS

```cangjie
ERR_UNEXPECTED_SECURITY_LIBRARY_STATUS
```

**功能：** 意外的安全库状态。

**起始版本：** 19

### ERR_UNKNOWN_URL_SCHEME

```cangjie
ERR_UNKNOWN_URL_SCHEME
```

**功能：** 未知 scheme。

**起始版本：** 19

### ERR_UNRECOGNIZED_FTP_DIRECTORY_LISTING_FORMAT

```cangjie
ERR_UNRECOGNIZED_FTP_DIRECTORY_LISTING_FORMAT
```

**功能：** 无法识别的 ftp 目录列表格式。

**起始版本：** 19

### ERR_UNSAFE_PORT

```cangjie
ERR_UNSAFE_PORT
```

**功能：** 不安全的端口。

**起始版本：** 19

### ERR_UNSAFE_REDIRECT

```cangjie
ERR_UNSAFE_REDIRECT
```

**功能：** 不安全的重定向。

**起始版本：** 19

### ERR_UNSUPPORTED_AUTH_SCHEME

```cangjie
ERR_UNSUPPORTED_AUTH_SCHEME
```

**功能：** 不支持的身份验证方案。

**起始版本：** 19

### ERR_UPLOAD_FILE_CHANGED

```cangjie
ERR_UPLOAD_FILE_CHANGED
```

**功能：** 上传文件失败因为文件的修改时间不符合预期。

**起始版本：** 19

### ERR_UPLOAD_STREAM_REWIND_NOT_SUPPORTED

```cangjie
ERR_UPLOAD_STREAM_REWIND_NOT_SUPPORTED
```

**功能：** 上传重传不支持。

**起始版本：** 19

### ERR_WINSOCK_UNEXPECTED_WRITTEN_BYTES

```cangjie
ERR_WINSOCK_UNEXPECTED_WRITTEN_BYTES
```

**功能：** Winsock有时会报告写入的数据多于传递的数据。

**起始版本：** 19

### ERR_WRONG_VERSION_ON_EARLY_DATA

```cangjie
ERR_WRONG_VERSION_ON_EARLY_DATA
```

**功能：** TLS 1.3 early data 版本错误。

**起始版本：** 19

### ERR_WS_PROTOCOL_ERROR

```cangjie
ERR_WS_PROTOCOL_ERROR
```

**功能：** Websocket协议错误。

**起始版本：** 19

### ERR_WS_THROTTLE_QUEUE_TOO_LARGE

```cangjie
ERR_WS_THROTTLE_QUEUE_TOO_LARGE
```

**功能：** 挂起的WebSocketJob实例太多，因此没有将新Job推送到队列中。

**起始版本：** 19

### ERR_WS_UPGRADE

```cangjie
ERR_WS_UPGRADE
```

**功能：** 当WebSocket握手成功完成并且连接已升级时，URLRequest将被取消，并返回此错误代码。

**起始版本：** 19

### NET_OK

```cangjie
NET_OK
```

**功能：** 访问正常。

**起始版本：** 19

### func !=(WebNetErrorList)

```cangjie
public operator func !=(other: WebNetErrorList): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebNetErrorList](#enum-webneterrorlist)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|