### func metaViewport(Bool)

```cangjie
public func metaViewport(enabled: Bool): This
```

**功能：** 设置meta标签的viewport属性是否可用。

> **说明：**
>
> - 设置false不支持meta标签viewport属性，将不解析viewport属性，进行默认布局。
> - 设置true支持meta标签viewport属性，将解析viewport属性，并根据viewport属性布局。
> - 如果设置为异常值将无效。
> - 如果设备为2in1，不支持viewport属性。设置为true或者false均不会解析viewport属性，进行默认布局。
> - 如果设备为Tablet，设置为true或false均会解析meta标签viewport-fit属性。当viewport-fit=cover时，可通过CSS属性获取安全区域大小。
> - 当前通过User-Agent中是否含有"Mobile"字段来判断是否开启前端HTML页面中meta标签的viewport属性。当User-Agent中不含有"Mobile"字段时，meta标签中viewport属性默认关闭，此时可通过显性设置metaViewport属性为true来覆盖关闭状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enabled|Bool|是|-|是否支持meta标签的viewport属性。true表示支持meta标签的viewport属性，false表示不支持meta标签的viewport属性。<br> 初始值：true。|

### func minFontSize(Int32)

```cangjie
public func minFontSize(size: Int32): This
```

**功能：** 设置网页字体大小最小值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int32|是|-|网页字体大小最小值，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72的值按照72进行渲染，低于1的值按照1进行渲染。<br> 初始值：8。|

### func minLogicalFontSize(Int32)

```cangjie
public func minLogicalFontSize(size: Int32): This
```

**功能：** 设置网页逻辑字体大小最小值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int32|是|-|网页逻辑字体大小最小值，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72的值按照72进行渲染，低于1的值按照1进行渲染。<br> 初始值：8|

### func mixedMode(MixMode)

```cangjie
public func mixedMode(mixedMode: MixMode): This
```

**功能：** 设置是否允许加载超文本传输协议（HTTP）和超文本传输安全协议（HTTPS）混合内容，默认不允许加载HTTP和HTTPS混合内容。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mixedMode|[MixMode](#enum-mixmode)|是|-|混合内容。<br> 初始值：MixedMode.None，表示不允许安全来源（secure origin）加载不安全来源（insecure origin）的内容。|

### func multiWindowAccess(Bool)

```cangjie
public func multiWindowAccess(multiWindow: Bool): This
```

**功能：** 设置是否开启多窗口权限，默认不开启。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|multiWindow|Bool|是|-|是否开启多窗口权限。true表示设置开启多窗口权限，false表示设置不开启多窗口权限。<br> 初始值：false。|