## class Want

```cangjie
public class Want {
    public init(
        deviceId!: String = "",
        bundleName!: String = "",
        abilityName!: String = "",
        moduleName!: String = "",
        flags!: UInt32 = 0,
        uri!: String = "",
        action!: String = "",
        entities!: Array<String> = [],
        `type`!: String = "",
        parameters!: String = ""
    )
}
```

**功能：** 创建相应的 Want。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 12

### prop `type`

```cangjie
public prop `type`: String
```

**功能：** MIME type类型描述，打开文件的类型，主要用于文管打开文件。比如："text/xml" 、 "image/\*"等，MIME定义参考：[Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop abilityName

```cangjie
public prop abilityName: String
```

**功能：** 待启动Ability名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop action

```cangjie
public prop action: String
```

**功能：** 要执行的通用操作（如：查看、分享、应用详情）。在隐式Want中，您可以定义该字段，配合uri或parameters来表示对数据要执行的操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop bundleName

```cangjie
public prop bundleName: String
```

**功能：** 待启动Ability所在的应用Bundle名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop deviceId

```cangjie
public prop deviceId: String
```

**功能：** 运行指定Ability的设备ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop entities

```cangjie
public prop entities: Array<String>
```

**功能：** 目标Ability额外的类别信息（如：浏览器、视频播放器），在隐式Want中是对action字段的补充。在隐式Want中，您可以定义该字段，来过滤匹配Ability类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 12

### prop flags

```cangjie
public prop flags: UInt32
```

**功能：** 处理Want的方式，具体参考：[Flags](#enum-flags)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### prop moduleName

```cangjie
public prop moduleName: String
```

**功能：** 待启动的Ability所属的模块名称。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop parameters

```cangjie
public prop parameters: String
```

**功能：** 开发者自行决定传入的json字符串形式。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### prop uri

```cangjie
public prop uri: String
```

**功能：** Uri描述。如果在Want中指定了Uri，则Want将匹配指定的Uri信息，包括scheme, schemeSpecificPart, authority和path信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19