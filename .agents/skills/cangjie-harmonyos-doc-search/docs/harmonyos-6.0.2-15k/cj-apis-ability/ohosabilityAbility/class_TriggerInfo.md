## class TriggerInfo

```cangjie
public class TriggerInfo {
    public TriggerInfo(
        public let code!: Int32,
        public let want!: ?Want = None,
        public let permission!: String = "",
        public let extraInfos!: ?String = None
    )
}
```

**功能：** 作为[trigger](#func-triggerwantagent-triggerinfo-completedata---unit)的入参定义触发WantAgent所需要的信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### let code

```cangjie
public let code: Int32
```

**功能：** 提供给目标wantAgent的自定义结果码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let extraInfos

```cangjie
public let extraInfos: ?String = None
```

**功能：** 额外数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let permission

```cangjie
public let permission: String = ""
```

**功能：** 权限定义。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let want

```cangjie
public let want: ?Want = None
```

**功能：** 对象间信息传递的载体，可以用于应用组件间的信息传递。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** ?[Want](#class-want)

**读写能力：** 只读

**起始版本：** 19

### TriggerInfo(Int32, ?Want, String, ?String)

```cangjie
public TriggerInfo(
    public let code!: Int32,
    public let want!: ?Want = None,
    public let permission!: String = "",
    public let extraInfos!: ?String = None
)
```

**功能：** TriggerInfo的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|Int32|是|-| **命名参数。** 提供给目标wantAgent的自定义结果码。|
|want|?[Want](#class-want)|否|None| **命名参数。** 对象间信息传递的载体，可以用于应用组件间的信息传递。|
|permission|String|否|""| **命名参数。** 权限定义。|
|extraInfos|?String|否|None| **命名参数。** 额外数据。|