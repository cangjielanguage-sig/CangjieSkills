# ohos.account_distributedAccount（分布式账号管理）

本模块提供管理分布式账号的一些基础功能，主要包括查询和更新账号登录状态。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

ohos.permission.GET_DISTRIBUTED_ACCOUNTS

ohos.permission.MANAGE_DISTRIBUTED_ACCOUNTS

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getDistributedAccountAbility()

```cangjie
public func getDistributedAccountAbility(): DistributedAccountAbility
```

**功能：** 获取分布式账号单实例对象。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DistributedAccountAbility](#class-distributedaccountability)|返回一个实例，实例提供查询和更新分布式账号登录状态方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  | :--- | :--- |
  | 201      | Permission denied.        |
  | 12300001 | System service exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let ability: DistributedAccountAbility = getDistributedAccountAbility()
```