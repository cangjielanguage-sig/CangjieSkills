### func geolocationAccess(Bool)

```cangjie
public func geolocationAccess(geolocationAccess: Bool): This
```

**功能：** 设置是否开启获取地理位置权限，默认开启。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|geolocationAccess|Bool|是|-|设置是否开启获取地理位置权限。|

### func horizontalScrollBarAccess(Bool)

```cangjie
public func horizontalScrollBarAccess(horizontalScrollBar: Bool): This
```

**功能：** 设置是否显示横向滚动条，包括系统默认滚动条和用户自定义滚动条。默认显示。

> **说明：**
>
> - 通过@State变量控制横向滚动条的隐藏/显示后，需要调用controller.refresh()生效。
> - 通过@State变量频繁动态改变时，建议切换开关变量和Web组件一一对应。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|horizontalScrollBar|Bool|是|-|是否显示横向滚动条。true表示设置显示横向滚动条，false表示设置不显示横向滚动条。<br> 初始值：true。|

### func imageAccess(Bool)

```cangjie
public func imageAccess(imageAccess: Bool): This
```

**功能：** 设置是否允许自动加载图片资源，默认允许。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageAccess|Bool|是|-|是否允许自动加载图片资源。|

### func initialScale(Float32)

```cangjie
public func initialScale(percent: Float32): This
```

**功能：** 设置整体页面的缩放百分比，默认为100。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19
**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|percent|Float32|是|-|整体页面的缩放百分比。<br> 初始值：100.0。取值范围：(0, 1000]。|

### func javaScriptAccess(Bool)

```cangjie
public func javaScriptAccess(javaScriptAccess: Bool): This
```

**功能：** 设置是否允许执行JavaScript脚本，默认允许执行。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|javaScriptAccess|Bool|是|-|是否允许执行JavaScript脚本。true表示允许执行JavaScript脚本，false表示不允许执行JavaScript脚本。<br> 初始值：true。|

### func javaScriptOnDocumentEnd(Array\<ScriptItem>)

```cangjie
public func javaScriptOnDocumentEnd(scripts: Array<ScriptItem>): This
```

**功能：** 将JavaScript脚本注入到Web组件中，当指定页面或者文档加载完成时，该脚本将在其来源与scriptRules匹配的任何页面中执行。

> **说明：**
>
> - 该脚本将在页面的任何JavaScript代码之后运行，并且DOM树此时已经加载、渲染完毕。
> - 该脚本按照字典序执行，非数组本身顺序。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scripts|Array\<[ScriptItem](#class-scriptitem)>|是|-|需要注入的ScriptItem数组。|