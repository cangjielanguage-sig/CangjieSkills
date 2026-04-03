# ohos.power（系统电源管理）

该模块主要提供重启、关机、查询屏幕状态等接口。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getPowerMode()

```cangjie
public func getPowerMode(): DevicePowerMode
```

**功能：** 获取当前设备的电源模式。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[DevicePowerMode](#enum-devicepowermode)|电源模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[系统电源管理错误码](../../errorcodes/cj-errorcode-power.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |4900101|Failed to connect to the service.|

## func isActive()

```cangjie
public func isActive(): Bool
```

**功能：** 检测当前设备是否处于活动状态。有屏的设备为亮屏状态，无屏的设备为非休眠状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|处于活动状态返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[系统电源管理错误码](../../errorcodes/cj-errorcode-power.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |4900101|Failed to connect to the service. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

try {
    let ret = isActive()
    AppLog.info("test_power_isActive ret is  :${ret}")
} catch (e: Exception) {
    AppLog.error("test_power_isActive ret is :${e.message.toString()}")
}
```

## func isStandby()

```cangjie
public func isStandby(): Bool
```

**功能：** 检测当前设备是否进入待机低功耗续航模式。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|进入待机模式返回true，否则返回false。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[系统电源管理错误码](../../errorcodes/cj-errorcode-power.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |4900101|Failed to connect to the service. |

## enum DevicePowerMode

```cangjie
public enum DevicePowerMode {
    | MODE_NORMAL
    | MODE_POWER_SAVE
    | MODE_PERFORMANCE
    | MODE_EXTREME_POWER_SAVE
    | MODE_UNKNOWN
    | ...
}
```

**功能：** 表示电源模式的枚举值。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

### MODE_EXTREME_POWER_SAVE

```cangjie
MODE_EXTREME_POWER_SAVE
```

**功能：** 表示超级省电模式。

**起始版本：** 19

### MODE_NORMAL

```cangjie
MODE_NORMAL
```

**功能：** 表示标准模式，默认值。

**起始版本：** 19

### MODE_PERFORMANCE

```cangjie
MODE_PERFORMANCE
```

**功能：** 表示性能模式。

**起始版本：** 19

### MODE_POWER_SAVE

```cangjie
MODE_POWER_SAVE
```

**功能：** 表示省电模式。

**起始版本：** 19

### MODE_UNKNOWN

```cangjie
MODE_UNKNOWN
```

**功能：** 表示未知电源模式。

**起始版本：** 19

### func getValue()

```cangjie
public func getValue(): UInt32
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|枚举的值。|
