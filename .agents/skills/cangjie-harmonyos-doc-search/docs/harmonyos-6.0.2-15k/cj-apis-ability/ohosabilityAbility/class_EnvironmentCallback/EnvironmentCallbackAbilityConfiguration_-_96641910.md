### EnvironmentCallback((AbilityConfiguration) -> Unit, (MemoryLevel) -> Unit)

```cangjie
public EnvironmentCallback(
    public let onConfigurationUpdated!: (AbilityConfiguration) -> Unit,
    public let onMemoryLevel!: (MemoryLevel) -> Unit
)
```

**功能：** EnvironmentCallback的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onConfigurationUpdated|([AbilityConfiguration](#class-abilityconfiguration))->Unit|否|-| **命名参数。** 注册系统环境变化的监听后，在系统环境变化时触发回调。|
|onMemoryLevel|([MemoryLevel](#enum-memorylevel))->Unit|否|-| **命名参数。** 注册系统环境变化的监听后，在系统内存变化时触发回调。|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.*
import kit.AbilityKit.*

var callId: Int32 = 0

class MainAbility <: UIAbility {
    public init() {
        super()
        registerSelf()
    }

    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
        let envCallback: EnvironmentCallback = EnvironmentCallback(
            onConfigurationUpdated: {
                config: AbilityConfiguration =>
                AppLog.info("envCallback onConfigurationUpdated success:")
                AppLog.info(config.language)
                match (config.colorMode) {
                    case COLOR_MODE_NOT_SET => AppLog.info("COLOR_MODE_NOT_SET")
                    case COLOR_MODE_DARK => AppLog.info("COLOR_MODE_DARK")
                    case COLOR_MODE_LIGHT => AppLog.info("COLOR_MODE_LIGHT")
                    case _ => AppLog.info("undefined colorMode!")
                }
                match (config.direction) {
                    case DIRECTION_NOT_SET => AppLog.info("DIRECTION_NOT_SET")
                    case DIRECTION_VERTICAL => AppLog.info("DIRECTION_VERTICAL")
                    case DIRECTION_HORIZONTAL => AppLog.info("DIRECTION_HORIZONTAL")
                    case _ => AppLog.info("undefined direction!")
                }
                match (config.screenDensity) {
                    case SCREEN_DENSITY_NOT_SET => AppLog.info("SCREEN_DENSITY_NOT_SET")
                    case SCREEN_DENSITY_SDPI => AppLog.info("SCREEN_DENSITY_SDPI")
                    case SCREEN_DENSITY_MDPI => AppLog.info("SCREEN_DENSITY_MDPI")
                    case SCREEN_DENSITY_LDPI => AppLog.info("SCREEN_DENSITY_LDPI")
                    case SCREEN_DENSITY_XLDPI => AppLog.info("SCREEN_DENSITY_XLDPI")
                    case SCREEN_DENSITY_XXLDPI => AppLog.info("SCREEN_DENSITY_XXLDPI")
                    case SCREEN_DENSITY_XXXLDPI => AppLog.info("SCREEN_DENSITY_XXXLDPI")
                    case _ => AppLog.info("undefined screenDensity!")
                }
                AppLog.info("${config.displayId}")
                AppLog.info("${config.hasPointerDevice}")
                AppLog.info("${config.fontSizeScale}")
                AppLog.info("${config.fontWeightScale}")
                AppLog.info("${config.mcc}")
                AppLog.info("${config.mnc}")
            },
            onMemoryLevel: {
                mem: MemoryLevel => match (mem) {
                    case MEMORY_LEVEL_MODERATE => AppLog.info("MEMORY_LEVEL_MODERATE")
                    case MEMORY_LEVEL_LOW => AppLog.info("MEMORY_LEVEL_LOW")
                    case MEMORY_LEVEL_CRITICAL => AppLog.info("MEMORY_LEVEL_CRITICAL")
                    case _ => AppLog.info("undefined MemoryLevel!")
                }
            }
        )
        let appcontext = this.context.getApplicationContext()
        callId = appcontext.on(ApplicationContextType.ENVIRONMENT, envCallback)
        AppLog.info("Register EnvironmentCallback success and id is ${callId}.")
    }

    public override func onWindowStageCreate(windowStage: WindowStage): Unit {
        AppLog.info("MainAbility onWindowStageCreate.")
        let properties = windowStage.getMainWindow().getWindowProperties()
        AppLog.info("onWindowStageCreate: ${properties.windowRect.width}")
        windowStage.loadContent("EntryView")
    }
}
```