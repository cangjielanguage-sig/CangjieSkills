# ohos.ability_delegator_registry（AbilityDelegatorRegistry）

AbilityDelegatorRegistry模块提供用于存储已注册的[AbilityDelegator](#class-abilitydelegator)和[AbilityDelegatorArgs](#class-abilitydelegatorargs)对象的全局寄存器的能力，包括获取应用程序的[AbilityDelegator](#class-abilitydelegator)对象、获取单元测试参数对象。该模块中的接口只能用于测试框架中。

## 导入模块

```cangjie
import kit.TestKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。