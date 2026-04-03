## class ExecuteResult

```cangjie
public class ExecuteResult {
    public var code: Int32
    public var result: String
    public var uris: Array<String>
    public var flags: Int32
    public init(code: Int32, result!: String = "", uris!: Array<String> = [], flags!: Int32 = 0)
}
```

**功能：** 意图调用的返回结果。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

### var code

```cangjie
public var code: Int32
```

**功能：** 意图调用返回的错误码。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20

### var flags

```cangjie
public var flags: Int32
```

**功能：** 意图调用时，意图执行方给意图调用方授权的uris的[Flags](#enum-flags)。该参数仅支持FLAG_AUTH_READ_URI_PERMISSION、FLAG_AUTH_WRITE_URI_PERMISSION、FLAG_AUTH_READ_URI_PERMISSION|FLAG_AUTH_WRITE_URI_PERMISSION。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20

### var result

```cangjie
public var result: String
```

**功能：** 意图调用返回的结果。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### var uris

```cangjie
public var uris: Array<String>
```

**功能：** 意图调用时，意图执行方给意图调用方授权的URI列表。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 20

### init(Int32, String, Array\<String>, Int32)

```cangjie
public init(code: Int32, result!: String = "", uris!: Array<String> = [], flags!: Int32 = 0)
```

**功能：** 意图调用的返回结果的构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|Int32|是|-|意图调用返回的错误码。|
|result|String|否|""|意图调用返回的结果。|
|uris|Array\<String>|否|[]|意图调用时，意图执行方给意图调用方授权的URI列表。|
|flags|Int32|否|0|意图调用时，意图执行方给意图调用方授权的uris的[Flags](#enum-flags)。|