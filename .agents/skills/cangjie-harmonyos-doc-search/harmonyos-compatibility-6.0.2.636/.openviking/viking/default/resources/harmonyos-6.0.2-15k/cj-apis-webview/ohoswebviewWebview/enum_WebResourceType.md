## enum WebResourceType

```cangjie
public enum WebResourceType <: Equatable<WebResourceType> & ToString {
    | MAIN_FRAME
    | SUB_FRAME
    | STYLE_SHEET
    | SCRIPT
    | IMAGE
    | FONT_RESOURCE
    | SUB_RESOURCE
    | OBJECT
    | MEDIA
    | WORKER
    | SHARED_WORKER
    | PREFETCH
    | FAVICON
    | XHR
    | PING
    | SERVICE_WORKER
    | CSP_REPORT
    | PLUGIN_RESOURCE
    | NAVIGATION_PRELOAD_MAIN_FRAME
    | NAVIGATION_PRELOAD_SUB_FRAME
    | ...
}
```

**功能：** 资源请求的资源类型。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**父类型：**

- Equatable\<WebResourceType>
- ToString

### CSP_REPORT

```cangjie
CSP_REPORT
```

**功能：** 内容安全策略违规报告。

**起始版本：** 19

### FAVICON

```cangjie
FAVICON
```

**功能：** 网站图标。

**起始版本：** 19

### FONT_RESOURCE

```cangjie
FONT_RESOURCE
```

**功能：** 字体。

**起始版本：** 19

### IMAGE

```cangjie
IMAGE
```

**功能：** 图片（jpg/gif/png/以及其他）。

**起始版本：** 19

### MAIN_FRAME

```cangjie
MAIN_FRAME
```

**功能：** 顶层页面。

**起始版本：** 19

### MEDIA

```cangjie
MEDIA
```

**功能：** 媒体资源。

**起始版本：** 19

### NAVIGATION_PRELOAD_MAIN_FRAME

```cangjie
NAVIGATION_PRELOAD_MAIN_FRAME
```

**功能：** 触发service worker预热的主frame跳转请求。

**起始版本：** 19

### NAVIGATION_PRELOAD_SUB_FRAME

```cangjie
NAVIGATION_PRELOAD_SUB_FRAME
```

**功能：** 触发service worker预热的子frame跳转请求。

**起始版本：** 19

### OBJECT

```cangjie
OBJECT
```

**功能：** 插件的Object（或embed）标签，或者插件请求的资源。

**起始版本：** 19

### PING

```cangjie
PING
```

**功能：** \<a ping>/sendBeacon的Ping请求。

**起始版本：** 19

### PLUGIN_RESOURCE

```cangjie
PLUGIN_RESOURCE
```

**功能：** 插件请求的资源。

**起始版本：** 19

### PREFETCH

```cangjie
PREFETCH
```

**功能：** 明确的预取请求。

**起始版本：** 19

### SCRIPT

```cangjie
SCRIPT
```

**功能：** 外部脚本。

**起始版本：** 19

### SERVICE_WORKER

```cangjie
SERVICE_WORKER
```

**功能：** service worker的主资源。

**起始版本：** 19

### SHARED_WORKER

```cangjie
SHARED_WORKER
```

**功能：** 共享工作线程的主资源。

**起始版本：** 19

### STYLE_SHEET

```cangjie
STYLE_SHEET
```

**功能：** CSS样式表。

**起始版本：** 19

### SUB_FRAME

```cangjie
SUB_FRAME
```

**功能：** Frame或Iframe。

**起始版本：** 19

### SUB_RESOURCE

```cangjie
SUB_RESOURCE
```

**功能：** 其他子资源。如果实际类型未知，则是默认类型。

**起始版本：** 19

### WORKER

```cangjie
WORKER
```

**功能：** 专用工作线程的主资源。

**起始版本：** 19

### XHR

```cangjie
XHR
```

**功能：** XMLHttpRequest。

**起始版本：** 19

### func !=(WebResourceType)

```cangjie
public operator func !=(other: WebResourceType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebResourceType](#enum-webresourcetype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(WebResourceType)

```cangjie
public operator func ==(other: WebResourceType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WebResourceType](#enum-webresourcetype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|