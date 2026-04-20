## class SkillUri

```cangjie
public class SkillUri {
    public let scheme: String
    public let host: String
    public let port: Int32
    public let path: String
    public let pathStartWith: String
    public let pathRegex: String
    public let uriType: String
    public let utd: String
    public let maxFilesSupported: Int32
    public let linkFeature: String
}
```

**功能：** 描述标识URI信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let host

```cangjie
public let host: String
```

**功能：** 标识 URI 主机地址部分，仅当 scheme 存在时才生效。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let linkFeature

```cangjie
public let linkFeature: String
```

**功能：** 标识 URI 提供的功能类型，用于实现应用间跳转，仅在AbilityInfo中存在。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let maxFilesSupported

```cangjie
public let maxFilesSupported: Int32
```

**功能：** 对于指定类型的文件，标识一次能接收或打开的最大数量。取值范围：不小于0的整数。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let path

```cangjie
public let path: String
```

**功能：** 标识 URI 路径部分，仅当 scheme 和 host 同时存在时才生效。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let pathRegex

```cangjie
public let pathRegex: String
```

**功能：** 标识 URI 路径部分，用于正则匹配，仅当 scheme 和 host 同时存在时才生效。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let pathStartWith

```cangjie
public let pathStartWith: String
```

**功能：** 标识 URI 路径部分，用于前缀匹配，仅当 scheme 和 host 同时存在时才生效。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let port

```cangjie
public let port: Int32
```

**功能：** 标识 URI 端口，仅当 scheme 和 host 同时存在时才生效。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let scheme

```cangjie
public let scheme: String
```

**功能：** 标识 URI 协议名，常见的有http、https、file、ftp等。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let uriType

```cangjie
public let uriType: String
```

**功能：** 标识与Want相匹配的数据类型，使用MIME（Multipurpose&nbsp;Internet&nbsp;Mail&nbsp;Extensions）类型规范和UniformDataType类型规范。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let utd

```cangjie
public let utd: String
```

**功能：** 标识与 Want 相匹配的 URI 的标准化数据类型，适用于分享等场景。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22