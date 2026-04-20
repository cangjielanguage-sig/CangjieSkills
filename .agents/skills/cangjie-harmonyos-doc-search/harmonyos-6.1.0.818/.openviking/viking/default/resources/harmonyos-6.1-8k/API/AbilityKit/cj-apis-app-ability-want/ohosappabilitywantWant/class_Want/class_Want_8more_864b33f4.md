## class Want

```cangjie
public class Want {
    public var deviceId: String
    public var bundleName: String
    public var abilityName: String
    public var moduleName: String
    public var flags: UInt32
    public var uri: String
    public var action: String
    public var entities: Array<String>
    public var dataType: String
    public var parameters: HashMap<String, WantValueType>
    public init(
        deviceId!: String = "",
        bundleName!: String = "",
        abilityName!: String = "",
        moduleName!: String = "",
        flags!: UInt32 = 0,
        uri!: String = "",
        action!: String = "",
        entities!: Array<String> = [],
        dataType!: String = "",
        parameters!: HashMap<String, WantValueType> = HashMap<String, WantValueType>(),
        fds!: HashMap<String, Int32> = HashMap<String, Int32>()
    )
}
```

**功能：** 用于描述应用组件启动请求的Want信息。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var abilityName

```cangjie
public var abilityName: String
```

**功能：** 应用的Ability组件名。在应用启动场景中表示被拉起方的Ability组件名。如果在Want中该字段同时指定了BundleName和AbilityName，则Want可以直接匹配到指定的Ability。AbilityName需要在一个应用的范围内保证唯一。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var action

```cangjie
public var action: String
```

**功能：** 表示要执行的通用操作（如：查看、分享、应用详情）。在隐式Want中，开发者可以定义该action字段，配合uri或parameters来表示对数据执行的操作。隐式Want定义及匹配规则请参见[显式Want与隐式Want匹配规则](../../application-models/cj-explicit-implicit-want-mappings.md)。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var bundleName

```cangjie
public var bundleName: String
```

**功能：** 应用包名。在应用启动场景中表示被拉起方的应用包名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** 设备ID。在应用启动场景中表示被拉起方的设备ID，如果未设置该字段，则表示指定当前设备。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var entities

```cangjie
public var entities: Array<String>
```

**功能：** 表示目标Ability额外的类别信息（如：浏览器、视频播放器）。在隐式Want中是对action字段的补充。在隐式Want中，开发者可以定义该entities字段，来过滤匹配Ability类型。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var flags

```cangjie
public var flags: UInt32
```

**功能：** 表示处理Want的方式。值为枚举类型[Flags](./cj-apis-app-ability-want_constant.md#class-flags)，默认传数字。例如取值为0x00000001（即Flags.FLAG_AUTH_READ_URI_PERMISSION）表示临时授予接收方读取该Want对象中URI指向的数据的权限。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### var moduleName

```cangjie
public var moduleName: String
```

**功能：** 应用模块名。在应用启动场景中表示被拉起方的应用模块名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22