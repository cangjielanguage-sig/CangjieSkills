### func javaScriptProxy(?Array\<(String) -> String>, ?String, ?Array\<String>, ?WebviewController)

```cangjie
public func javaScriptProxy(funcList!: ?Array<(String) -> String>, name!: ?String, methodList!: ?Array<String>,
    controller!: ?WebviewController): This
```

**功能：** 注入JavaScript对象到window对象中，并在window对象中调用该对象的方法。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|funcList|?Array\<(String)->String>|是|-| **命名参数。** 参与注册的应用侧JavaScript对象的同步方法。<br>初始值：[]。|
|name|?String|是|-| **命名参数。** 注册对象的名称，与window中调用的对象名一致。<br>初始值：""。|
|methodList|?Array\<String>|是|-| **命名参数。** 参与注册的应用侧JavaScript对象的异步方法。<br>初始值：[]。|
|controller|?[WebviewController](../ArkWeb/cj-apis-webview.md#class-webviewcontroller)|是|-| **命名参数。** 设置Web控制器。<br>初始值：WebviewController()。|

### func mixedMode(?MixedMode)

```cangjie
public func mixedMode(mixedMode: ?MixedMode): This
```

**功能：** 设置是否允许加载超文本传输协议（HTTP）和超文本传输安全协议（HTTPS）混合内容，默认不允许加载HTTP和HTTPS混合内容。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mixedMode|?[MixedMode](./cj-common-types.md#enum-mixedmode)|是|-|混合内容。<br>初始值：MixedMode.None。表示不允许安全来源（secure origin）加载不安全来源（insecure origin）的内容。|

### func nestedScroll(?NestedScrollMode, ?NestedScrollMode)

```cangjie
public func nestedScroll(
    scrollForward!: ?NestedScrollMode,
    scrollBackward!: ?NestedScrollMode
): This
```

**功能：** 设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scrollForward|?[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|是|-| **命名参数。** 向前滚动模式。<br>初始值：NestedScrollMode.SelfFirst。|
|scrollBackward|?[NestedScrollMode](./cj-common-types.md#enum-nestedscrollmode)|是|-| **命名参数。** 向后滚动模式。<br>初始值：NestedScrollMode.SelfFirst。|

### func onlineImageAccess(?Bool)

```cangjie
public func onlineImageAccess(onlineImageAccess: ?Bool): This
```

**功能：** 设置是否允许从网络加载图片资源（通过HTTP和HTTPS访问的资源），默认不允许访问。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onlineImageAccess|?Bool|是|-|是否允许从网络加载图片资源。true表示设置允许从网络加载图片资源，false表示设置不允许从网络加载图片资源。<br>初始值：false。|

### func verticalScrollBarAccess(?Bool)

```cangjie
public func verticalScrollBarAccess(verticalScrollBar: ?Bool): This
```

**功能：** 设置是否显示纵向滚动条，包括系统默认滚动条和用户自定义滚动条。默认不显示。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|verticalScrollBar|?Bool|是|-|是否显示纵向滚动条。true表示设置显示纵向滚动条，false表示设置不显示纵向滚动条。<br>初始值：false。|