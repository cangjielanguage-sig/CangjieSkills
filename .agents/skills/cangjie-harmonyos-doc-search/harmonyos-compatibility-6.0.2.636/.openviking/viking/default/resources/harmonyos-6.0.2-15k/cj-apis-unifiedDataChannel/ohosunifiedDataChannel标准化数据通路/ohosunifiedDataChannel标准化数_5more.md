# ohos.unifiedDataChannel（标准化数据通路）

本模块为统一数据管理框架（Unified Data Management Framework,UDMF）的组成部分，针对多对多跨应用数据共享的不同业务场景，提供了标准化的数据通路，提供了标准化的数据接入与读取接口。同时对文本、图片等数据类型提供了标准化定义，方便不同应用间进行数据交互，减少数据类型适配的工作量。

## 导入模块

```cangjie
import kit.ArkData.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func deleteData(Options)

```cangjie
public func deleteData(options: Options): Array<UnifiedData>
```

**功能：** 删除UDMF公共数据通路的数据。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|---|---|---|---|
|options|[Options](#class-options)|是|配置项参数，key和intention均为可选，根据传入的参数做相应的校验以返回不同的值。|

**返回值：**

|类型|说明|
|----|----|
|Array\<[UnifiedData](#class-unifieddata)>|删除的所有数据。|

**异常：**

- IllegalArgumentException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Delete UnifiedData failed! Possible causes: Incorrect input parameters.|可能由传入参数不正确导致。|检查输入参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let opt = UnifiedDataChannelOptions(intention: Intention.DATA_HUB, key: "")
let res = deleteData(opt)
```

## func insertData(Options, UnifiedData)

```cangjie
public func insertData(options: Options, data: UnifiedData): String
```

**功能：** 将数据写入UDMF的公共数据通路中，并生成数据的唯一标识符。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|---|---|---|---|
|options|[Options](#class-options)|是|配置项参数，参数中intention字段必填；其他字段是否填写均不影响接口的使用。|
|data|[UnifiedData](#class-unifieddata)|是|目标数据。|

**返回值：**

|类型|说明|
|----|----|
|String|返回写入UDMF的数据的唯一标识符key的值。|

**异常：**

- IllegalArgumentException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Insert UnifiedData failed! Possible causes: Incorrect input parameters.|可能由传入参数不正确导致。|检查输入参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let opt = UnifiedDataChannelOptions(intention: Intention.DATA_HUB, key: "")
let uniRecord = UnifiedRecord(UniformDataType.FILE.get(), UnifiedDataChannelValueType.STRING("123"))
let uniData = UnifiedData(uniRecord)
let res = insertData(opt, uniData)
```