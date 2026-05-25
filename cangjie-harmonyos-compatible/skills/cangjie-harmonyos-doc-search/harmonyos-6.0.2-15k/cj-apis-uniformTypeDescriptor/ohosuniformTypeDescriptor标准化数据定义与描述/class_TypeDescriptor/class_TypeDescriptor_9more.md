## class TypeDescriptor

```cangjie
public class TypeDescriptor {}
```

**功能：** 标准化数据类型的描述类，它包含了一些属性和方法，用于描述标准化数据类型自身，以及和其他标准化数据类型之间的归属与层级关系。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

### prop belongingToTypes

```cangjie
public prop belongingToTypes: Array<String>
```

**功能：** 标准化数据类型所归属的类型typeId列表。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### prop description

```cangjie
public prop description: String
```

**功能：** 标准化数据类型的简要说明。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop filenameExtensions

```cangjie
public prop filenameExtensions: Array<String>
```

**功能：** 标准化数据类型所关联的文件名后缀列表。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### prop iconFile

```cangjie
public prop iconFile: String
```

**功能：** 标准化数据类型的默认图标文件路径，可能为空字符串（即没有默认图标），应用可以自行决定是否使用该默认图标。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop mimeTypes

```cangjie
public prop mimeTypes: Array<String>
```

**功能：** 标准化数据类型所关联的多用途互联网邮件扩展类型列表。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### prop referenceURL

```cangjie
public prop referenceURL: String
```

**功能：** 标准化数据类型的参考链接URL，用于描述类型的详细信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### prop typeId

```cangjie
public prop typeId: String
```

**功能：** 标准化数据类型的ID（即[UniformDataType](#enum-uniformdatatype)中对应的枚举值）。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func belongsTo(String)

```cangjie
public func belongsTo(utype: String): Bool
```

**功能：** 判断当前标准化数据类型是否归属于指定的标准化数据类型。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|utype|String|是|-|所指定的标准化数据类型（即[UniformDataType](#enum-uniformdatatype)中对应的枚举值）。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示当前的标准化数据类型归属于所指定的标准化数据类型，包括所指定类型与当前类型相同的情况；返回false则表示无归属关系。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let typeObj : TypeDescriptor = getTypeDescriptor(UniformDataType.PHOTOSHOP_IMAGE.get())
let belongs1 = typeObj.belongsTo(UniformDataType.PLAIN_TEXT.get())
let belongs2 = typeObj.belongsTo(UniformDataType.IMAGE.get())
if(!belongs1){
    AppLog.info("type com.adobe.photoshop-image not belongs to type general.plain-text")
}
if(!belongs2){
    AppLog.info("type com.adobe.photoshop-image belongs to type general.image")
}
```