## class RouterItem

```cangjie
public class RouterItem {
    public let name: String
    public let pageSourceFile: String
    public let buildFunction: String
    public let data: Array<DataItem>
    public let customData: String
}
```

**功能：** 描述模块配置的路由表信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let buildFunction

```cangjie
public let buildFunction: String
```

**功能：** 标识被@Builder修饰的函数，该函数描述页面的UI。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let customData

```cangjie
public let customData: String
```

**功能：** 标识路由表配置文件中的任意类型的自定义数据，即customData字段的JSON字符串，开发者需要调用JSON.parse函数解析出具体内容。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let data

```cangjie
public let data: Array<DataItem>
```

**功能：** 标识路由表配置文件中的字符串自定义数据，即data字段的信息，该字段已由系统解析，无需开发者自行解析。

**类型：** Array\<[DataItem](#class-dataitem)>

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let name

```cangjie
public let name: String
```

**功能：** 标识跳转页面的名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let pageSourceFile

```cangjie
public let pageSourceFile: String
```

**功能：** 标识页面在模块内的路径。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## class SignatureInfo

```cangjie
public class SignatureInfo {
    public let appId: String
    public let fingerprint: String
    public let appIdentifier: String
}
```

**功能：** 描述应用包的签名信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let appId

```cangjie
public let appId: String
```

**功能：** 应用的appId，表示应用的唯一标识。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let appIdentifier

```cangjie
public let appIdentifier: String
```

**功能：** 应用的唯一标识。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let fingerprint

```cangjie
public let fingerprint: String
```

**功能：** 应用包的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## class UsedScene

```cangjie
public class UsedScene {
    public var abilities: Array<String>
    public var when: String
}
```

**功能：** 描述权限使用的场景和时机。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### var abilities

```cangjie
public var abilities: Array<String>
```

**功能：** 使用到该权限的Ability集合。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### var when

```cangjie
public var when: String
```

**功能：** 使用该权限的时机。支持的取值有inuse（使用时）、always（始终）。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22