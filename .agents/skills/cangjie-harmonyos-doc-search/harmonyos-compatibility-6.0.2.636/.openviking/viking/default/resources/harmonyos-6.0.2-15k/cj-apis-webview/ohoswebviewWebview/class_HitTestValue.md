## class HitTestValue

```cangjie
public class HitTestValue {}
```

**功能：** 提供点击区域的元素信息。示例代码参考[getHitTestValue](#func-gethittestvalue)。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

### let extra

```cangjie
public let extra: String
```

**功能：** 点击区域的附加参数信息。若被点击区域为图片或链接，则附加参数信息为其URL地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let hitTestType

```cangjie
public let hitTestType: WebHitTestType
```

**功能：** 当前被点击区域的元素类型。

**类型：** [WebHitTestType](#enum-webhittesttype)

**读写能力：** 只读

**起始版本：** 12