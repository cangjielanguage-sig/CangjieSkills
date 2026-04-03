### init(WindowMode, Int32)

```cangjie
public init(
    windowMode!: WindowMode = WINDOW_MODE_UNDEFINED,
    displayId!: Int32 = 0
)
```

**功能：** StartOptions的构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowMode|[WindowMode](#enum-windowmode)|否|WINDOW_MODE_UNDEFINED| **命名参数。** 启动Ability时的窗口模式。|
|displayId|Int32|否|0| **命名参数。** 屏幕ID模式。默认是0，表示当前屏幕。|
|withAnimation|Bool|否|true| **命名参数。** Ability是否具有动画效果。|
|windowLeft|Int32|否|0| **命名参数。** 窗口左边的位置。|
|windowTop|Int32|否|0| **命名参数。** 窗口顶部的位置。|
|windowWidth|Int32|否|0| **命名参数。** 窗口的宽度。|
|windowHeight|Int32|否|0| **命名参数。** 窗口的高度。|
|processMode|?[ProcessMode](#enum-processmode)|否|None| **命名参数。** 进程模式。<br>1.仅在平板类设备上生效。<br>2.仅在[UIAbilityContext.startAbility](#func-startabilitywant-startoptions)中生效。|
|startupVisibility|?[StartupVisibility](#enum-startupvisibility)|否|None| **命名参数。** Ability启动后的可见性。<br>1.仅在平板类设备上生效。<br>2.仅在[UIAbilityContext.startAbility](#func-startabilitywant-startoptions)中生效。|