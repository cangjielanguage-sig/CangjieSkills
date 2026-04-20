### class NavPathInfo

```cangjie
public class NavPathInfo {
    public var name: String
    public var param: String
    public var onPop: Option<(PopInfo) -> Unit> = None

    public init(name: String, param: String)
    public init(name: String, param: String, onPop: Option<(PopInfo) -> Unit>)
}
```

**功能：** 保存路由页面信息的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var name

```cangjie
public var name: String
```

**功能：** 表示NavDestination页面名称。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### var onPop

```cangjie
public var onPop: Option<(PopInfo) -> Unit> = None
```

**功能：** 表示NavDestination页面触发[pop](#func-popbool)时返回的回调。仅[pop](#func-popbool)中设置result参数后触发。

**类型：** <([PopInfo](#class-popinfo))->Unit>

**读写能力：** 可读写

**起始版本：** 20

#### var param

```cangjie
public var param: String
```

**功能：** 表示NavDestination页面详细参数。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

#### init(String, String)

```cangjie
public init(name: String, param: String)
```

**功能：** 创建NavPathInfo。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。|
|param|String|是|-|NavDestination页面详细参数。|

#### init(String, String, Option\<(PopInfo) -> Unit>)

```cangjie
public init(name: String, param: String, onPop: Option<(PopInfo) -> Unit>)
```

**功能：** 创建NavPathInfo。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|NavDestination页面名称。|
|param|String|是|-|NavDestination页面详细参数。|
|onPop|([PopInfo](#class-popinfo))->Unit|是|-| NavDestination页面触发[pop](#func-popbool)时返回的回调。仅[pop](#func-popbool)中设置result参数后触发。|