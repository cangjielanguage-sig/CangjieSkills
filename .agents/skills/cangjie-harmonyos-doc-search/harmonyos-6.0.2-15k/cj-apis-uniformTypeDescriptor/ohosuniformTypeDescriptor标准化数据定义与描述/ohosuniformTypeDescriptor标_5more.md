# ohos.uniformTypeDescriptor（标准化数据定义与描述）

本模块对标准化数据类型进行了抽象定义与描述。

## 导入模块

```cangjie
import kit.ArkData.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getTypeDescriptor(String)

```cangjie
public func getTypeDescriptor(typeId: String): TypeDescriptor
```

**功能：** 按给定的标准化数据类型ID查询并返回对应的标准化数据类型描述类对象。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|typeId|String|是|-|标准化数据类型ID。|

**返回值：**

|类型|说明|
|:----|:----|
|[TypeDescriptor](#class-typedescriptor)|返回标准化数据类型描述类对象，如果要查询的标准化数据类型不存在则返回null。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let typeObj: TypeDescriptor = getTypeDescriptor(UniformDataType.PHOTOSHOP_IMAGE.get())
```

## func getUniformDataTypeByFilenameExtension(String, String)

```cangjie
public func getUniformDataTypeByFilenameExtension(filenameExtension: String, belongsTo!: String = ""): String
```

**功能：** 根据给定的文件后缀名和所归属的标准化数据类型,查询标准化数据类型的ID。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|filenameExtension|String|是|-|文件后缀名称。|
|belongsTo|String|否|""| **命名参数。** 要查询的标准化数据类型所归属类型ID，若不传入此参数则只按照文件后缀名称查询标准化数据类型ID。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回与给定文件后缀名以及归属类型ID（如果设置了belongsTo参数）匹配的标准化数据类型ID，如果要查询的标准化数据类型不存在则返回根据入参按指定规则生成的动态类型。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let typeObj: TypeDescriptor = getTypeDescriptor(UniformDataType.PHOTOSHOP_IMAGE.get())
```