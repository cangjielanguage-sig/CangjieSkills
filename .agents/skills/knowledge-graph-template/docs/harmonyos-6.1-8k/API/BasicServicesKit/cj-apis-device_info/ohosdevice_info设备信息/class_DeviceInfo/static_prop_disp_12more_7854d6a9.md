### static prop displayVersion

```cangjie
public static prop displayVersion: String
```

**功能：** 产品版本。例如“<!--RP8-->SGT-AL00 6.0.0.125<!--RP8End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop distributionOSApiName

```cangjie
public static prop distributionOSApiName: String
```

**功能：** 发行版系统api版本名称<!--Del-->，由发行方定义<!--DelEnd-->。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop distributionOSApiVersion

```cangjie
public static prop distributionOSApiVersion: Int32
```

**功能：** 发行版系统api版本<!--Del-->，由发行方定义<!--DelEnd-->。例如“60001”。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop distributionOSName

```cangjie
public static prop distributionOSName: String
```

**功能：** 发行版系统名称<!--Del-->，由发行方定义<!--DelEnd-->。例如“OpenHarmony”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop distributionOSReleaseType

```cangjie
public static prop distributionOSReleaseType: String
```

**功能：** 发行版系统类型<!--Del-->，由发行方定义<!--DelEnd-->。例如“Release”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop distributionOSVersion

```cangjie
public static prop distributionOSVersion: String
```

**功能：** 发行版系统版本号<!--Del-->，由发行方定义<!--DelEnd-->。<!--RP11--><!--RP11End-->例如“6.0.0”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop featureVersion

```cangjie
public static prop featureVersion: Int32
```

**功能：** Feature版本号，标识规划的新特性版本，值为osFullName中的第三位数值，建议直接使用deviceInfo.featureVersion获取，可提升效率，不建议开发者自主解析osFullName获取。例如“0”。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop firstApiVersion

```cangjie
public static prop firstApiVersion: Int32
```

**功能：** 首个版本系统软件API版本。例如“3”。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop hardwareModel

```cangjie
public static prop hardwareModel: String
```

**功能：** 硬件版本号。例如“<!--RP6-->TASA00CVN1<!--RP6End-->”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop incrementalVersion

```cangjie
public static prop incrementalVersion: String
```

**功能：** 差异版本号。例如“default”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop majorVersion

```cangjie
public static prop majorVersion: Int32
```

**功能：** Major版本号，随主版本更新增加，值为osFullName中的第一位数值，建议直接使用deviceInfo.majorVersion获取，可提升效率，不建议开发者解析osFullName获取。例如“5”。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

### static prop manufacture

```cangjie
public static prop manufacture: String
```

**功能：** 设备厂家名称。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22