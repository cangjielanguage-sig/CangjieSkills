### class NavPathStack

```cangjie
public class NavPathStack {
    public init()
}
```

**功能：** 表示Navigation路由栈，允许被继承。开发者可以在派生类中新增属性方法，也可以重写基类NavPathStack的方法。派生类对象可以替代基类NavPathStack对象使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> - 连续调用多个页面栈操作方法时，中间过程会被忽略，显示最终的栈操作结果。例如：在Page1页面先pop再push一个Page1，系统会认为操作前和操作后的结果一致而不进行任何操作，如果需要强行push一个Page1实例，可以使用NEW_INSTANCE模式。
> - 不建议开发者通过监听生命周期的方式管理自己的页面栈。

#### init()

```cangjie
public init()
```

**功能：** 创建NavPathStack类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func clear(Bool)

```cangjie
public func clear(animated!: Bool = true): Unit
```

**功能：** 清除栈中所有页面。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|animated|Bool|否|true|是否支持转场动画。|

#### func disableAnimation(Bool)

```cangjie
public func disableAnimation(value: Bool): Unit
```

**功能：** 关闭（true）或打开（false）当前Navigation中所有转场动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否关闭转场动画。|

#### func getAllPathName()

```cangjie
public func getAllPathName(): Array<String>
```

**功能：** 获取栈中所有NavDestination页面的名称。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回栈中所有NavDestination页面的名称。|

#### func getIndexByName(String)

```cangjie
public func getIndexByName(name: String): Array<Int32>
```

**功能：** 获取全部名为name的NavDestination页面的位置索引。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| NavDestination页面名称。 |

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>| 全部名为name的NavDestination页面的位置索引。|

#### func getParamByIndex(Int32)

```cangjie
public func getParamByIndex(index: Int32): String
```

**功能：** 获取index指定的NavDestination页面的参数信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|NavDestination页面的位置索引。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回对应NavDestination页面的参数信息。|

#### func getParamByName(String)

```cangjie
public func getParamByName(name: String): Array<String>
```

**功能：** 获取全部名为name的NavDestination页面的参数信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|全部名为name的NavDestination页面的参数信息。|