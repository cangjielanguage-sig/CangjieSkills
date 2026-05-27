# ohos.account.osAccount（系统账号管理）

本模块提供管理系统账号的基础能力，包括系统账号的添加、删除、查询、设置、订阅、启动等功能。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

ohos.permission.MANAGE_LOCAL_ACCOUNTS

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getAccountManager()

```cangjie
public func getAccountManager(): AccountManager
```

**功能：** 获取系统账号管理对象。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AccountManager](#class-accountmanager)|系统账号管理对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let accountManager: AccountManager = getAccountManager()
```