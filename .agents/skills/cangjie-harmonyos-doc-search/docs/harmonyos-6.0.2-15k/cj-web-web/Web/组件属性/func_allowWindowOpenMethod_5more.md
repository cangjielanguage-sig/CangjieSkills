### func allowWindowOpenMethod(Bool)

```cangjie
public func allowWindowOpenMethod(flag: Bool): This
```

**功能：** 设置网页是否可以通过JavaScript自动打开新窗口。

该属性为true时，可通过JavaScript自动打开新窗口。该属性为false时，用户行为仍可通过JavaScript自动打开新窗口，但非用户行为不能通过JavaScript自动打开新窗口。此处的用户行为是指，在用户对Web组件进行点击等操作后，同时在5秒内请求打开新窗口（window.open）的行为。

该属性仅在[javaScriptAccess](#func-javascriptaccessbool)开启时生效。

该属性在[multiWindowAccess](#func-multiwindowaccessbool)开启时打开新窗口，关闭时打开本地窗口。

该属性的初始值与系统属性persist.web.allowWindowOpenMethod.enabled 保持一致，如果未设置系统属性则初始值为false。

检查系统配置项persist.web.allowWindowOpenMethod.enabled 是否开启。

通过hdc shell param get persist.web.allowWindowOpenMethod.enabled 查看，若配置项为0或不存在，可通过命令hdc shell param set persist.web.allowWindowOpenMethod.enabled 1 开启配置。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|flag|Bool|是|-|网页是否可以通过JavaScript自动打开窗口。true表示网页可以通过JavaScript自动打开窗口，false表示网页不可以通过JavaScript自动打开窗口。初始值与系统参数关联，当系统参数persist.web.allowWindowOpenMethod.enabled为true时，初始值为true，否则为false。|

### func blockNetwork(Bool)

```cangjie
public func blockNetwork(block: Bool): This
```

**功能：** 设置Web组件是否阻止从网络加载资源。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|block|Bool|是|-|Web组件是否阻止从网络加载资源。true表示设置Web组件阻止从网络加载资源，false表示设置Web组件不阻止从网络加载资源。<br> 初始值：false。|

### func cacheMode(CacheMode)

```cangjie
public func cacheMode(cacheMode: CacheMode): This
```

**功能：** 设置缓存模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cacheMode|[CacheMode](#enum-cachemode)|是|-|缓存模式。<br> 初始值：CacheMode.Default。|

### func copyOptions(CopyOptions)

```cangjie
public func copyOptions(value: CopyOptions): This
```

**功能：** 设置剪贴板复制范围选项。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CopyOptions](../arkui-cj/cj-common-types.md#enum-copyoptions)|是|-|剪贴板复制范围选项。<br> 初始值：CopyOptions.LocalDevice。|

### func darkMode(WebDarkMode)

```cangjie
public func darkMode(mode: WebDarkMode): This
```

**功能：** 设置Web深色模式，默认关闭。当深色模式开启时，Web将启用媒体查询prefers-color-scheme中网页所定义的深色样式，若网页未定义深色样式，则保持原状。如需开启强制深色模式，建议配合[forceDarkAccess](#func-forcedarkaccessbool)使用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[WebDarkMode](./cj-common-types.md#enum-webdarkmode)|是|-|Web的深色模式为关闭、开启或跟随系统。<br> 初始值：WebDarkMode.Off。|