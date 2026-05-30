### func databaseAccess(Bool)

```cangjie
public func databaseAccess(databaseAccess: Bool): This
```

**功能：** 设置是否开启数据库存储API权限，默认不开启。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|databaseAccess|Bool|是|-|是否开启数据库存储API权限。true表示设置开启数据库存储API权限，false表示设置不开启数据库存储API权限。<br> 初始值：false。|

### func defaultFixedFontSize(Int32)

```cangjie
public func defaultFixedFontSize(size: Int32): This
```

**功能：** 设置网页的默认等宽字体大小。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int32|是|-|设置网页的默认等宽字体大小，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72的值按照72进行渲染，低于1的值按照1进行渲染。<br> 初始值：13。|

### func defaultFontSize(Int32)

```cangjie
public func defaultFontSize(size: Int32): This
```

**功能：** 设置网页的默认字体大小。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|Int32|是|-|网页的默认字体大小，单位px。输入值的范围为-2^31到2^31-1，实际渲染时超过72的值按照72进行渲染，低于1的值按照1进行渲染。<br> 初始值：16。|

### func defaultTextEncodingFormat(String)

```cangjie
public func defaultTextEncodingFormat(textEncodingFormat: String): This
```

**功能：** 设置网页的默认字符编码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|textEncodingFormat|String|是|-|默认字符编码。<br> 初始值："UTF-8"。|

### func domStorageAccess(Bool)

```cangjie
public func domStorageAccess(domStorageAccess: Bool): This
```

**功能：** 设置是否开启文档对象模型存储接口（DOM Storage API）权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domStorageAccess|Bool|是|-|是否开启文档对象模型存储接口（DOM Storage API）权限。true表示开启，false表示未开启。<br> 初始值：false。|