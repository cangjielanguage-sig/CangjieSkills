## class RouterState

```cangjie
public class RouterState {
    public var index: Int32
    public var name: String
    public var path: String
    public var params: String
    public init(
        index!: Int32,
        name!: String,
        path!: String,
        params!: String
    )
}
```

**功能：** 页面状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var index

```cangjie
public var index: Int32
```

**功能：** 表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 表示当前页面的名称，即对应文件名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var path

```cangjie
public var path: String
```

**功能：** 表示当前页面的路径。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var params

```cangjie
public var params: String
```

**功能：** 表示当前页面携带的参数。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(Int32, String, String, String)

```cangjie
public init(
    index!: Int32,
    name!: String,
    path!: String,
    params!: String
)
```

**功能：** 创建RouterState对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int32|是|-|**命名参数。** 表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。|
|name|String|是|-|**命名参数。** 表示当前页面的名称，即对应文件名。|
|path|String|是|-|**命名参数。** 表示当前页面的路径。|
|params|String|是|-|**命名参数。** 表示当前页面携带的参数。|

## enum RouterMode

```cangjie
public enum RouterMode <: Equatable<RouterMode> {
    | Standard
    | Single
    | ...
}
```

**功能：** 路由跳转模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- Equatable\<[RouterMode](#enum-routermode)>

### Standard

```cangjie
Standard
```

**功能：** 多实例模式，也是默认情况下的跳转模式。目标页面会被添加到页面栈顶，无论栈中是否存在相同url的页面。不使用路由跳转模式时，则按照默认的多实例模式进行跳转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### Single

```cangjie
Single
```

**功能：** 单实例模式。如果目标页面的url已经存在于页面栈中，则该url页面移动到栈顶。如果目标页面的url在页面栈中不存在同url页面，则按照默认的多实例模式进行跳转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### operator func !=(RouterMode)

```cangjie
public operator func !=(other: RouterMode): Bool
```

**功能：** 比较两个枚举值是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RouterMode](#enum-routermode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不相等则返回true，否则返回false。|

### operator func ==(RouterMode)

```cangjie
public operator func ==(other: RouterMode): Bool
```

**功能：** 比较两个枚举值是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[RouterMode](#enum-routermode)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等则返回true，否则返回false。|