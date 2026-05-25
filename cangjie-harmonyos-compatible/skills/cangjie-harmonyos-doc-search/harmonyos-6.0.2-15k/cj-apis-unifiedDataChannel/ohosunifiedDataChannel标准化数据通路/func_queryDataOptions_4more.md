## func queryData(Options)

```cangjie
public func queryData(options: Options): Array<UnifiedData>
```

**功能：** 查询UDMF公共数据通路的数据。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|---|---|---|---|
|options|[Options](#class-options)|是|配置项参数，key和intention均为可选，根据传入的参数做相应的校验以返回不同的值。|

**返回值：**

|类型|说明|
|----|----|
|Array\<[UnifiedData](#class-unifieddata)>|查询到的所有数据。|

**异常：**

- IllegalArgumentException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Query UnifiedData failed! Possible causes: Incorrect input parameters.|可能由传入参数不正确导致。|检查输入参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let opt = UnifiedDataChannelOptions(intention: Intention.DATA_HUB, key: "")
let res = queryData(opt)
```

## func updateData(Options, UnifiedData)

```cangjie
public func updateData(options: Options, data: UnifiedData): Unit
```

**功能：** 更新已写入UDMF的公共数据通路的数据。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|---|---|---|---|
|options|[Options](#class-options)|是|配置项参数，参数中intention字段必填；其他字段是否填写均不影响接口的使用。|
|data|[UnifiedData](#class-unifieddata)|是|目标数据。|

**异常：**

- IllegalArgumentException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |Update UnifiedData failed! Possible causes: Incorrect input parameters.|可能由传入参数不正确导致。|检查输入参数。|

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
let opt2 = UnifiedDataChannelOptions(intention: Intention.DATA_HUB, key: res)
updateData(opt2, uniData)
```

## class File

```cangjie
public open class File <: UnifiedRecord {}
```

**功能：** 是文件类型数据的基类，用于描述文件类型数据。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**父类型：**

- [UnifiedRecord](#class-unifiedrecord)

### prop details

```cangjie
public mut prop details: HashMap<String, String>
```

**功能：** 是一个字典类型对象，key和value都是String类型，用于描述文件相关信息。

**类型：** HashMap\<String, String>

**读写能力：** 可读写。

**起始版本：** 20

### prop uri

```cangjie
public mut prop uri: String
```

**功能：** 本地文件数据uri或网络文件uri。本地文件数据uri可通过[getUriFromPath](../../apis/CoreFileKit/cj-apis-file_fileuri.md#static-func-geturifrompathstring)函数获取。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20

## class HyperLink

```cangjie
public class HyperLink <: Text {}
```

**功能：** 超链接类型数据，用于描述超链接类型数据。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**父类型：**

- [Text](#class-text)

### prop description

```cangjie
public mut prop description: String
```

**功能：** 链接内容描述，默认值为空字符串。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20

### prop url

```cangjie
public mut prop url: String
```

**功能：** 链接url。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20