## class ConfigOption

```cangjie
public class ConfigOption {
    public var disable: Bool
    public var maxStorage: String
    public init(disable!: Bool = false, maxStorage!: String = "10M")
}
```

**功能：** 提供对应用事件打点功能的配置选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var disable

```cangjie
public var disable: Bool
```

**功能：** 打点功能开关。true：关闭打点功能，false：开启打点功能。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### var maxStorage

```cangjie
public var maxStorage: String
```

**功能：** 打点数据存放目录的配额大小。建议配额大小不超过10M，配额过大可能会影响接口效率。

在目录大小超出配额后，下次打点会触发对目录的清理操作：按从旧到新的顺序逐个删除打点数据文件，直到目录大小不超出配额时结束。

配额值字符串规格如下：

- 配额值字符串只由数字字符和大小单位字符（单位字符支持[b\|k\|kb\|m\|mb\|g\|gb\|t\|tb]，不区分大小写）构成。

- 配额值字符串必须以数字开头，后面可以选择不传单位字符（默认使用byte作为单位），或者以单位字符结尾。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### init(Bool, String)

```cangjie
public init(disable!: Bool = false, maxStorage!: String = "10M")
```

**功能：** 创建[ConfigOption](#class-configoption)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|disable|Bool|否|false|**命名参数。** 打点功能开关。|
|maxStorage|String|否|"10M"|**命名参数。** 打点数据存放目录的配额大小，默认值为“10M”。建议配额大小不超过10M，配额过大可能会影响接口效率。|

## class Domain

```cangjie
public class Domain {
    public static const OS = "OS"
}
```

**功能：** 提供领域名称常量。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### static const OS

```cangjie
public static const OS = "OS"
```

**功能：** 系统领域。

**类型：** String

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22