## class DataItem

```cangjie
public class DataItem {
    public let key: String
    public let value: String
}
```

**功能：** 描述模块配置的路由表中的自定义数据。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let key

```cangjie
public let key: String
```

**功能：** 标识路由表自定义数据的键。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let value

```cangjie
public let value: String
```

**功能：** 标识路由表自定义数据的值。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

## class DefaultAppManager

```cangjie
public class DefaultAppManager {}
```

**功能：** 该类提供查询默认应用的能力，支持查询当前应用是否是默认应用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**起始版本：** 22

### static func isDefaultApplication(ApplicationType)

```cangjie
public static func isDefaultApplication(appType: ApplicationType): Bool
```

**功能：** 根据系统已定义的应用类型判断当前应用是否是该类型的默认应用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appType|ApplicationType|是|-|要查询的应用类型，取[ApplicationType](#enum-applicationtype)类型中的值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回当前应用是否是默认应用，true表示是默认应用，false表示不是默认应用。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let tag = DefaultAppManager.isDefaultApplication(ApplicationType.Image)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## class Dependency

```cangjie
public class Dependency {
    public let bundleName: String
    public let moduleName: String
    public let versionCode: UInt32
}
```

**功能：** 描述模块所依赖的动态共享库信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let bundleName

```cangjie
public let bundleName: String
```

**功能：** 标识当前模块依赖的共享包的包名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let moduleName

```cangjie
public let moduleName: String
```

**功能：** 标识当前模块依赖的共享包模块名。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### let versionCode

```cangjie
public let versionCode: UInt32
```

**功能：** 标识当前共享包的版本号。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22