### func getValue()

```cangjie
public func getValue(): UnifiedDataChannelValueType
```

**功能：** 获取当前数据记录的值。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[UnifiedDataChannelValueType](#enum-unifieddatachannelvaluetype)|当前数据记录对应的值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType.OPENHARMONY_STYLED_STRING.get()
let value = UnifiedDataChannelValueType.STRING("value")
let uniRecordWith = UnifiedRecord(datatype, value)
let value_get = uniRecordWith.getValue()
let message: String

match (value_get) {
    case INTEGER32(v) => message = v.toString()
    case INTEGER64(v) => message = v.toString()
    case DOUBLE(v) => message = v.toString()
    case BOOLEAN(v) => message = v.toString()
    case STRING(v) => message = v
    case ARRAYBUFFER(v) => message = v.toString()
    case PIXELMAP(v) => message = "PIXELMAP"
    case _ => throw IllegalArgumentException("The type is not supporte.")
}
```