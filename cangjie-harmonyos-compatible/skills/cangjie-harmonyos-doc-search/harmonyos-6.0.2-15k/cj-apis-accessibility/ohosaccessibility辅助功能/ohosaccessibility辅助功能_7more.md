# ohos.accessibility（辅助功能）

本模块提供辅助功能查询能力，包括获取辅助应用列表、辅助应用启用状态、无障碍字幕配置、发送无障碍事件等。

## 导入模块

```cangjie
import kit.AccessibilityKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getAccessibilityExtensionList(AbilityType, AbilityState)

```cangjie
public func getAccessibilityExtensionList(abilityType: AbilityType, stateType: AbilityState): Array<AccessibilityAbilityInfo>
```

**功能：** 查询辅助应用列表。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityType|[AbilityType](#enum-abilitytype)|是|-|辅助应用的类型。|
|stateType|[AbilityState](#enum-abilitystate)|是|-|辅助应用的状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[AccessibilityAbilityInfo](#class-accessibilityabilityinfo)>|返回辅助应用信息列表。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AccessibilityKit.*
import ohos.base.*

try {
    let arrAccessibilityAbilityInfo = getAccessibilityExtensionList(
        AbilityType.ABILITYTYPE_AUDIBLE, AbilityState.ABILITYSTATE_ENABLE)
    AppLog.info("isOpenAccessibility: ${arrAccessibilityAbilityInfo.size}")
} catch (e: Exception) {
    AppLog.error("isOpenAccessibility: ${e.toString()}")
}
```

## func isOpenAccessibility()

```cangjie
public func isOpenAccessibility(): Bool
```

**功能：** 是否启用了辅助功能。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|启用辅助功能返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AccessibilityKit.*
import ohos.base.*

try {
    let isOpen: Bool = isOpenAccessibility()
    AppLog.info("isOpenAccessibility: ${isOpen}")
} catch (e: Exception) {
    AppLog.error("isOpenAccessibility: ${e.toString()}")
}
```

## func isOpenTouchGuide()

```cangjie
public func isOpenTouchGuide(): Bool
```

**功能：** 是否开启了触摸浏览模式。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|启用辅助功能返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AccessibilityKit.*
import ohos.base.*

try {
    let isOpen: Bool = isOpenTouchGuide()
    AppLog.info("isOpenTouchGuide: ${isOpen}")
} catch (e: Exception) {
    AppLog.error("isOpenTouchGuide: ${e.toString()}")
}
```

## func isScreenReaderOpen()

```cangjie
public func isScreenReaderOpen(): Bool
```

**功能：** 是否开启了屏幕朗读模式。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|启用屏幕朗读返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AccessibilityKit.*
import ohos.base.*

try {
    let isOpen: Bool = isScreenReaderOpen()
    AppLog.info("isScreenReaderOpen: ${isOpen}")
} catch (e: Exception) {
    AppLog.error("isScreenReaderOpen: ${e.toString()}")
}
```