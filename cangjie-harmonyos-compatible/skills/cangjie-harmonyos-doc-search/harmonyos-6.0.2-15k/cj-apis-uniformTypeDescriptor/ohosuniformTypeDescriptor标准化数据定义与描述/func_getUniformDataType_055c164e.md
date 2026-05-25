## func getUniformDataTypeByMIMEType(String, String)

```cangjie
public func getUniformDataTypeByMIMEType(mimeType: String, belongsTo!: String = ""): String
```

**功能：** 根据给定的MIME类型和所归属的标准化数据类型查询标准化数据类型的ID。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeType|String|是|-|MIME类型名称。|
|belongsTo|String|否|""| **命名参数。** 要查询的标准化数据类型所归属类型ID。若不传入此参数则只按照MIME类型名称查询标准化数据类型ID。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回与MIME类型名称以及归属类型ID（如果设置了belongsTo参数）匹配的标准化数据类型ID，如果要查询的标准化数据类型不存在则返回根据入参按指定规则生成的动态类型。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let typeMId = getUniformDataTypeByMIMEType("image/jpeg", belongsTo: "general.image")
let typeId = getUniformDataTypeByMIMEType("image/jpeg")
```