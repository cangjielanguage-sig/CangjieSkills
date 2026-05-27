## class UnifiedData

```cangjie
public class UnifiedData {
    public init()
    public init(record: UnifiedRecord)
}
```

**功能：** 表示UDMF统一数据对象，提供封装一组数据记录的方法。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

### prop properties

```cangjie
public mut prop properties: UnifiedDataProperties
```

**功能：** 定义统一数据对象中所有数据记录的属性，包含时间戳、标签、粘贴范围以及一些附加数据等。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**类型：** [UnifiedDataProperties](#class-unifieddataproperties)

**起始版本：** 20

**示例：**

```cangjie
import kit.ArkData.*

let pr: UnifiedDataProperties = UnifiedDataProperties()
let ud: UnifiedData = UnifiedData()
ud.properties = pr
```

### init()

```cangjie
public init()
```

**功能：** 用于创建统一数据对象。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let unifiedData: UnifiedData = UnifiedData()
```

### init(UnifiedRecord)

```cangjie
public init(record: UnifiedRecord)
```

**功能：** 用于创建带有一条数据记录的统一数据对象。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|record|[UnifiedRecord](#class-unifiedrecord)|是|-|要添加到统一数据对象中的数据记录，该记录为UnifiedRecord或其子类对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType.OPENHARMONY_STYLED_STRING.get()
let value = UnifiedDataChannelValueType.STRING("value")
let uniRecord = UnifiedRecord(datatype, value)
let uniData = UnifiedData(uniRecord)
```

### func addRecord(UnifiedRecord)

```cangjie
public func addRecord(record: UnifiedRecord): Unit
```

**功能：** 在当前统一数据对象中添加一条数据记录。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|record|[UnifiedRecord](#class-unifiedrecord)|是|-|要添加到统一数据对象中的数据记录，该记录为UnifiedRecord子类对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType.OPENHARMONY_STYLED_STRING.get()
let value = UnifiedDataChannelValueType.STRING("value")
let uniRecord = UnifiedRecord(datatype, value)
let uniData = UnifiedData()
uniData.addRecord(uniRecord)
```

### func getRecords()

```cangjie
public func getRecords(): Array<UnifiedRecord>
```

**功能：** 将当前统一数据对象中的所有数据记录取出。通过本接口取出的数据为UnifiedRecord类型，需通过[getType](#func-gettype)获取数据类型后转为子类再使用。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[UnifiedRecord](#class-unifiedrecord)>|当前统一数据对象内所添加的记录。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let datatype = UniformDataType.OPENHARMONY_STYLED_STRING.get()
let value = UnifiedDataChannelValueType.STRING("value")
let uniRecord = UnifiedRecord(datatype, value)
let uniData = UnifiedData(uniRecord)
let datatype1 = UniformDataType.JAVA_SCRIPT.get()
let value1 = UnifiedDataChannelValueType.DOUBLE(2.2)
let uniRecord1 = UnifiedRecord(datatype1, value1)
uniData.addRecord(uniRecord1)
let records = uniData.getRecords()
let resuniRecord0 = records[0]
let resuniRecord1 = records[1]
```