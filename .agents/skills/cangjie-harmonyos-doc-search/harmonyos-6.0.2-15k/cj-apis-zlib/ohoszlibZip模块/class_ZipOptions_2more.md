## class ZipOptions

```cangjie
public class ZipOptions {
    public let level: CompressLevel
    public let memLevel: MemLevel
    public let strategy: CompressStrategy
    public init(level: CompressLevel, memLevel: MemLevel, strategy: CompressStrategy)
}
```

**功能：** 压缩模式的选择项。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 19

### let level

```cangjie
public let level: CompressLevel
```

**功能：** 压缩速度级别。参考[CompressLevel枚举定义](#enum-compresslevel)。

**类型：** [CompressLevel](#enum-compresslevel)

**读写能力：** 只读

**起始版本：** 19

### let memLevel

```cangjie
public let memLevel: MemLevel
```

**功能：** 压缩内存级别。参考[MemLevel枚举定义](#enum-memlevel)。

**类型：** [MemLevel](#enum-memlevel)

**读写能力：** 只读

**起始版本：** 19

### let strategy

```cangjie
public let strategy: CompressStrategy
```

**功能：** 压缩策略。参考[CompressStrategy枚举定义](#enum-compressstrategy)。

**类型：** [CompressStrategy](#enum-compressstrategy)

**读写能力：** 只读

**起始版本：** 19

### init(CompressLevel, MemLevel, CompressStrategy)

```cangjie
public init(level: CompressLevel, memLevel: MemLevel, strategy: CompressStrategy)
```

**功能：** 创建压缩模式的选择项对象。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 19

**参数：**

|参数名|类型|必填性|说明|
|:---|:---|:---|:---|
|level|[CompressLevel](#enum-compresslevel)|是|压缩速度级别。参考[CompressLevel枚举定义](#enum-compresslevel)。|
|memLevel|[MemLevel](#enum-memlevel)|是|压缩内存级别。参考[MemLevel枚举定义](#enum-memlevel)。|
|strategy|[CompressStrategy](#enum-compressstrategy)|是|压缩策略。参考[CompressStrategy枚举定义](#enum-compressstrategy)。|

## class ZipOutputInfo

```cangjie
public class ZipOutputInfo {
    public let status: ReturnStatus
    public let destLen: Int64
}
```

**功能：** 压缩返回结果。

**系统能力：** SystemCapability.BundleManager.Zlib

**起始版本：** 20

### let destLen

```cangjie
public let destLen: Int64
```

**功能：** 目标缓冲区的总长度。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 20

### let status

```cangjie
public let status: ReturnStatus
```

**功能：** 参考[ReturnStatus枚举定义](#enum-returnstatus)。

**类型：** [ReturnStatus](#enum-returnstatus)

**读写能力：** 只读

**起始版本：** 20