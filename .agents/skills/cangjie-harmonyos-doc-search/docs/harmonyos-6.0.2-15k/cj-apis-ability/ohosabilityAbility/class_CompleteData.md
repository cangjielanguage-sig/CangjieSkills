## class CompleteData

```cangjie
public class CompleteData {
    public CompleteData(
        public let info!: WantAgent,
        public let want!: Want,
        public let finalCode!: Int32,
        public let finalData!: String,
        public let extraInfo!: String
    )
}
```

**功能：** 表示主动激发WantAgent返回的数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### let extraInfo

```cangjie
public let extraInfo: String
```

**功能：** 额外数据。Json字符串。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let finalCode

```cangjie
public let finalCode: Int32
```

**功能：** 触发wantAgent的请求代码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let finalData

```cangjie
public let finalData: String
```

**功能：** 公共事件收集的最终数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let info

```cangjie
public let info: WantAgent
```

**功能：** 触发的wantAgent。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [WantAgent](#class-wantagent)

**读写能力：** 只读

**起始版本：** 19

### let want

```cangjie
public let want: Want
```

**功能：** 存在的被触发的want。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** [Want](#class-want)

**读写能力：** 只读

**起始版本：** 19

### CompleteData(WantAgent, Want, Int32, String, String)

```cangjie
public CompleteData(
    public let info!: WantAgent,
    public let want!: Want,
    public let finalCode!: Int32,
    public let finalData!: String,
    public let extraInfo!: String
)
```

**功能：** CompleteData的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|info|[WantAgent](#class-wantagent)|是|-| **命名参数。** 触发的wantAgent。|
|want|[Want](#class-want)|是|-| **命名参数。** 存在的被触发的want。|
|finalCode|Int32|是|-| **命名参数。** 触发wantAgent的请求代码。|
|finalData|String|是|-| **命名参数。** 公共事件收集的最终数据。|
|extraInfo|String|是|-| **命名参数。** 额外数据。Json字符串。|