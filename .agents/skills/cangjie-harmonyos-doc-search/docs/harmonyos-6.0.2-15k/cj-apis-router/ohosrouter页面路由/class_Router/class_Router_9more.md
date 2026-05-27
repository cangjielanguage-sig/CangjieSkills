## class Router

```cangjie
public class Router {}
```

**功能：** 页面路由。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func back(String, String)

```cangjie
public static func back(url!: String, params!: String = "")
```

**功能：** 返回上一页面或指定的页面，会删除当前页面与指定页面之间的所有页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-| **命名参数。** 表示目标页面的url。|
|params|String|否|""| **命名参数。** 表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。<br>**说明：**<br>params参数不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造String类型的Json对象进行传递。|

### static func back()

```cangjie
public static func back()
```

**功能：** 返回上一页面，会删除当前页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### static func back(Int32, String)

```cangjie
public static func back(index!: Int32,  params!: String = "")
```

**功能：** 返回上一页面或指定的页面，会删除当前页面与指定页面之间的所有页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-| **命名参数。** 跳转目标页面的索引值。从栈底到栈顶，index从1开始递增。|
|params|String|否|""| **命名参数。** 页面返回时携带的参数。|

### static func clear()

```cangjie
public static func clear()
```

**功能：** 清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func getLength()

```cangjie
public static func getLength(): String
```

**功能：** 获取当前在页面栈内的页面数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|页面数量，页面栈支持最大数值是32。|

### static func getParams()

```cangjie
public static func getParams(): Option<String>
```

**功能：** 获取发起跳转的页面往当前页传入的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Option\<String>|发起跳转的页面往当前页传入的参数。|

### static func getState()

```cangjie
public static func getState(): RouterState
```

**功能：** 获取栈顶页面的状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[RouterState](#class-routerstate)|页面状态信息。|

### static func getStateByIndex(Int32)

```cangjie
public static func getStateByIndex(index: Int32): Option<RouterState>
```

**功能：** 通过索引值获取对应页面的状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|表示要获取的页面索引。从栈底到栈顶，index从1开始递增。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<[RouterState](#class-routerstate)>|返回页面状态信息。索引不存在时返回None。|