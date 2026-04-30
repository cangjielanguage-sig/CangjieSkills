### func registerNativeEmbedRule(String, String)

```cangjie
public func registerNativeEmbedRule(tag: String, `type`: String): This
```

**功能：** 注册使用同层渲染的HTML标签名和类型。标签名仅支持使用object和embed。标签类型只能使用ASCII可显示字符。

若指定类型与w3c定义的object或embed标准类型重合，ArkWeb内核将其识别为非同层标签。

本接口同样受enableNativeEmbedMode接口控制，在未使能同层渲染时本接口无效。在不使用本接口的情况下，ArkWeb内核默认将"native/"前缀类型的embed标签识别为同层标签。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tag|String|是|-|标签名。|
|\`type\`|String|是|-|标签类型,内核使用前缀匹配此参数。|

### func selectionMenuOptions(Array\<ExpandedMenuItemOptions>)

```cangjie
public func selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>): This
```

**功能：** Web组件自定义菜单扩展项接口，允许用户设置扩展项的文本内容、图标、回调方法。

该接口只支持选中纯文本，当选中内容包含图片及其他非文本内容时，action信息中会显示乱码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|expandedMenuOptions|Array\<[ExpandedMenuItemOptions](#class-expandedmenuitemoptions)>|是|-|扩展菜单选项。<br>菜单项数量，及菜单的content大小、startIcon图标尺寸，与ArkUI Menu组件保持一致。|

### func textAutosizing(Bool)

```cangjie
public func textAutosizing(textAutosizing: Bool): This
```

**功能：** 设置使能文本自动调整大小。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textAutosizing|Bool|是|-|文本自动调整大小。true表示文本自动调整大小，false表示文本不自动调整大小。<br> 初始值：true。|

### func textZoomRatio(Int32)

```cangjie
public func textZoomRatio(textZoomRatio: Int32): This
```

**功能：** 设置页面的文本缩放百分比，默认为100。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textZoomRatio|Int32|是|-|页面的文本缩放百分比。取值为整数，范围为(0, 2147483647]。<br> 初始值：100。|

### func verticalScrollBarAccess(Bool)

```cangjie
public func verticalScrollBarAccess(verticalScrollBar: Bool): This
```

**功能：** 设置是否显示纵向滚动条，包括系统默认滚动条和用户自定义滚动条。默认显示。

> **说明:**
>
> - 通过@State变量控制纵向滚动条的隐藏/显示后，需要调用controller.refresh()生效。
> - 通过@State变量频繁动态改变时，建议切换开关变量和Web组件一一对应。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|verticalScrollBar|Bool|是|-|是否显示纵向滚动条。true表示设置显示纵向滚动条，false表示设置不显示纵向滚动条。<br> 初始值：true。|

### func webCursiveFont(String)

```cangjie
public func webCursiveFont(family: String): This
```

**功能：** 设置网页的cursive font字体库。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|family|String|是|-|网页的cursive font字体库。<br> 初始值：cursive。|