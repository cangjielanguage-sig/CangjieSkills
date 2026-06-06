### class AdsBlockedDetails

```cangjie
public class AdsBlockedDetails {
    public AdsBlockedDetails(
        public let adsBlocked: Array<String>
    )
}
```

**功能：** 描述发生广告拦截时，广告资源信息的参数结构。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

#### let adsBlocked

```cangjie
public let adsBlocked: Array<String>
```

**功能：** 被过滤的资源的url或dompath标识，被过滤的多个对象url相同则可能出现重复元素。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

#### let url

```cangjie
public let url: String
```

**功能：** 发生广告过滤的页面url。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

#### AdsBlockedDetails(String, Array\<String>)

```cangjie
public AdsBlockedDetails(
    public let url: String,
    public let adsBlocked: Array<String>
)
```

**功能：** 发生广告拦截时，广告资源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|发生广告过滤的页面url。|
|adsBlocked|Array\<String>|是|-|被过滤的资源的url或dompath标识，被过滤的多个对象url相同则可能出现重复元素。|