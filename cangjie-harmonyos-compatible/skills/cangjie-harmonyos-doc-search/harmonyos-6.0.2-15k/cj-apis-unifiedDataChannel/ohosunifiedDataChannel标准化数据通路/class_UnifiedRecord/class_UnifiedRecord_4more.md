## class UnifiedRecord

```cangjie
public open class UnifiedRecord {
    public init()
    public init(dtype: String, value: UnifiedDataChannelValueType)
}
```

**功能：** 对UDMF支持的数据内容的抽象定义，称为数据记录。一个统一数据对象内包含一条或多条数据记录，例如一条文本记录、一条图片记录、一条HTML记录等。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 用于创建数据记录。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let uniRecord = UnifiedRecord()
```

### init(String, UnifiedDataChannelValueType)

```cangjie
public init(dtype: String, value: UnifiedDataChannelValueType)
```

**功能：** 用于创建指定类型和值的数据记录。

- 当参数value为image.PixelMap类型时，参数dtype必须为[UniformDataType.OPENHARMONY_PIXEL_MAP](cj-apis-uniformTypeDescriptor.md#openharmony_pixel_map)的值;
- 当参数value为Want类型时，参数dtype必须为[UniformDataType.OPENHARMONY_WANT](cj-apis-uniformTypeDescriptor.md#openharmony_want)的值。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|dtype|String|是|-|要创建的数据记录的类型。|
|value|[UnifiedDataChannelValueType](#enum-unifieddatachannelvaluetype)|是|-|要创建的数据记录的值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType.OPENHARMONY_STYLED_STRING.get()
let value = UnifiedDataChannelValueType.STRING("value")
let uniRecordWith = UnifiedRecord(datatype, value)
```

### func getType()

```cangjie
public func getType(): String
```

**功能：** 获取当前数据记录的类型。由于从统一数据对象中调用[getRecords](#func-getrecords)所取出的数据是UnifiedRecord对象，因此需要通过本接口查询此记录的具体类型，再将该UnifiedRecord对象转换为其子类，调用子类接口。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前数据记录对应的具体数据类型，见[UniformDataType](cj-apis-uniformTypeDescriptor.md#enum-UniformDataType)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType.OPENHARMONY_STYLED_STRING.get()
let value = UnifiedDataChannelValueType.STRING("value")
let uniRecordWith = UnifiedRecord(datatype, value)
let type_get = uniRecordWith.getType()
```