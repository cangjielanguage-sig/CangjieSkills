#### func pushDestinationByName(String, String, (PopInfo) -> Unit, Bool)

```cangjie
public func pushDestinationByName(name: String, param: String, onPop: (PopInfo) -> Unit, animated!: Bool = true): Unit
```

**功能：** 将name指定的NavDestination页面信息入栈，传递的数据为param，并且添加用于页面出栈时处理返回结果的OnPop回调，使用Promise异步回调返回接口调用结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| NavDestination页面名称。|
|param|String|是|-|NavDestination页面详细参数。|
|onPop|([PopInfo](#class-popinfo))->Unit|是|-|Callback回调，用于页面出栈时处理返回结果。仅pop中设置result参数后触发。|
|animated|Bool|否|true|是否支持转场动画，默认值：true。|

#### func pushPath(NavPathInfo)

```cangjie
public func pushPath(info: NavPathInfo): Unit
```

**功能：** 将info指定的NavDestination页面信息入栈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-| NavDestination页面的信息。|

#### func pushPath(NavPathInfo, Bool)

```cangjie
public func pushPath(info: NavPathInfo, animated!: Bool): Unit
```

**功能：** 将info指定的NavDestination页面信息入栈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-| NavDestination页面的信息。|
|animated|Bool|是|-|是否支持转场动画。|

#### func pushPath(NavPathInfo, NavigationOptions)

```cangjie
public func pushPath(info: NavPathInfo, options!: NavigationOptions): Unit
```

**功能：** 将info指定的NavDestination页面信息入栈，具体根据options中指定不同的[LaunchMode](#enum-launchmode)，有不同的行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-| NavDestination页面的信息。|
|options|[NavigationOptions](#class-navigationoptions)|是|-| 页面栈操作选项。|

#### func pushPathByName(String, String, Bool)

```cangjie
public func pushPathByName(name: String, param: String, animated!: Bool = true): Unit
```

**功能：** 将name指定的NavDestination页面信息入栈，传递的数据为param。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。|
|param|String|是|-| NavDestination页面详细参数。|
|animated|Bool|否|true|是否支持转场动画。|

#### func pushPathByName(String, String, (PopInfo) -> Unit, Bool)

```cangjie
public func pushPathByName(name: String, param: String, onPop: (PopInfo) -> Unit, animated!: Bool = true): Unit
```

**功能：** 将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。 |
|param|String|是|-|NavDestination页面详细参数。|
|onPop|([PopInfo](#class-popinfo))->Unit|是|-|Callback回调，用于页面出栈时触发该回调处理返回结果。仅pop中设置result参数后触发。|
|animated|Bool|否|true|是否支持转场动画。|