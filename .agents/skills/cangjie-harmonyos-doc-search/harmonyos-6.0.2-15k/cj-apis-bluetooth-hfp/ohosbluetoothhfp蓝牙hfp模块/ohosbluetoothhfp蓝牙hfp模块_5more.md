# ohos.bluetooth.hfp（蓝牙hfp模块）

hfp模块提供了访问蓝牙呼叫接口的方法。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 权限列表

ohos.permission.ACCESS_BLUETOOTH

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createHfpAgProfile()

```cangjie
public func createHfpAgProfile(): HandsFreeAudioGatewayProfile
```

**功能：** 创建hfp profile实例。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[HandsFreeAudioGatewayProfile](#class-handsfreeaudiogatewayprofile)|返回该profile的实例。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

try {
    let hdfProfile = createHfpAgProfile()
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```