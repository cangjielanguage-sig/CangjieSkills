## class BaseAbility

```cangjie
abstract sealed class BaseAbility {}
```

**功能：** [UIAbility](#class-uiability)和[ExtensionAbility](#class-extensionability)的基类，提供系统配置更新回调和系统内存调整回调。不支持开发者直接继承该基类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

### Ability的继承关系说明

各类Ability的继承关系如下图所示。

![uiExtensionAbility](../../figures/image-ability-uiExtensionAbility.png)

### static func registerCreator(String, () -> BaseAbility)

```cangjie
public static func registerCreator(name: String, creator: () -> BaseAbility): Unit
```

**功能：** 注册BaseAbility的对应的creator。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|注册 UIAbility 的名称。|
|creator|()->[BaseAbility](#class-baseability)|是|-|注册BaseAbility的对应的creator。|

### func onConfigurationUpdate(AbilityConfiguration)

```cangjie
public open func onConfigurationUpdate(newConfig: AbilityConfiguration): Unit
```

**功能：** 当系统配置更新时调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newConfig|[AbilityConfiguration](#class-abilityconfiguration)|是|-|表示需要更新的配置信息。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

// BaseAbility是顶层基类，不支持开发者直接继承。故以派生类Ability举例说明。
class MainAbility <: UIAbility {
    public override func onConfigurationUpdate(newConfig: AbilityConfiguration) {
        AppLog.info(newConfig.language)
    }
}
```

### func onMemoryLevel(MemoryLevel)

```cangjie
public open func onMemoryLevel(level: MemoryLevel): Unit
```

**功能：** 当内存到达不同级别时系统回调该方法。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|level|[MemoryLevel](#enum-memorylevel)|是|-|当前内存使用级别。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.AppLog
import kit.AbilityKit.*

// BaseAbility是顶层基类，不支持开发者直接继承。故以派生类Ability举例说明。
class MainAbility <: UIAbility {
    public override func onMemoryLevel(level: MemoryLevel) {
        AppLog.info("onMemoryLevel")
    }
}
```