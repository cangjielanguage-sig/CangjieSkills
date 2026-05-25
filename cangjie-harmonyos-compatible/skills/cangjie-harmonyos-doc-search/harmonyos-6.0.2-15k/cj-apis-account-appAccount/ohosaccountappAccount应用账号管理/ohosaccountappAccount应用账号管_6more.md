# ohos.account.appAccount（应用账号管理）

本模块提供应用账号信息的添加、删除、修改和查询基础能力，并支持应用间鉴权和分布式数据同步功能。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createAppAccountManager()

```cangjie
public func createAppAccountManager(): AppAccountManager
```

**功能：** 创建应用账号管理器对象。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AppAccountManager](#class-appaccountmanager)|应用账号管理器对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let appAccountManager: AppAccountManager = createAppAccountManager()
```

## class AppAccountInfo

```cangjie
public class AppAccountInfo {
    public AppAccountInfo (
        public var owner: String,
        public var name: String
    )
}
```

**功能：** 表示应用账号信息。

**系统能力：** SystemCapability.Account.AppAccount。

**起始版本：** 19

### var owner

```cangjie
public var owner: String
```

**功能：** 应用账号所有者的包名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var name

```cangjie
public var name: String
```

**功能：** 应用账号的名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### AppAccountInfo(String, String)

```cangjie
public AppAccountInfo (
    public var owner: String,
    public var name: String
)
```

**功能：** 构建AppAccountInfo实例。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|owner|String|是|-|应用账号所有者的包名。|
|name|String|是|-|应用账号的名称。|