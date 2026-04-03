# ohos.app.ability.want（Want）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

Want是对象间信息传递的载体，可以用于应用组件间的信息传递。

其典型应用场景之一是，当[UIAbility](./cj-apis-app-ability-ui_ability.md#class-uiability) A启动 UIAbility B、并需要传入一些数据时，可使用[Want](#class-want)作为载体。例如在[startAbility](./cj-apis-app-ability-ui_ability.md#func-startabilitywant-startoptions)接口的入参want中，可以通过abilityName指定启动的目标Ability，也可以通过parameters等字段携带其他数据。

## 导入模块

```cangjie
import kit.AbilityKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

ohos.permission.PREPARE_APP_TERMINATE

ohos.permission.PRIVACY_WINDOW

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](./cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。