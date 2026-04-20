### func darkMode(?WebDarkMode)

```cangjie
public func darkMode(mode: ?WebDarkMode): This
```

**功能：** 设置Web深色模式，默认关闭。当深色模式开启时，Web将启用媒体查询prefers-color-scheme中网页所定义的深色样式，若网页未定义深色样式，则保持原状。如需开启强制深色模式，建议配合[forceDarkAccess](#func-forcedarkaccessbool)使用。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|?[WebDarkMode](./cj-common-types.md#enum-webdarkmode)|是|-|Web的深色模式为关闭、开启或跟随系统。<br>初始值：WebDarkMode.Off。|

### func domStorageAccess(?Bool)

```cangjie
public func domStorageAccess(domStorageAccess: ?Bool): This
```

**功能：** 设置是否开启文档对象模型存储接口（DOM Storage API）权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domStorageAccess|?Bool|是|-|是否开启文档对象模型存储接口（DOM Storage API）权限。true表示开启，false表示未开启。<br> 初始值：false。|

### func fileAccess(?Bool)

```cangjie
public func fileAccess(fileAccess: ?Bool): This
```

**功能：** 设置是否开启应用中文件系统的访问，默认启用。rawfile路径的文件不受该属性影响而限制访问。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fileAccess|?Bool|是|-|是否开启应用中文件系统的访问，默认启用。<br> 初始值：false|

### func forceDarkAccess(?Bool)

```cangjie
public func forceDarkAccess(access: ?Bool): This
```

**功能：** 设置网页是否开启强制深色模式。默认关闭。该属性仅在darkMode开启深色模式时生效。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|access|?Bool|是|-|设置网页是否开启强制深色模式。true：开启，false：关闭。<br>初始值：false。|

### func geolocationAccess(?Bool)

```cangjie
public func geolocationAccess(geolocationAccess: ?Bool): This
```

**功能：** 设置是否开启获取地理位置权限，默认关闭。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|geolocationAccess|?Bool|是|-|设置是否开启获取地理位置权限。<br>初始值：false。|

### func imageAccess(?Bool)

```cangjie
public func imageAccess(imageAccess: ?Bool): This
```

**功能：** 设置是否允许自动加载图片资源，默认允许。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imageAccess|?Bool|是|-|是否允许自动加载图片资源。<br>初始值：false。|