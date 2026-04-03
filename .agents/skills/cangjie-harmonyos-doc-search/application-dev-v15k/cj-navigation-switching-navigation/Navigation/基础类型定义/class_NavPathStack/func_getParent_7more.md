#### func getParent()

```cangjie
public func getParent(): Option<NavPathStack>
```

**功能：** 获取上一层的NavPathStack。<br/>当出现Navigation嵌套Navigation的情况时（可以是直接嵌套，也可以是间接嵌套），内部Navigation的NavPathStack能够获取到外层Navigation的NavPathStack。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|?[NavPathStack](#class-navpathstack)|如果当前NavPathStack所属Navigation的外层有另外的一层Navigation，则能够获取到外层Navigation的NavPathStack。否则获取不到NavPathStack，返回None。|

#### func moveIndexToTop(Int32, Bool)

```cangjie
public func moveIndexToTop(index: Int32, animated!: Bool = true): Unit
```

**功能：** 将index指定的NavDestination页面移到栈顶。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|NavDestination页面的位置索引。|
|animated|Bool|否|true|是否支持转场动画。|

#### func moveToTop(String, Bool)

```cangjie
public func moveToTop(name: String, animated!: Bool = true): Int32
```

**功能：** 将由栈底开始第一个名为name的NavDestination页面移到栈顶。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。|
|animated|Bool|否|true|是否支持转场动画。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|如果栈中存在名为name的NavDestination页面，则返回由栈底开始第一个名为name的NavDestination页面的当前索引，否则返回-1。|

#### func pop()

```cangjie
public func pop(): Option<NavPathInfo>
```

**功能：** 弹出路由栈栈顶元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[NavPathInfo](#class-navpathinfo)|返回栈顶NavDestination页面的信息。|

#### func pop(Bool)

```cangjie
public func pop(animated!: Bool): Option<NavPathInfo>
```

**功能：** 弹出路由栈栈顶元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|animated|Bool|是|-|是否支持转场动画。|

**返回值：**

|类型|说明|
|:----|:----|
|[NavPathInfo](#class-navpathinfo)|返回栈顶NavDestination页面的信息。|

#### func pop(String, Bool)

```cangjie
public func pop(result: String, animated!: Bool = true): Option<NavPathInfo>
```

**功能：** 弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|result|String|是|-|页面自定义处理结果。|
|animated|Bool|否|true|是否支持转场动画。|

**返回值：**

|类型|说明|
|:----|:----|
|?[NavPathInfo](#class-navpathinfo)|返回栈顶NavDestination页面的信息。|

#### func popToIndex(Int32, Bool)

```cangjie
public func popToIndex(index: Int32, animated!: Bool = true): Unit
```

**功能：** 回退路由栈到index指定的NavDestination页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|NavDestination页面的位置索引。|
|animated|Bool|否|true|是否支持转场动画。|