## class CacheOptions

```cangjie
public class CacheOptions {
    public CacheOptions(
        public var responseHeaders: Array<WebHeader>
    )
}
```

**功能：** Web组件预编译JavaScript生成字节码缓存的配置对象，用于控制字节码缓存更新。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var responseHeaders

```cangjie
public var responseHeaders: Array<WebHeader>
```

**功能：** 请求此JavaScript文件时服务器返回的响应头，使用E-Tag或Last-Modified标识文件版本，判断是否需要更新。

**类型：** Array\<[WebHeader](#class-webheader)>

**读写能力：** 可读写

**起始版本：** 19

### CacheOptions(Array\<WebHeader>)

```cangjie
public CacheOptions(
    public var responseHeaders: Array<WebHeader>
)
```

**功能：** CacheOptions的主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|responseHeaders|Array\<[WebHeader](#class-webheader)>|是|-|请求此JavaScript文件时服务器返回的响应头，使用E-Tag或Last-Modified标识文件版本，判断是否需要更新。|

## class Error

```cangjie
public class Error {
    public Error(
        public let errorName: String,
        public let errorMsg: String
    )
}
```

**功能：** [WebMessageExt](#class-webmessageext)设置或返回的错误对象类型的数据。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### let errorMsg

```cangjie
public let errorMsg: String
```

**功能：** 错误信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let errorName

```cangjie
public let errorName: String
```

**功能：** 错误名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### Error(String, String)

```cangjie
public Error(
    public let errorName: String,
    public let errorMsg: String
)
```

**功能：** Error的主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|errorName|String|是|-|错误名。|
|errorMsg|String|是|-|错误信息。|

## class HistoryItem

```cangjie
public class HistoryItem {
    public HistoryItem(
        public let icon: ?PixelMap,
        public let historyUrl: String,
        public let historyRawUrl: String,
        public let title: String
    )
}
```

**功能：** 页面历史记录项。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

### let historyRawUrl

```cangjie
public let historyRawUrl: String
```

**功能：** 历史记录项的原始URL地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let historyUrl

```cangjie
public let historyUrl: String
```

**功能：** 历史记录项的URL地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let icon

```cangjie
public let icon: ?PixelMap
```

**功能：** 历史页面图标的PixelMap对象。

**类型：** ?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 只读

**起始版本：** 12

### let title

```cangjie
public let title: String
```

**功能：** 历史记录项的标题。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### HistoryItem(?PixelMap, String, String, String)

```cangjie
public HistoryItem(
    public let icon: ?PixelMap,
    public let historyUrl: String,
    public let historyRawUrl: String,
    public let title: String
)
```

**功能：** 构造HistoryItem对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|icon|?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|历史页面图标的PixelMap对象。|
|historyUrl|String|是|-|历史记录项的URL地址。|
|historyRawUrl|String|是|-|历史记录项的原始URL地址。|
|title|String|是|-|历史记录项的标题。|