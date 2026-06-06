## class MediaSourceInfo

```cangjie
public class MediaSourceInfo {
    public MediaSourceInfo(
        let format: String,
        let source: String,
        let `type`: SourceType
    )
}
```

**功能：** 表示媒体源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### MediaSourceInfo(String, String, SourceType)

```cangjie
public MediaSourceInfo(
    let format: String,
    let source: String,
    let `type`: SourceType
)
```

**功能：** 构造MediaSourceInfo对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|format|String|是|-|媒体源格式，可能为空，需要使用者自己去判断格式。|
|source|String|是|-|媒体源地址。|
|\`type`|[SourceType](#enum-sourcetype)|是|-|媒体源的类型。|