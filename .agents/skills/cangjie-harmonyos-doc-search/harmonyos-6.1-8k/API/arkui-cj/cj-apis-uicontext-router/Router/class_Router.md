## class Router

```cangjie
public class Router {}
```

**功能：** 路由类，提供跳转到应用内的指定页面、返回上一页面或指定的页面等功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### func pushUrl(String,String)

```cangjie
public func pushUrl(url!: String, params!: String = ""): Unit
```

**功能：** 跳转到应用内的指定页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|**命名参数。** 表示目标页面的url。|
|params|String|否|""|**命名参数。** 表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用getParams()获取传递的参数。|

### func back(?String,String)

```cangjie
public func back(url!: ?String = None, params!: String = ""): Unit
```

**功能：** 返回上一页面或指定的页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|?String|否|None|**命名参数。** 表示目标页面的url。|
|params|String|否|""|**命名参数。** 页面返回时携带的参数。|

### func back(Int32,String)

```cangjie
public func back(index!: Int32, params!: String = ""): Unit
```

**功能：** 返回指定的页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-| **命名参数。** 跳转目标页面的索引值。取值范围：[0, +∞)|
|params|String|否|""| **命名参数。** 页面返回时携带的参数。|

### func getParams()

```cangjie
public func getParams(): Option<String>
```

**功能：** 获取发起跳转的页面往当前页传入的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Option\<String>|发起跳转的页面往当前页传入的参数。|