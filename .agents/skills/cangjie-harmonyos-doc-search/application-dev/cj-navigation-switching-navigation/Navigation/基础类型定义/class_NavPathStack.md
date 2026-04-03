### class NavPathStack

```cangjie
public class NavPathStack {
    public init()
}
```

**功能：** 表示NavDestinations的信息。提供控制栈中目标页面的方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init()

```cangjie
public init()
```

**功能：** 创建NavPathStack的实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func pop(?Bool)

```cangjie
public func pop(animated!: ?Bool = None): ?NavPathInfo
```

**功能：** 将顶部NavDestination弹出栈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|animated|?Bool|否|None|**命名参数。** 是否支持过渡动画。初始值：true。|

**返回值：**

|类型|说明|
|:---|:---|
|?[NavPathInfo](#class-navpathinfo)|如果栈不为空则返回顶部NavPathInfo，否则返回None。|

#### func pushPath(?NavPathInfo, ?NavigationOptions)

```cangjie
public func pushPath(info: ?NavPathInfo, options!: ?NavigationOptions = None): Unit
```

**功能：** 将指定的NavDestination推入栈中。根据options参数中指定的launchMode，将触发不同的行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|?[NavPathInfo](#class-navpathinfo)|是|-|要推入的NavDestination。|
|options|?[NavigationOptions](#class-navigationoptions)|否|None|**命名参数。**  导航选项。|

#### func pushPathByName(?String, ?String, ?Bool)

```cangjie
public func pushPathByName(name: ?String, param: ?String, animated!: ?Bool = None)
```

**功能：** 将指定的NavDestination推入栈中。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|?String|是|-|要推入的NavDestination的名称。初始值：""。|
|param|?String|是|-|要推入的NavDestination的详细参数。初始值：""。|
|animated|?Bool|否|None|**命名参数。** 是否支持过渡动画。|