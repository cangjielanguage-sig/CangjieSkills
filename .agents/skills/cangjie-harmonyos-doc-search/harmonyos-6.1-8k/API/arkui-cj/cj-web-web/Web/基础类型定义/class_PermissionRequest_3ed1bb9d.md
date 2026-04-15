### class PermissionRequest

```cangjie
public class PermissionRequest {}
```

**功能：** Web组件返回授权或拒绝权限功能的对象。示例代码参考[onPermissionRequest](#class-onpermissionrequestevent)事件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### func deny()

```cangjie
public func deny(): Unit
```

**功能：** 拒绝网页所请求的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

#### func getAccessibleResource()

```cangjie
public func getAccessibleResource(): Array<String>
```

**功能：** 获取网页所请求的权限资源列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|网页所请求的权限资源列表。|

#### func getOrigin()

```cangjie
public func getOrigin(): String
```

**功能：** 获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|当前请求权限网页的来源。|

#### func grant(Array\<String>)

```cangjie
public func grant(resources: Array<String>): Unit
```

**功能：** 对网页访问的屏幕捕获操作进行授权。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resources|Array\<String>|是|-|屏幕捕获配置。|