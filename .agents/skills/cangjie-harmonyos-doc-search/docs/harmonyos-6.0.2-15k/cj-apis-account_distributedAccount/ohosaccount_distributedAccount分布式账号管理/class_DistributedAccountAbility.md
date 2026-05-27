## class DistributedAccountAbility

```cangjie
public class DistributedAccountAbility {}
```

**功能：** 提供查询和更新分布式账号登录状态方法（需要先获取分布式账号的单实例对象）。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

### func getOsAccountDistributedInfo()

```cangjie
public func getOsAccountDistributedInfo(): DistributedInfo
```

**功能：** 获取分布式账号信息。

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS（仅系统应用可申请）或ohos.permission.GET_DISTRIBUTED_ACCOUNTS（仅系统应用可申请）或ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
| DistributedInfo | 当获取分布式账号信息成功，err为undefined，data为获取到的分布式账号信息对象；否则为错误对象。 |

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|
  |12300001|System service exception.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let ability: DistributedAccountAbility = getDistributedAccountAbility()
let accountInfo: DistributedInfo = DistributedInfo("name", "002", OhosAccountEvent.LOGIN, nickname: "nkname", avatar: "avatar", status: DistributedAccountStatus.LOGGED_IN)
ability.setOsAccountDistributedInfo(accountInfo)
let accountInfo_get: DistributedInfo = ability.getOsAccountDistributedInfo()
```

### func setOsAccountDistributedInfo(DistributedInfo)

```cangjie
public func setOsAccountDistributedInfo(accountInfo: DistributedInfo): Unit
```

**功能：** 更新分布式账号信息。

**需要权限：** ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|accountInfo|[DistributedInfo](#class-distributedinfo)|是|-|分布式账号信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                                     |
  | :--- | :--- |
  | 201      | Permission denied.                                           |
  | 401      | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception.                                    |
  | 12300002 | Invalid accountInfo.                                         |
  | 12300003 | Account not found.                                           |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let ability: DistributedAccountAbility = getDistributedAccountAbility()
let accountInfo: DistributedInfo = DistributedInfo("name", "002", OhosAccountEvent.LOGIN, nickname: "nkname", avatar: "avatar", status: DistributedAccountStatus.LOGGED_IN)
ability.setOsAccountDistributedInfo(accountInfo)
```