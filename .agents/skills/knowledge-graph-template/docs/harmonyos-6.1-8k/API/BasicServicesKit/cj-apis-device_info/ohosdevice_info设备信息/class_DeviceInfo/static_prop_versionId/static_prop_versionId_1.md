### static prop versionId

```cangjie
public static prop versionId: String
```

**功能：** 版本ID。由deviceType、manufacture、brand、productSeries、osFullName、productModel、softwareModel、sdkApiVersion、incrementalVersion、buildType拼接组成。例如“wearable/TAS/OpenHarmony-6.0.2.126/TAS-AL00/TAS-AL00/22/default/release:nolog”。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog