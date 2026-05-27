## class APILevel

```cangjie
public class APILevel {
    public let level: UInt8
    public let atomicservice: Bool
    public let crossplatform: Bool
    public let deprecated: UInt8
    public let form: Bool
    public let permission:?PermissionValue
    public let stagemodelonly: Bool
    public let syscap: String
    public const init(level_val: UInt8, atomicservice!: Bool = false, crossplatform!: Bool = false,
        deprecated!: UInt8 = 0, form!: Bool = false, permission!: ?PermissionValue= None,
        stagemodelonly!: Bool = true, syscap!: String = "")
}
```

**功能：** 标签的定义。标签以注解的形式打在api上。标签包括atomicservice（是否支持元服务）、crossplatform（是否支持跨平台）、deprecated（废弃版本）、form（是否支持在form中使用）、permission（所需权限）、since（api等级）、stagemodelonly（是否仅支持Stage模型）、syscap（所需系统能力）等信息。

**起始版本：** 19

### let atomicservice

```cangjie
public let atomicservice: Bool
```

**功能：** 当前api是否支持元服务。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let crossplatform

```cangjie
public let crossplatform: Bool
```

**功能：** 当前api是否支持跨平台。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let deprecated

```cangjie
public let deprecated: UInt8
```

**功能：** 当前api的废弃版本，默认为0表示未废弃。

**类型：** UInt8

**读写能力：** 只读

**起始版本：** 19

### let form

```cangjie
public let form: Bool
```

**功能：** 当前api是否支持在form中使用。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let level

```cangjie
public let level: UInt8
```

**功能：** 当前api的等级。

**类型：** UInt8

**读写能力：** 只读

**起始版本：** 19

### let permission

```cangjie
public let permission:?PermissionValue
```

**功能：** 当前api所需的权限信息。

**类型：** ?[PermissionValue](#interface-permissionvalue)

**读写能力：** 只读

**起始版本：** 19

### let stagemodelonly

```cangjie
public let stagemodelonly: Bool
```

**功能：** 当前api是否仅支持Stage模型。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let syscap

```cangjie
public let syscap: String
```

**功能：** 当前api所需的系统能力。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### init(UInt8, Bool, Bool, UInt8, Bool, ?PermissionValue, Bool, String)

```cangjie
public const init(level_val: UInt8, atomicservice!: Bool = false, crossplatform!: Bool = false, deprecated!: UInt8 = 0, form!: Bool = false, permission!: ?PermissionValue= None,
    stagemodelonly!: Bool = true, syscap!: String = "")
```

**功能：** APILevel构造器。

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|level_val|UInt8|是|-|api等级。|
|atomicservice|Bool|否|false| **命名参数。** 是否支持元服务。|
|crossplatform|Bool|否|false| **命名参数。** 是否支持跨平台。|
|deprecated|UInt8|否|0| **命名参数。** 废弃版本。|
|form|Bool|否|false| **命名参数。** 是否支持在form中使用。|
|permission|?[PermissionValue](#interface-permissionvalue)|否|None| **命名参数。** 所需权限。|
|stagemodelonly|Bool|否|true| **命名参数。** 是否仅支持Stage模型。|
|syscap|String|否|""| **命名参数。** 所需系统能力。|