# ohos.thermal（热管理）

本模块提供热管理相关的接口，包括热档位查询及注册回调等功能。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getLevel()

```cangjie
public func getLevel(): ThermalLevel
```

**功能：** 获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[ThermalLevel](#enum-thermallevel)|热档位信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*

let level: ThermalLevel = getLevel()
```

## func registerThermalLevelCallback(Callback1Argument\<ThermalLevel>)

```cangjie
public func registerThermalLevelCallback(callback: Callback1Argument<ThermalLevel>): Unit
```

**功能：** 订阅热档位变化时的回调提醒。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[ThermalLevel](#enum-thermallevel)>|是|-|回调函数，返回变化后的热档位。|

## func unregisterThermalLevelCallback(?Callback0Argument)

```cangjie
public func unregisterThermalLevelCallback(callback!: ?Callback0Argument = None): Unit
```

**功能：** 取消订阅热档位变化时的回调提醒。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|?[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|否|None| **命名参数。** 回调函数，取消已注册的回调函数成功后将执行的回调函数。|