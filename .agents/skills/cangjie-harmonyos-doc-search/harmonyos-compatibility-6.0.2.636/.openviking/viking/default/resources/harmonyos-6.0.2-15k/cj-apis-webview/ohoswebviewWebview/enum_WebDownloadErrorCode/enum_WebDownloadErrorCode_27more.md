## enum WebDownloadErrorCode

```cangjie
public enum WebDownloadErrorCode <: Equatable<WebDownloadErrorCode> & ToString {
    | ERROR_UNKNOWN
    | FILE_FAILED
    | FILE_ACCESS_DENIED
    | FILE_NO_SPACE
    | FILE_NAME_TOO_LONG
    | FILE_TOO_LARGE
    | FILE_TRANSIENT_ERROR
    | FILE_BLOCKED
    | FILE_TOO_SHORT
    | FILE_HASH_MISMATCH
    | FILE_SAME_AS_SOURCE
    | NETWORK_FAILED
    | NETWORK_TIMEOUT
    | NETWORK_DISCONNECTED
    | NETWORK_SERVER_DOWN
    | NETWORK_INVALID_REQUEST
    | SERVER_FAILED
    | SERVER_NO_RANGE
    | SERVER_BAD_CONTENT
    | SERVER_UNAUTHORIZED
    | SERVER_CERT_PROBLEM
    | SERVER_FORBIDDEN
    | SERVER_UNREACHABLE
    | SERVER_CONTENT_LENGTH_MISMATCH
    | SERVER_CROSS_ORIGIN_REDIRECT
    | USER_CANCELED
    | USER_SHUTDOWN
    | CRASH
    | ...
}
```

**功能：** 下载任务的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<WebDownloadErrorCode>
- ToString

### CRASH

```cangjie
CRASH
```

**功能：** 应用发生了崩溃。

**起始版本：** 19

### ERROR_UNKNOWN

```cangjie
ERROR_UNKNOWN
```

**功能：** 未知的错误。

**起始版本：** 19

### FILE_ACCESS_DENIED

```cangjie
FILE_ACCESS_DENIED
```

**功能：** 没有权限访问文件。

**起始版本：** 19

### FILE_BLOCKED

```cangjie
FILE_BLOCKED
```

**功能：** 由于某些本地策略，文件被阻止访问。

**起始版本：** 19

### FILE_FAILED

```cangjie
FILE_FAILED
```

**功能：** 常规文件操作失败。

**起始版本：** 19

### FILE_HASH_MISMATCH

```cangjie
FILE_HASH_MISMATCH
```

**功能：** 哈希不匹配。

**起始版本：** 19

### FILE_NAME_TOO_LONG

```cangjie
FILE_NAME_TOO_LONG
```

**功能：** 文件名字过长。

**起始版本：** 19

### FILE_NO_SPACE

```cangjie
FILE_NO_SPACE
```

**功能：** 磁盘没有足够的空间。

**起始版本：** 19

### FILE_SAME_AS_SOURCE

```cangjie
FILE_SAME_AS_SOURCE
```

**功能：** 文件已存在。

**起始版本：** 19

### FILE_TOO_LARGE

```cangjie
FILE_TOO_LARGE
```

**功能：** 文件太大。

**起始版本：** 19

### FILE_TOO_SHORT

```cangjie
FILE_TOO_SHORT
```

**功能：** 当尝试恢复下载时，发现文件不够长，可能该文件已不存在。

**起始版本：** 19

### FILE_TRANSIENT_ERROR

```cangjie
FILE_TRANSIENT_ERROR
```

**功能：** 出现了一些临时问题，例如内存不足、文件正在使用以及同时打开的文件过多。

**起始版本：** 19

### NETWORK_DISCONNECTED

```cangjie
NETWORK_DISCONNECTED
```

**功能：** 网络断开连接。

**起始版本：** 19

### NETWORK_FAILED

```cangjie
NETWORK_FAILED
```

**功能：** 一般网络错误。

**起始版本：** 19

### NETWORK_INVALID_REQUEST

```cangjie
NETWORK_INVALID_REQUEST
```

**功能：** 无效的网络请求，可能重定向到不支持的方案或无效的URL。

**起始版本：** 19

### NETWORK_SERVER_DOWN

```cangjie
NETWORK_SERVER_DOWN
```

**功能：** 服务器关闭。

**起始版本：** 19

### NETWORK_TIMEOUT

```cangjie
NETWORK_TIMEOUT
```

**功能：** 网络超时。

**起始版本：** 19

### SERVER_BAD_CONTENT

```cangjie
SERVER_BAD_CONTENT
```

**功能：** 服务器没有请求的数据。

**起始版本：** 19

### SERVER_CERT_PROBLEM

```cangjie
SERVER_CERT_PROBLEM
```

**功能：** 服务器证书错误。

**起始版本：** 19

### SERVER_CONTENT_LENGTH_MISMATCH

```cangjie
SERVER_CONTENT_LENGTH_MISMATCH
```

**功能：** 接收到的数据与内容长度不匹配。

**起始版本：** 19

### SERVER_CROSS_ORIGIN_REDIRECT

```cangjie
SERVER_CROSS_ORIGIN_REDIRECT
```

**功能：** 发生意外的跨站重定向。

**起始版本：** 19

### SERVER_FAILED

```cangjie
SERVER_FAILED
```

**功能：** 服务器返回了一个一般性错误。

**起始版本：** 19

### SERVER_FORBIDDEN

```cangjie
SERVER_FORBIDDEN
```

**功能：** 服务器访问被禁止。

**起始版本：** 19

### SERVER_NO_RANGE

```cangjie
SERVER_NO_RANGE
```

**功能：** 服务器不支持范围请求。

**起始版本：** 19

### SERVER_UNAUTHORIZED

```cangjie
SERVER_UNAUTHORIZED
```

**功能：** 服务器不允许下载该文件。

**起始版本：** 19

### SERVER_UNREACHABLE

```cangjie
SERVER_UNREACHABLE
```

**功能：** 无法访问服务器。

**起始版本：** 19