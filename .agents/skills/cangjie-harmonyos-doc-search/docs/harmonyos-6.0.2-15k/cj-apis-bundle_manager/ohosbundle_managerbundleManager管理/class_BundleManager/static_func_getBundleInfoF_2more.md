### static func getBundleInfoForSelf(Int32)

```cangjie
public static func getBundleInfoForSelf(bundleFlags: Int32): BundleInfo
```

**功能：** 根据给定的bundleFlags获取当前应用的BundleInfo。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleFlags|Int32|是|-|指定返回的BundleInfo所包含的信息，具体可参考[BundleFlag](#enum-bundleflag)。|

**返回值：**

|类型|说明|
|:----|:----|
|[BundleInfo](#class-bundleinfo)|BundleInfo对象，返回当前应用的BundleInfo。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|

**示例1：**

```cangjie
// index.cj

import kit.AbilityKit.*

let bundleFlags = GET_BUNDLE_INFO_DEFAULT.getValue()
let res = BundleManager.getBundleInfoForSelf(bundleFlags)
```

**示例2：**

```cangjie
// index.cj

import kit.AbilityKit.*

let bundleFlags = GET_BUNDLE_INFO_DEFAULT.getValue() | GET_BUNDLE_INFO_WITH_APPLICATION.getValue() |
    GET_BUNDLE_INFO_WITH_HAP_MODULE.getValue() | GET_BUNDLE_INFO_WITH_ABILITY.getValue()
let res = BundleManager.getBundleInfoForSelf(bundleFlags)
```

### static func getBundleNameByUid(Int32)

```cangjie
public static func getBundleNameByUid(uid: Int32): String
```

**功能：** 根据给定的uid获取对应应用的bundleName。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uid|Int32|是|-|表示应用程序的UID。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回获取到的bundleName。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |17700021|The specified uid is invalid.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let bundleFlags = GET_BUNDLE_INFO_DEFAULT.getValue()
try {
    let bundleinfo = BundleManager.getBundleInfo("com.example.myapplication",
            (GET_BUNDLE_INFO_DEFAULT.getValue() | GET_BUNDLE_INFO_WITH_APPLICATION.getValue()))
    let name = BundleManager.getBundleNameByUid(bundleinfo
            .appInfo
            .uid)
} catch (e: BusinessException) {
    AppLog.error("getBundleNameByUid failed, errcode is ${e.code}")
}
```