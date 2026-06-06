### class OnDownloadStartEvent

```cangjie
public class OnDownloadStartEvent {
    public OnDownloadStartEvent(
        public let url: String,
        public let userAgent: String,
        public let contentDisposition: String,
        public let mimetype: String,
        public let contentLength: Int64
    )
}
```

**功能：** 定义通知主应用开始下载一个文件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let contentDisposition

```cangjie
public let contentDisposition: String
```

**功能：** 服务器返回的 Content-Disposition响应头，可能为空。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### let contentLength

```cangjie
public let contentLength: Int64
```

**功能：** 服务器返回文件的长度。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

#### let mimetype

```cangjie
public let mimetype: String
```

**功能：** 服务器返回内容媒体类型（MIME）信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### let url

```cangjie
public let url: String
```

**功能：** 文件下载的URL。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### let userAgent

```cangjie
public let userAgent: String
```

**功能：** 用于下载的用户代理。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### OnDownloadStartEvent(String, String, String, String, Int64)

```cangjie
public OnDownloadStartEvent(
    public let url: String,
    public let userAgent: String,
    public let contentDisposition: String,
    public let mimetype: String,
    public let contentLength: Int64
)
```

**功能：** 通知主应用开始下载一个文件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|文件下载的URL。|
|userAgent|String|是|-|用于下载的用户代理。|
|contentDisposition|String|是|-|服务器返回的 Content-Disposition响应头，可能为空。|
|mimetype|String|是|-|服务器返回内容媒体类型（MIME）信息。|
|contentLength|Int64|是|-|服务器返回文件的长度。|