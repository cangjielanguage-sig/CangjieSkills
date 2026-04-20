## class Context

```cangjie
public open class Context <: BaseContext {}
```

**功能：** Context为ability或application提供上下文支持能力，包括访问特定应用程序的资源等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**父类型：**

- [BaseContext](./cj-apis-app-ability.md#class-basecontext)

### prop applicationInfo

```cangjie
public prop applicationInfo: ApplicationInfo
```

**功能：** 当前应用程序的信息。

**类型：** [ApplicationInfo](./cj-apis-bundle_manager.md#class-applicationinfo)

**读写能力：** 只读

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility3 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let info = this.context.applicationInfo
    }
}
```

### prop area

```cangjie
public mut prop area: AreaMode
```

**功能：** 文件分区信息，按加密等级[AreaMode](./cj-apis-app-ability-context_constant.md#enum-areamode) 进行分区。

**类型：** [AreaMode](./cj-apis-app-ability-context_constant.md#enum-areamode)

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility4 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let area = this.context.area
    }
}
```

### prop filesDir

```cangjie
public prop filesDir: String
```

**功能：** 文件目录。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility5 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let filesDir = this.context.filesDir
    }
}
```

### prop resourceManager

```cangjie
public prop resourceManager: ResourceManager
```

**功能：** 资源管理对象。

**类型：** [ResourceManager](../LocalizationKit/cj-apis-resource_manager.md#class-resourcemanager)

**读写能力：** 只读

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**示例：**

<!-- compile -->
```cangjie
import kit.AbilityKit.*

class MyUIAbility6 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let resourceManager = this.context.resourceManager
    }
}
```

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉对象转换成[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|ArkTS互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)|ArkTS统一类型。|