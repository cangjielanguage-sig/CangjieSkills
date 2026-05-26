### func webFantasyFont(String)

```cangjie
public func webFantasyFont(family: String): This
```

**功能：** 设置网页的fantasy font字体库。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|family|String|是|-|网页的fantasy font字体库。<br> 初始值：fantasy。|

### func webFixedFont(String)

```cangjie
public func webFixedFont(family: String): This
```

**功能：** 设置网页的fixed font字体库。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|family|String|是|-|网页的fixed font字体库。<br> 初始值：monospace。|

### func webSansSerifFont(String)

```cangjie
public func webSansSerifFont(family: String): This
```

**功能：** 设置网页的sans serif font字体库。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|family|String|是|-|网页的sans serif font字体库。<br> 初始值：sans-serif。|

### func webSerifFont(String)

```cangjie
public func webSerifFont(family: String): This
```

**功能：** 设置网页的serif font字体库。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|family|String|是|-|网页的serif font字体库。<br> 初始值：serif。|

### func webStandardFont(String)

```cangjie
public func webStandardFont(family: String): This
```

**功能：** 设置网页的standard font字体库。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|family|String|是|-|网页的standard font字体库。<br> 初始值：sans serif。|

### func zoomAccess(Bool)

```cangjie
public func zoomAccess(zoomAccess: Bool): This
```

**功能：** 设置是否支持手势进行缩放，默认允许执行缩放。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|zoomAccess|Bool|是|-|是否支持手势进行缩放。true表示设置支持手势进行缩放，false表示设置不支持手势进行缩放。<br> 初始值：true。|