## class AtManager

```cangjie
public class AtManager {}
```

**功能：** 管理访问控制模块的实例。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

### func checkAccessToken(UInt32, Permissions)

```cangjie
public func checkAccessToken(tokenID: UInt32, permissionName: Permissions): GrantStatus
```

**功能：** 校验应用是否授予权限。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tokenID|UInt32|是|-|要校验的目标应用的身份标识。可通过应用的[ApplicationInfo](cj-apis-bundle_manager.md#class-applicationinfo)的accessTokenId字段获得。|
|permissionName|[Permissions](#type-permissions)|是|-|需要校验的权限名称，合法的权限名取值可在[应用权限列表](../../security/AccessToken/cj-app-permissions.md)中查询。|

**返回值：**

|类型|说明|
|:----|:----|
|[GrantStatus](#enum-grantstatus)|返回授权状态结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[访问控制错误码](./cj-errorcode-access-token.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let atManager = AbilityAccessCtrl.createAtManager()
    let tokenID : UInt32 = 1 // tokenID系统应用可以通过bundleManager.getApplicationInfo获取，普通应用可以通过bundleManager.getBundleInfoForSelf获取
    let status = atManager.checkAccessToken(tokenID, "ohos.permission.READ_CONTACTS")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```