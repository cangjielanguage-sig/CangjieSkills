### func getTypes()

```cangjie
public func getTypes(): Array<String>
```

**功能：** 获取当前统一数据对象所有数据记录的类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>| [UniformDataType](cj-apis-uniformTypeDescriptor.md#enum-UniformDataType)类型的数组，表示当前统一数据对象所有数据记录对应的数据类型。 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType.AUDIO.get()
let value = UnifiedDataChannelValueType.INTEGER64(7)
let uniRecord = UnifiedRecord(datatype, value)
let uniData = UnifiedData(uniRecord)
let datatype1 = UniformDataType.OPENTYPE_FONT.get()
let value1 = UnifiedDataChannelValueType.BOOLEAN(true)
let uniRecord1 = UnifiedRecord(datatype1, value1)
uniData.addRecord(uniRecord1)
let types = uniData.getTypes()
let type0 = types[0]
let type1 = types[1]
```

### func hasType(String)

```cangjie
public func hasType(utype: String): Bool
```

**功能：** 检查当前统一数据对象中是否有指定的数据类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|utype|String|是|-|要查询的数据类型，见[UniformDataType](cj-apis-uniformTypeDescriptor.md#enum-UniformDataType)。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|有指定的数据类型返回true，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType
    .JAVA_SOURCE
    .get()
let value = UnifiedDataChannelValueType.INTEGER64(7)
let uniRecord = UnifiedRecord(datatype, value)
let uniData = UnifiedData(uniRecord)
let datatype1 = UniformDataType
    .AI_IMAGE
    .get()
let value1 = UnifiedDataChannelValueType.BOOLEAN(true)
let uniRecord1 = UnifiedRecord(datatype1, value1)
uniData.addRecord(uniRecord1)
if (uniData.hasType(UniformDataType
    .JAVA_SOURCE
    .get())) {
    AppLog.info("This UnifiedData has type ${UniformDataType.JAVA_SOURCE.get()}")
}

if (uniData.hasType(UniformDataType
    .AI_IMAGE
    .get())) {
    AppLog.info("This UnifiedData has type ${UniformDataType.AI_IMAGE.get()}")
}

if (!uniData.hasType(UniformDataType
    .AU_AUDIO
    .get())) {
    AppLog.info("This UnifiedData has not type ${UniformDataType.AU_AUDIO.get()}")
}
```