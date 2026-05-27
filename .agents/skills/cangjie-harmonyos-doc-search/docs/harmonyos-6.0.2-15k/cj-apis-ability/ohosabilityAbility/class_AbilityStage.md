## class AbilityStage

```cangjie
public open class AbilityStage {}
```

**功能：** AbilityStage类提供在HAP加载的时候，通知开发者，可以在此进行该HAP的初始化（如资源预加载，线程创建等）能力。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### prop context

```cangjie
public prop context: AbilityStageContext
```

**类型：** [AbilityStageContext](#class-abilitystagecontext)

**读写能力：** 只读

**起始版本：** 12

### static func registerCreator(String, () -> AbilityStage)

```cangjie
public static func registerCreator(moduleName: String, creator: () -> AbilityStage): Unit
```

**功能：** 注册[AbilityStage](#class-abilitystage)的对应的creator。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

| 参数名  | 类型   | 必填 | 说明 |
| :------ | :---- | :--- | :-- |
| moduleName | String | 是 | 注册AbilityStage的名称。 |
| creator | () -> [AbilityStage](#class-abilitystage) | 是 |  注册AbilityStage的对应的 creator。 |

### func onAcceptWant(Want)

```cangjie
public open func onAcceptWant(want: Want): String
```

**功能：** 启动一个specified类型的ability时触发的事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

| 参数名  | 类型   | 必填 | 说明 |
| :------- | :------ | :---- | :---- |
| want | [Want](#class-want) | 是 | Want类型参数，传入需要启动的ability的信息，如Ability名称，Bundle名称等。 |

**返回值：**

| 类型                                                         | 说明                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| String | 返回一个ability标识，如果之前启动过标识的ability，不创建新的实例并拉回栈顶，否则创建新的实例并启动。 |

### func onConfigurationUpdate(AbilityConfiguration)

```cangjie
public open func onConfigurationUpdate(newConfig: AbilityConfiguration): Unit
```

**功能：** 环境变化通知接口，发生全局配置变更时回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

| 参数名  | 类型   | 必填 | 说明 |
| :------- | :------ | :---- | :---- |
| newConfig | [AbilityConfiguration](#class-abilityconfiguration) | 是 | 发生全局配置变更时触发回调，当前全局配置包括系统语言、深浅色模式等。 |

### func onCreate()

```cangjie
public open func onCreate(): Unit
```

**功能：** [AbilityStage](#class-abilitystage)创建时回调，执行初始化业务逻辑操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func onDestroy()

```cangjie
public open func onDestroy(): Unit
```

**功能：** 当应用销毁时调用, 此方法将在正常的调度生命周期中调用, 当应用程序异常退出或被终止时，将不会调用此方法。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### func onMemoryLevel(MemoryLevel)

```cangjie
public open func onMemoryLevel(level: MemoryLevel): Unit
```

**功能：** 当内存到达不同级别时系统回调该方法。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|level|[MemoryLevel](#enum-memorylevel)|是|-|当前内存使用级别。|