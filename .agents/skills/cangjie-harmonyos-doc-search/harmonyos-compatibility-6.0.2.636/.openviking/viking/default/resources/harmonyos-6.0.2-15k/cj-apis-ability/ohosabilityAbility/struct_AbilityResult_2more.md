## struct AbilityResult

```cangjie
public struct AbilityResult {
    public AbilityResult(
        public let resultCode: Int32,
        public let want: Want
    )
}
```

**功能：** 定义Ability拉起、销毁之后返回的结果码和数据。
可以通过startAbilityForResult获取对端Ability销毁后返回的AbilityResult对象，被startAbilityForResult拉起的Ability对象可以通过terminateSelfWithResult返回AbilityResult对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### let resultCode

```cangjie
public let resultCode: Int32
```

**功能：** 表示ability拉起、销毁之后返回的结果码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### let want

```cangjie
public let want: Want
```

**功能：** 表示ability销毁之后返回的数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [Want](#class-want)

**读写能力：** 只读

**起始版本：** 12

### AbilityResult(Int32, Want)

```cangjie
public AbilityResult(
    public let resultCode: Int32,
    public let want: Want
)
```

**功能：** 定义Ability拉起、销毁之后返回的结果码和数据。
可以通过startAbilityForResult获取对端Ability销毁后返回的AbilityResult对象，被startAbilityForResult拉起的Ability对象可以通过terminateSelfWithResult返回AbilityResult对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|resultCode|Int32|是|-|表示ability拉起、销毁之后返回的结果码。|
|want|[Want](#class-want)|是|-|表示ability销毁之后返回的数据。|

## struct ErrorObject

```cangjie
public struct ErrorObject {
    public let name: String
    public let message: String
    public let stack: Option<String>
    public init(name: String, message: String, stack!: Option<String> = None)
}
```

**功能：** 异常事件信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### let message

```cangjie
public let message: String
```

**功能：** 异常事件消息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 异常事件名字。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let stack

```cangjie
public let stack: Option<String>
```

**功能：** 异常事件错误堆栈信息。默认是None。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Option\<String>

**读写能力：** 只读

**起始版本：** 12

### init(String, String, Option\<String>)

```cangjie
public init(name: String, message: String, stack!: Option<String> = None)
```

**功能：** ErrorObject主构造函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|异常事件名字。|
|message|String|是|-|异常事件消息。|
|stack|Option\<String>|否|None| **命名参数。** 异常事件错误堆栈信息。默认是None。|