# ohos.distributed_device_manager（设备管理）

本模块提供分布式设备管理能力。

应用可调用接口实现如下功能：

- 注册和解除注册设备上下线变化监听
- 发现周边不可信设备
- 认证和取消认证设备
- 查询可信设备列表
- 查询本地设备信息，包括设备名称，设备类型和设备标识等

## 导入模块

```cangjie
import kit.DistributedServiceKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createDeviceManager(String)

```cangjie
public func createDeviceManager(bundleName: String): DeviceManager
```

**功能：** 创建一个设备管理实例。设备管理实例是分布式设备管理方法的调用入口。用于获取可信设备和本地设备的相关信息。

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bundleName|String|是|-|指示应用程序的Bundle名称。|

**返回值：**

|类型|说明|
|:----|:----|
|[DeviceManager](#class-devicemanager)|返回设备管理器对象实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible caused by parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*

try {
    let dm = createDeviceManager("com.example.myapplication")
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```

## func releaseDeviceManager(DeviceManager)

```cangjie
public func releaseDeviceManager(deviceManager: DeviceManager): Unit
```

**功能：** 设备管理实例不再使用后，通过该方法释放DeviceManager实例。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceManager|[DeviceManager](#class-devicemanager)|是|-|设备管理器对象实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[设备管理错误码](../../errorcodes/cj-errorcode-distributed_device_manager.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible caused by parameter verification failed.|
  |11600101|Failed to execute the function.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*

try {
    let dm = createDeviceManager("com.example.myapplication")
    releaseDeviceManager(dm)
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```