## struct ConfigOption

```cangjie
public struct ConfigOption {
    public let disable: Bool
    public let maxStorage: String
    public ConfigOption(maxStorage: String, disable!: Bool = false)
}
```

**功能：** 提供了对应用事件打点功能的配置选项。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let disable

```cangjie
public let disable: Bool
```

**功能：** 打点功能开关，默认值为false。true：关闭打点功能，false：不关闭打点功能。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let maxStorage

```cangjie
public let maxStorage: String
```

**功能：** 打点数据存放目录的配额大小，默认值为“10M”。

在目录大小超出配额后，下次打点会触发对目录的清理操作：按从旧到新的顺序逐个删除打点数据文件，直到目录大小不超出配额时结束。

配额值字符串规格如下：

- 配额值字符串只由数字字符和大小单位字符（单位字符支持[b\|k\|kb\|m\|mb\|g\|gb\|t\|tb]，不区分大小写）构成。
- 配额值字符串必须以数字开头，后面可以选择不传单位字符（默认使用byte作为单位），或者以单位字符结尾。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### ConfigOption(String, Bool)

```cangjie
public ConfigOption(maxStorage: String, disable!: Bool = false)
```

**功能：** 创建[ConfigOption](#struct-configoption)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maxStorage|String|是|-|打点数据存放目录的配额大小，默认值为“10M”。<br>在目录大小超出配额后，下次打点会触发对目录的清理操作：按从旧到新的顺序逐个删除打点数据文件，直到目录大小不超出配额时结束。<br>配额值字符串规格如下：<br>- 配额值字符串只由数字字符和大小单位字符（单位字符支持[b\|k\|kb\|m\|mb\|g\|gb\|t\|tb]，不区分大小写）构成。<br>- 配额值字符串必须以数字开头，后面可以选择不传单位字符（默认使用byte作为单位），或者以单位字符结尾。|
|disable|Bool|否|false| **命名参数。** 打点功能开关，默认值为false。true：关闭打点功能，false：不关闭打点功能。|