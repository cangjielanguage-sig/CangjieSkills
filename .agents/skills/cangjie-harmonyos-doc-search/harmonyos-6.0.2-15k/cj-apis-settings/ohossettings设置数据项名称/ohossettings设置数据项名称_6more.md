# ohos.settings（设置数据项名称）

本模块提供访问设置数据项的能力。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getUriSync\<T>(T) where T <: ToString

```cangjie
public func getUriSync<T>(name: T): String where T <: ToString
```

**功能：** 获取数据项的URI。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|T|是|-|类型T需实现ToString接口。数据项的名称。数据项名称分为以下两种：<br>- 上述任意一个数据库中已存在的数据项。<br>- 开发者自行添加的数据项。|

**返回值：**

|类型|说明|
|:----|:----|
|String|数据项的URI。|

## func getUriSync\<T, P>(T, P) where T <: ToStringP <: ToString

```cangjie
public func getUriSync<T, P>(name: T, domainName: P): String where T <: ToString, P <: ToString
```

**功能：** 获取数据项的URI。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|T|是|-|类型T需实现ToString 接口。数据项的名称。数据项名称分为以下两种：<br>- 上述任意一个数据库中已存在的数据项。<br>- 开发者自行添加的数据项。 |
|domainName|P|是|-|类型P需实现ToString 接口。指定要设置的域名<br> - domainName为DomainName.DEVICE_SHARED，<br>&nbsp;&nbsp;&nbsp;表示设备属性共享域。<br>- domainName为DomainName.USER_PROPRERTY，<br>&nbsp;&nbsp;&nbsp;表示为用户属性域。  |

**返回值：**

|类型|说明|
|:----|:----|
|String|数据项的URI。|

## func getValue\<T>(StageContext, T, String) where T <: ToString

```cangjie
public func getValue<T>(context: StageContext, name: T, defValue: String): String where T <: ToString
```

**功能：** 获取数据项的值。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|应用上下文。context的获取方式请参见[getStageContext](../AbilityKit/cj-apis-ability.md#func-getstagecontextabilitycontext)。|
|name|T|是|-|类型T需实现ToString接口。数据项的名称。数据项名称分为以下两种：<br>- 上述任意一个数据库中已存在的数据项。<br>- 开发者自行添加的数据项。|
|defValue|String|是|-|默认值。由开发者设置，当未从数据库中查询到该数据时，表示返回该默认值。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回数据项的值。 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.ability.getStageContext

let ret = getValue(getStageContext(Global.getAbilityContext()), Display.SCREEN_BRIGHTNESS_STATUS, "50") // 需获取Context应用上下文，详见本文使用说明
```