# ohos.ability_access_ctrl（程序访问控制管理）

程序访问控制提供程序的权限管理能力，包括鉴权、授权和取消授权等。

## 导入模块

```cangjie
import kit.AbilityKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class AbilityAccessCtrl

```cangjie
public class AbilityAccessCtrl {}
```

**功能：** 此类用于创建管理访问控制模块的实例。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

### static func createAtManager()

```cangjie
public static func createAtManager(): AtManager
```

**功能：** 获取访问控制模块对象。

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[AtManager](#class-atmanager)|获取访问控制模块的实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

let atManager: AtManager = AbilityAccessCtrl.createAtManager()
```