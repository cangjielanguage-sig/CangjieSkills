## func unregisterKeyObserver\<T, P>(StageContext, T, P) where T <: ToStringP <: ToString

```cangjie
public func unregisterKeyObserver<T, P>(context: StageContext, name: T, domainName: P): Bool where T <: ToString, P <: ToString
```

**功能：** 进行注销指定域名下对指定键的监视器。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用上下文。context的获取方式请参见[getStageContext](../AbilityKit/cj-apis-ability.md#func-getstagecontextabilitycontext)。|
|name|T|是|-|类型T需实现ToString接口。数据项的名称。数据项名称分为以下两种：<br> - 上述任意一个数据库中已存在的数据项。<br>- 开发者自行添加的数据项。 |
|domainName|P|是|-|类型P需实现ToString接口。指定要设置的域名<br> - domainName为DomainName.DEVICE_SHARED，<br>&nbsp;&nbsp;&nbsp;表示设备属性共享域。<br>- domainName为DomainName.USER_PROPRERTY，<br>&nbsp;&nbsp;&nbsp;表示为用户属性域。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回取消数据项的观察者是否成功的结果，true表示设置成功，false表示设置失败。 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.ability.*

let ret = unregisterKeyObserver(getStageContext(Global.getAbilityContext()), Display.SCREEN_BRIGHTNESS_STATUS,
    DomainName.USER_PROPERTY) // 需获取Context应用上下文，详见本文使用说明
```

## class DisplayAutoScreenBrightnessMode

```cangjie
public class DisplayAutoScreenBrightnessMode {
    public static let AUTO_SCREEN_BRIGHTNESS_MODE: String = "1"
    public static let MANUAL_SCREEN_BRIGHTNESS_MODE: String = "0"
}
```

**功能：** 设置显示效果。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### static let AUTO_SCREEN_BRIGHTNESS_MODE

```cangjie
public static let AUTO_SCREEN_BRIGHTNESS_MODE: String = "1"
```

**功能：** 使用屏幕亮度自动调整时AUTO_SCREEN_BRIGHTNESS的值。

**系统能力：** SystemCapability.Applications.Settings.Core

**类型：** String

**起始版本：** 19

### static let MANUAL_SCREEN_BRIGHTNESS_MODE

```cangjie
public static let MANUAL_SCREEN_BRIGHTNESS_MODE: String = "0"
```

**功能：** 使用屏幕亮度手动调整时的AUTO_SCREEN_BRIGHTNESS值。

**系统能力：** SystemCapability.Applications.Settings.Core

**类型：** String

**起始版本：** 19