#### func popToIndex(Int32, String, Bool)

```cangjie
public func popToIndex(index: Int32, result: String, animated!: Bool = true): Unit
```

**功能：** 回退路由栈到index指定的NavDestination页面，并触发onPop回调传入页面处理结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|NavDestination页面的位置索引。|
|result|String|是|-|页面自定义处理结果。|
|animated|Bool|否|true|是否支持转场动画。|

#### func popToName(String, Bool)

```cangjie
public func popToName(name: String, animated!: Bool = true): Int32
```

**功能：** 回退路由栈到由栈底开始第一个名为name的NavDestination页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| NavDestination页面名称。|
|animated|Bool|否|true|是否支持转场动画。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32| 如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。|

#### func popToName(String, String, Bool)

```cangjie
public func popToName(name: String, result: String, animated!: Bool = true): Int32
```

**功能：** 回退路由栈到由栈底开始第一个名为name的NavDestination页面，并触发onPop回调传入页面处理结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。|
|result|String|是|-|页面自定义处理结果。|
|animated|Bool|否|true|是否支持转场动画。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的索引，否则返回-1。|

#### func pushDestination(NavPathInfo, Bool)

```cangjie
public func pushDestination(info: NavPathInfo, animated!: Bool = true) : Unit
```

**功能：** 将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-|NavDestination页面的信息。|
|animated|Bool|否|true|是否支持转场动画。|

#### func pushDestination(NavPathInfo, NavigationOptions)

```cangjie
public func pushDestination(info: NavPathInfo, options!: NavigationOptions) : Unit
```

**功能：** 将info指定的NavDestination页面信息入栈，使用Promise异步回调返回接口调用结果，具体根据options中指定不同的[LaunchMode](#enum-launchmode)，有不同的行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-|NavDestination页面的信息。|
|options|[NavigationOptions](#class-navigationoptions)|是|-| 页面栈操作选项。|

#### func pushDestinationByName(String, String, Bool)

```cangjie
public func pushDestinationByName(name: String, param: String, animated!: Bool = true): Unit
```

**功能：** 将name指定的NavDestination页面信息入栈，传递的数据为param，使用Promise异步回调返回接口调用结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。 |
|param|String|是|-| NavDestination页面详细参数。|
|animated|Bool|否|true| 是否支持转场动画。|