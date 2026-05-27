## struct RouterItem

```cangjie
public struct RouterItem {
    public let name: String
    public let pageSourceFile: String
    public let buildFunction: String
    public let data: Array<DataItem>
    public let customData: String
}
```

**功能：** 描述模块配置的路由表信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

### let buildFunction

```cangjie
public let buildFunction: String
```

**功能：** 标识被@Builder修饰的函数，该函数描述页面的UI。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let customData

```cangjie
public let customData: String
```

**功能：** 标识路由表配置文件中的任意类型的自定义数据。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let data

```cangjie
public let data: Array<DataItem>
```

**功能：** 标识路由表配置文件中的字符串自定义数据，即data字段的信息，该字段已由系统解析，无需开发者自行解析。

**类型：** Array\<[DataItem](#struct-dataitem)>

**读写能力：** 只读

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 标识跳转页面的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let pageSourceFile

```cangjie
public let pageSourceFile: String
```

**功能：** 标识页面在模块内的路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

## struct Skill

```cangjie
public struct Skill {
    public let actions: Array<String>
    public let entities: Array<String>
    public let uris: Array<SkillUri>
    public let domainVerify: Bool
}
```

**功能：** skill标签对象，三方应用可以通过[getBundleInfoForSelf](#static-func-getbundleinfoforselfint32)获取skill信息，其中入参bundleFlags至少包含 GET_BUNDLE_INFO_WITH_HAP_MODULE、GET_BUNDLE_INFO_WITH_ABILITY 和 GET_BUNDLE_INFO_WITH_SKILL。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

### let actions

```cangjie
public let actions: Array<String>
```

**功能：** Skill接收的Action集合。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### let domainVerify

```cangjie
public let domainVerify: Bool
```

**功能：** Skill接收的DomainVerify值，仅在AbilityInfo中存在。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let entities

```cangjie
public let entities: Array<String>
```

**功能：** Skill接收的Entity集合。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### let uris

```cangjie
public let uris: Array<SkillUri>
```

**功能：** Want匹配的Uri集合。

**类型：** Array\<[SkillUri](#struct-skilluri)>

**读写能力：** 只读

**起始版本：** 19