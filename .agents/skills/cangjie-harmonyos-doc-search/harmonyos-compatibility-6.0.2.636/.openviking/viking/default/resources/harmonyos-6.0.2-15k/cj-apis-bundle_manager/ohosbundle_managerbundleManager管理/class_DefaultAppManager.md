## class DefaultAppManager

```cangjie
public class DefaultAppManager {}
```

**功能：** 该类提供查询默认应用的能力，支持查询当前应用是否是默认应用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

### static func isDefaultApplication(String)

```cangjie
public static func isDefaultApplication(appType: String): Bool
```

**功能：** 根据系统已定义的应用类型，判断当前应用是否是该类型的默认应用。

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|appType|String|是|-|要查询的应用类型，取[ApplicationType](#enum-applicationtype)中的值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回当前应用是否是默认应用，true表示是默认应用，false表示不是默认应用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

let tag = DefaultAppManager.isDefaultApplication(ApplicationType.IMAGE.getValue())
```