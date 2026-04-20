## struct SkillUri

```cangjie
public struct SkillUri {
    public let scheme: String
    public let host: String
    public let port: String
    public let path: String
    public let pathStartWith: String
    public let pathRegex: String
    public let uriType: String
    public let utd: String
    public let maxFileSupported: Int32
    public let linkFeature: String
}
```

**功能：** 描述标识URI信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

### let host

```cangjie
public let host: String
```

**功能：** 标识URI主机地址部分，仅当scheme存在时有意义。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let linkFeature

```cangjie
public let linkFeature: String
```

**功能：** 标识URI提供的功能类型，用于实现应用间跳转，仅在AbilityInfo中存在。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let maxFileSupported

```cangjie
public let maxFileSupported: Int32
```

**功能：** 对于指定类型的文件，标识一次能接收或打开的最大数量。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let path

```cangjie
public let path: String
```

**功能：** 标识URI路径部分，仅当scheme和host同时存在时有意义。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let pathRegex

```cangjie
public let pathRegex: String
```

**功能：** 标识URI路径部分，用于正则匹配，仅当scheme和host同时存在时有意义。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let pathStartWith

```cangjie
public let pathStartWith: String
```

**功能：** 标识URI路径部分，用于前缀匹配，仅当scheme和host同时存在时有意义。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let port

```cangjie
public let port: String
```

**功能：** 标识URI端口部分，仅当scheme和host同时存在时有意义。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let scheme

```cangjie
public let scheme: String
```

**功能：** 标识URI协议名，常见的有http、https、file、ftp等。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let uriType

```cangjie
public let uriType: String
```

**功能：** 标识与Want相匹配的数据类型，使用MIME（Multipurpose Internet Mail Extensions）类型规范。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let utd

```cangjie
public let utd: String
```

**功能：** 标识与Want相匹配的URI的标准化数据类型，适用于分享等场景。

**类型：** String

**读写能力：** 只读

**起始版本：** 19