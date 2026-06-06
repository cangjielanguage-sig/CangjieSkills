## class WebStorageOrigin

```cangjie
public class WebStorageOrigin {
    public WebStorageOrigin(
        public var origin: String,
        public var quota: Int64,
        public var usage: Int64
    )
}
```

**功能：** 提供Web SQL数据库的使用信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### var origin

```cangjie
public var origin: String
```

**功能：** 指定源的字符串索引。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var quota

```cangjie
public var quota: Int64
```

**功能：** 指定源的存储配额。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var usage

```cangjie
public var usage: Int64
```

**功能：** 指定源的存储量。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### WebStorageOrigin(String, Int64, Int64)

```cangjie
public WebStorageOrigin(
    public var origin: String,
    public var quota: Int64,
    public var usage: Int64
)
```

**功能：** WebStorageOrigin的主构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|origin|String|是|-|指定源的字符串索引。|
|quota|Int64|是|-|指定源的存储配额。|
|usage|Int64|是|-|指定源的存储量。|