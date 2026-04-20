## class WantAgentInfo

```cangjie
public class WantAgentInfo {
    public WantAgentInfo(
        public let wants!: Array<Want>,
        public let actionType!: OperationType = UNKNOWN_TYPE,
        public let requestCode!: Int32,
        public let actionFlags!: Array<WantAgentFlags> = Array<WantAgentFlags>(),
        public let extraInfos!: String = ""
    )
}
```

**功能：** 定义触发WantAgent所需要的信息，可以作为[getWantAgent](#func-getwantagentwantagentinfo)的入参创建指定的WantAgent对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### let actionFlags

```cangjie
public let actionFlags: Array<WantAgentFlags> = Array<WantAgentFlags>()
```

**功能：** 动作执行属性。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Array\<[WantAgentFlags](#enum-wantagentflags)>

**读写能力：** 只读

**起始版本：** 19

### let actionType

```cangjie
public let actionType: OperationType = UNKNOWN_TYPE
```

**功能：** 动作类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [OperationType](#enum-operationtype)

**读写能力：** 只读

**起始版本：** 19

### let extraInfos

```cangjie
public let extraInfos: String = ""
```

**功能：** 额外数据。由开发者自行决定传入的json字符串。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let requestCode

```cangjie
public let requestCode: Int32
```

**功能：** 使用者定义的一个私有值。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let wants

```cangjie
public let wants: Array<Want>
```

**功能：** 将被执行的动作列表。wants数组为预留能力，当前只支持一个want。传入多个时只取wants数组的第一个成员。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Array\<[Want](#class-want)>

**读写能力：** 只读

**起始版本：** 19

### WantAgentInfo(Array\<Want>, OperationType, Int32, Array\<WantAgentFlags>, String)

```cangjie
public WantAgentInfo(
    public let wants!: Array<Want>,
    public let actionType!: OperationType = UNKNOWN_TYPE,
    public let requestCode!: Int32,
    public let actionFlags!: Array<WantAgentFlags> = Array<WantAgentFlags>(),
    public let extraInfos!: String = ""
)
```

**功能：** WantAgentInfo的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|wants|Array\<[Want](#class-want)>|是|-| **命名参数。** 将被执行的动作列表。wants数组为预留能力，当前只支持一个want。传入多个时只取wants数组的第一个成员。|
|actionType|[OperationType](#enum-operationtype)|否|UNKNOWN_TYPE| **命名参数。** 动作类型。|
|requestCode|Int32|是|-| **命名参数。** 使用者定义的一个私有值。|
|actionFlags|Array\<[WantAgentFlags](#enum-wantagentflags)>|否|Array\<[WantAgentFlags](#enum-wantagentflags)>()| **命名参数。** 动作执行属性。|
|extraInfos|String|否|""| **命名参数。** 额外数据。由开发者自行决定传入的json字符串。|