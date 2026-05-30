### static func getStateByUrl(String)

```cangjie
public static func getStateByUrl(url: String): ArrayList<RouterState>
```

**功能：** 通过url获取对应页面的状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|表示要获取对应页面信息的url。|

**返回值：**

|类型|说明|
|:----|:----|
|ArrayList\<[RouterState](#class-routerstate)>|页面状态信息。|

### static func hideAlertBeforeBackPage()

```cangjie
public static func hideAlertBeforeBackPage()
```

**功能：** 禁用页面返回询问对话框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func push(String, String)

```cangjie
public static func push(url!: String, params!: String = "")
```

**功能：** 跳转到应用内的指定页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-| **命名参数。** 表示目标页面的url。|
|params|String|否|""| **命名参数。** 表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。<br>**说明：**<br>params参数不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造String类型的Json对象进行传递。|

### static func pushUrl(String, String, ((Option\<Int32>) -> Unit))

```cangjie
public static func pushUrl(url!: String, params!: String = "", callback!: ((Option<Int32>) -> Unit))
```

**功能：** 跳转到应用内的指定页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-| **命名参数。** 表示目标页面的url。|
|params|String|否|""| **命名参数。** 表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。<br>**说明：**<br>params参数不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造String类型的Json对象进行传递。|
|callback|((Option\<Int32>)->Unit)|是|-| **命名参数。** 异常响应回调。|