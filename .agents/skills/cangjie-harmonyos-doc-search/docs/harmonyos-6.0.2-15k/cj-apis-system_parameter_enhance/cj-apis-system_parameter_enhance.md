# ohos.system_parameter_enhance（系统参数）

系统参数（SystemParameter）是为各系统服务提供的简单易用的键值对访问接口，各个系统服务可以定义系统参数来描述该服务的状态信息，或者通过系统参数来改变系统服务的行为。其基本操作原语为get和set，通过get可以查询系统参数的值，通过set可以修改系统参数的值。

## 导入模块

```cangjie
import kit.BasicServicesKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## class Systemparameter

```cangjie
public class Systemparameter {}
```

**功能：** 系统参数实例。

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 12

### static func get(String, String)

```cangjie
public static func get(key: String, def!: String = ""): String
```

**功能：** 获取系统参数Key对应的值。

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|待查询的系统参数key。|
|def|String|否|""| **命名参数。** def为所要获取的系统参数的默认值。def为可选参数，仅当系统参数不存在时生效。|

**返回值：**

|类型|说明|
|:----|:----|
|String|系统参数值，若key存在，返回设定的值。若key不存在且def有效，返回def；若未指定def，将抛出异常。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[系统参数错误码](../../errorcodes/cj-errorcode-system-parameter.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |14700101|System parameter can not be found.|
  |14700103|System permission operation permission denied.|
  |14700104|System internal error including out of memory, deadlock etc.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let value = Systemparameter.get("const.product.name")
AppLog.info("get product name: ${value}")
```

### static func set(String, String)

```cangjie
public static func set(key: String, value: String): Unit
```

**功能：** 设置系统参数Key对应的值。

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|String|是|-|待设置的系统参数Key。|
|value|String|是|-|待设置的系统参数值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[系统参数错误码](../../errorcodes/cj-errorcode-system-parameter.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |14700102|System parameter value is invalid.|
  |14700103|System permission operation permission denied.|
  |14700104|System internal error including out of memory, deadlock etc.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

Systemparameter.set("param.key.test", "testtest")
let value = Systemparameter.get("param.key.test")
AppLog.info("get test: ${value}")
```
