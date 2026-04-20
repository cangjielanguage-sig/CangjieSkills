### static prop marketName

```cangjie
public static prop marketName: String
```

**功能：** 外部产品系列。例如“<!--RP2-->Mate XX<!--RP2End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop osFullName

```cangjie
public static prop osFullName: String
```

**功能：** 系统版本，版本格式OpenHarmony-x.x.x.x,x为数值。例如“OpenHarmony-6.0.2.126”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop osReleaseType

```cangjie
public static prop osReleaseType: String
```

**功能：** 系统的发布类型，取值为：

Canary：面向特定开发者发布的早期预览版本，不承诺API稳定性。

Beta：面向开发者公开发布的Beta版本，不承诺API稳定性。

Release：面向开发者公开发布的正式版本，承诺API稳定性。

例如“<!--RP9-->Canary/Beta/Release<!--RP9End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop productModel

```cangjie
public static prop productModel: String
```

**功能：** 认证型号。例如“<!--RP4-->TAS-AL00<!--RP4End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop productSeries

```cangjie
public static prop productSeries: String
```

**功能：** 产品系列。例如“<!--RP3-->TAS<!--RP3End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop sdkApiVersion

```cangjie
public static prop sdkApiVersion: Int32
```

**功能：** 系统软件API版本。例如“22”。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop securityPatchTag

```cangjie
public static prop securityPatchTag: String
```

**功能：** 安全补丁级别。例如“<!--RP7-->2026/01/31<!--RP7End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop seniorVersion

```cangjie
public static prop seniorVersion: Int32
```

**功能：** Senior版本号，随局部架构、重大特性增加，值为osFullName中的第二位数值，建议直接使用deviceInfo.seniorVersion获取，可提升效率，不建议开发者自主解析osFullName获取。
例如“0”。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop serial

```cangjie
public static prop serial: String
```

**功能：** 设备序列号SN(Serial Number)。序列号随设备差异。

> **说明：**
>
> 可作为设备唯一识别码。

**类型：** String

**读写能力：** 只读

**需要权限：** ohos.permission.sec.ACCESS_UDID

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop softwareModel

```cangjie
public static prop softwareModel: String
```

**功能：** 内部软件子型号。例如“<!--RP5-->TAS-AL00<!--RP5End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop udid

```cangjie
public static prop udid: String
```

**功能：** 设备Udid。例如“9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412”。

> **说明：**
>
> 数据长度为65字节。可作为设备唯一识别码。

**类型：** String

**读写能力：** 只读

**需要权限：** ohos.permission.sec.ACCESS_UDID

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22