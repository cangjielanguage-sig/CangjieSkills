## class BundleManager

```cangjie
public class BundleManager {}
```

**功能：** 提供Bundle信息查询方法的类。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

### static func canOpenLink(String)

```cangjie
public static func canOpenLink(link: String): Bool
```

**功能：** 根据给定的链接判断目标应用是否可访问，链接中的scheme需要在module.json5文件的querySchemes字段下配置。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|link|String|是|-|表示需要查询的链接。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示给定的链接可以打开，返回false表示给定的链接不能打开。|

**异常：**

- BusinessException：对应错误码如下表，详见[包管理子系统通用错误码](./cj-errorcode-bundle.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17700055 | The specified link is invalid. |
  | 17700056 | The scheme of the specified link is not in the querySchemes. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let link = "app1Scheme://test.example.com/home"
    let canOpen = BundleManager.canOpenLink(link)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func getBundleInfoForSelf(Int32)

```cangjie
public static func getBundleInfoForSelf(bundleFlags: Int32): BundleInfo
```

**功能：** 根据给定的bundleFlags获取当前应用的BundleInfo。

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleFlags|Int32|是|-|指定返回的BundleInfo所包含的信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[BundleInfo](#class-bundleinfo)|BundleInfo对象，返回当前应用的BundleInfo。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let bundleFlags = BundleFlag.GET_BUNDLE_INFO_DEFAULT | BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION | BundleFlag.GET_BUNDLE_INFO_WITH_HAP_MODULE | BundleFlag.GET_BUNDLE_INFO_WITH_ABILITY
    let res = BundleManager.getBundleInfoForSelf(bundleFlags)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```