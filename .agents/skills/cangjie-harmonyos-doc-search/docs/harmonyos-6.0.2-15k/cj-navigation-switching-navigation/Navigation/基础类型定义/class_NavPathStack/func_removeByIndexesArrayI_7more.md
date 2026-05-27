#### func removeByIndexes(Array\<Int32>)

```cangjie
public func removeByIndexes(indexes: Array<Int32>): Int32
```

**功能：** 将页面栈内索引值在indexes中的NavDestination页面删除。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|indexes|Array\<Int32>|是|-|待删除NavDestination页面的索引值数组。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回删除的NavDestination页面数量。|

#### func removeByName(String)

```cangjie
public func removeByName(name: String): Int32
```

**功能：** 将页面栈内指定name的NavDestination页面删除。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| 删除的NavDestination页面的名字。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32| 返回删除的NavDestination页面数量。|

#### func removeByNavDestinationId(String)

```cangjie
public func removeByNavDestinationId(navDestinationId: String): Bool
```

**功能：** 将页面栈内指定navDestinationId的NavDestination页面删除。navDestinationId可以在NavDestination的[onReady](./cj-navigation-switching-navdestination.md#func-onreadynavdestinationcontext---unit)回调中获取，也可以在[NavDestinationInfo]()中获取。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|navDestinationId|String|是|-|删除的NavDestination页面的唯一标识符navDestinationId。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回是否成功删除该页面，true为删除成功。|

#### func replacePath(NavPathInfo, Bool)

```cangjie
public func replacePath(info: NavPathInfo, animated!: Bool = true): Unit
```

**功能：** 将当前页面栈栈顶退出，将info指定的NavDestination页面信息入栈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-|新栈顶页面参数信息。|
|animated|Bool|否|true| 是否支持转场动画。|

#### func replacePath(NavPathInfo, NavigationOptions)

```cangjie
public func replacePath(info: NavPathInfo, options!: NavigationOptions): Unit
```

**功能：** 替换页面栈操作，具体根据options中指定不同的[LaunchMode](#enum-launchmode)，有不同的行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[NavPathInfo](#class-navpathinfo)|是|-|新栈顶页面参数信息。|
|options|[NavigationOptions](#class-navigationoptions)|是|-|页面栈操作选项。|

#### func replacePathByName(String, String, Bool)

```cangjie
public func replacePathByName(name: String, param: String, animated!: Bool = true): Unit
```

**功能：** 将当前页面栈栈顶退出，将name指定的页面入栈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| NavDestination页面名称。|
|param|String|是|-| NavDestination页面详细参数。|
|animated|Bool|否|true|是否支持转场动画。|

#### func size()

```cangjie
public func size(): Int32
```

**功能：** 获取栈大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Int32|返回栈大小。|