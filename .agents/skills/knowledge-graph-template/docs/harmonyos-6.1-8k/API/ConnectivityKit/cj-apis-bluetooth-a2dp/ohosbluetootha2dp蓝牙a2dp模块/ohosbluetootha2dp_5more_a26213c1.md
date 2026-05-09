# ohos.bluetooth.a2dp（蓝牙a2dp模块）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

a2dp模块提供了访问蓝牙音频接口的方法。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 权限列表

ohos.permission.ACCESS_BLUETOOTH

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](./../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func createA2dpSrcProfile()

```cangjie
public func createA2dpSrcProfile(): A2dpSourceProfile
```

**功能：** 创建蓝牙媒体[A2DP Source](#class-a2dpsourceprofile)实例。通过该实例可使用本端作为A2DP Source设备的方法，如：获取和其他设备间的蓝牙媒体音频播放状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[A2dpSourceProfile](#class-a2dpsourceprofile)|返回该profile的实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.*

try {
    let a2dpProfile = createA2dpSrcProfile()
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```