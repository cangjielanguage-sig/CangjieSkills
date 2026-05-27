## class BundleManager

```cangjie
public class BundleManager {}
```

**功能：** 提供Bundle信息查询方法的类。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 12

### static func canOpenLink(String)

```cangjie
public static func canOpenLink(link: String): Bool
```

**功能：** 查询给定的链接是否可以打开。指定链接的scheme需要在module.json文件的querySchemes字段下配置。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|link|String|是|-|表示需要查询的链接。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示给定的链接可以打开，返回false表示给定的链接不能打开。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[包管理子系统通用错误码](../../errorcodes/cj-errorcode-bundle.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.|
  |17700055|The specified link is invalid.|
  |17700056|The scheme of the specified link is not in the querySchemes.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.hilog.Hilog

let link = "app1Scheme://test.example.com/home"
let canOpen = BundleManager.canOpenLink(link)
```

### static func getBundleInfo(String, Int32, ?Int32)

```cangjie
public static func getBundleInfo(bundleName: String, bundleFlags: Int32, userId!: ?Int32 = None): BundleInfo
```

**功能：** 根据给定的bundleName、bundleFlags和userId获取BundleInfo。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|是|-|表示要查询的应用Bundle名称。|
|bundleFlags|Int32|是|-|指定返回的BundleInfo所包含的信息，具体可参考[BundleFlag](#enum-bundleflag)。|
|userId|?Int32|否|None|表示用户ID，可以通过[getOsAccountLocalId](../BasicServicesKit/cj-apis-account-osAccount.md#func-getosaccountlocalid)接口获取。|

**返回值：**

|类型|说明|
|:----|:----|
|[BundleInfo](#class-bundleinfo)|BundleInfo对象，返回当前应用的BundleInfo。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |17700001|The specified bundleName is not found.|
  |17700004|The specified user id is not found.|
  |17700026|The specified bundle is disabled.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let bundleFlags = GET_BUNDLE_INFO_DEFAULT.getValue()
try {
    let res = BundleManager.getBundleInfo("com.example.myapplication", bundleFlags)
} catch (e: BusinessException) {
    AppLog.error("getBundleInfo failed, errcode is ${e.code}")
}
```