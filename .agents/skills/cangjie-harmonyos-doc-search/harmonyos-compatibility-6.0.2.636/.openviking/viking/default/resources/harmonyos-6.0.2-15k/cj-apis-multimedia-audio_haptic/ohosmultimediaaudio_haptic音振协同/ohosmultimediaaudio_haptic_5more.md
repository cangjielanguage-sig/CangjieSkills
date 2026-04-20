# ohos.multimedia.audio_haptic（音振协同）

音振协同，表示在播放声音时，可同步发起振动。可用于来电通知、消息提醒等场景。

## 导入模块

```cangjie
import kit.AudioKit.*
```

## 权限列表

ohos.permission.VIBRATE

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getAudioHapticManager()

```cangjie
public func getAudioHapticManager(): AudioHapticManager
```

**功能：** 获取音振管理器。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioHapticManager](#class-audiohapticmanager)|音振管理器。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

let audiohapticmanager = getAudioHapticManager()
```