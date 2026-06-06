### func equals(TypeDescriptor)

```cangjie
public func equals(typeDescriptor: TypeDescriptor): Bool
```

**功能：** 判断当前TypeDescriptor和指定TypeDescriptor的typeId是否相同。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|typeDescriptor|[TypeDescriptor](#class-typedescriptor)|是|-|待比较的标准化数据类型描述类对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示所比较的标准化数据类型相同；返回false则表示不同。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let typeObj1 = getTypeDescriptor(UniformDataType.TYPE_SCRIPT.get())
let typeObj2 : TypeDescriptor = getTypeDescriptor(UniformDataType.SOURCE_CODE.get())
let typeObj3 : TypeDescriptor = getTypeDescriptor('general.source-code')
if(typeObj2.equals(typeObj1)) {
    AppLog.info("typeObj1 is not equal to typeObj2")
}
if(typeObj2.equals(typeObj3)) {
    AppLog.info("typeObj2 is equal to typeObj3")
}
```

### func isHigherLevelType(String)

```cangjie
public func isHigherLevelType(utype: String): Bool
```

**功能：** 判断当前标准化数据类型是否是指定标准化数据类型的高层级类型。例如SOURCE_CODE为TYPE_SCRIPT的高层级类型，PLAIN_TEXT为SOURCE_CODE和TYPE_SCRIPT的高层级类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|utype|String|是|-|所指定的标准化数据类型（即[UniformDataType](#enum-uniformdatatype)中对应的枚举值）。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示当前的标准化数据类型是所指定标准化数据类型的高层级类型，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let typeObj : TypeDescriptor = getTypeDescriptor(UniformDataType.SOURCE_CODE.get())
let isHigherLevelType1 = typeObj.isHigherLevelType(UniformDataType.TYPE_SCRIPT.get())
if(isHigherLevelType1) {
    AppLog.info('type general.source-code is higher level type of type general.type-script')
}
let isHigherLevelType2 = typeObj.isHigherLevelType(UniformDataType.JPEG.get())
if(!isHigherLevelType2) {
    AppLog.info('type general.source-code is not higher level type of type general.jpeg')
}
```

### func isLowerLevelType(String)

```cangjie
public func isLowerLevelType(utype: String): Bool
```

**功能：** 判断当前标准化数据类型是否是指定标准化数据类型的低层级类型。例如TYPE_SCRIPT为SOURCE_CODE的低层级类型，TYPE_SCRIPT和SOURCE_CODE为PLAIN_TEXT的低层级类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|utype|String|是|-|所指定的标准化数据类型（即[UniformDataType](#enum-uniformdatatype)中对应的枚举值）。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示当前的标准化数据类型是所指定标准化数据类型的低层级类型，否则返回false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let typeObj : TypeDescriptor = getTypeDescriptor(UniformDataType.TYPE_SCRIPT.get())
let isLowerLevelType1 = typeObj.isLowerLevelType(UniformDataType.SOURCE_CODE.get())
if(isLowerLevelType1) {
    AppLog.info('type general.type-script is lower level type of type general.source-code')
}
let isLowerLevelType2 = typeObj.isLowerLevelType(UniformDataType.JPEG.get())
if(!isLowerLevelType2) {
    AppLog.info('type general.type-script is not lower level type of type general.jpeg')
}
```