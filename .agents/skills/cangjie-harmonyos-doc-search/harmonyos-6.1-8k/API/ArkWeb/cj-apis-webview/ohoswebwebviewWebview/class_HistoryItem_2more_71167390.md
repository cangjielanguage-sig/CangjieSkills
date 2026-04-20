## class HistoryItem

```cangjie
public class HistoryItem {
    public var icon: ?PixelMap
    public var historyUrl: String
    public var historyRawUrl: String
    public var title: String
}
```

**功能：** 页面历史记录项。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### var historyRawUrl

```cangjie
public var historyRawUrl: String
```

**功能：** 历史记录项的原始URL地址。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### var historyUrl

```cangjie
public var historyUrl: String
```

**功能：** 历史记录项的URL地址。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### var title

```cangjie
public var title: String
```

**功能：** 历史记录项的标题。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### var icon

```cangjie
public var icon: ?PixelMap
```

**功能：** 历史页面图标的PixelMap对象。

**类型：** ?[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

## class HitTestValue

```cangjie
public class HitTestValue {
    public var hitTestType: WebHitTestType
    public var extra: String
}
```

**功能：** 提供点击区域的元素信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### var extra

```cangjie
public var extra: String
```

**功能：** 点击区域的附加参数信息。若被点击区域为图片或链接，则附加参数信息为其url地址。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### var hitTestType

```cangjie
public var hitTestType: WebHitTestType
```

**功能：** 当前被点击区域的元素类型。

**类型：** [WebHitTestType](#enum-webhittesttype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22