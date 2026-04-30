## enum ValueTypeEx

```cangjie
public enum ValueTypeEx {
    | Integer32(Int32)
    | Integer64(Int64)
    | Double(Float64)
    | Boolean(Bool)
    | StringData(String)
    | ArrayBuffer(Array<UInt8>)
    | ...
}
```

**功能：** 用于表示[UnifiedDataProperties](#class-unifieddataproperties)的extras属性的value值。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

### ArrayBuffer(Array\<UInt8>)

```cangjie
ArrayBuffer(Array<UInt8>)
```

**功能：** 表示Array\<UInt8>的类型。

**起始版本：** 20

### Boolean(Bool)

```cangjie
Boolean(Bool)
```

**功能：** 表示Bool的类型。

**起始版本：** 20

### Double(Float64)

```cangjie
Double(Float64)
```

**功能：** 表示Float64的类型。

**起始版本：** 20

### Integer32(Int32)

```cangjie
Integer32(Int32)
```

**功能：** 表示Int32的类型。

**起始版本：** 20

### Integer64(Int64)

```cangjie
Integer64(Int64)
```

**功能：** 表示Int64的类型。

**起始版本：** 20

### StringData(String)

```cangjie
StringData(String)
```

**功能：** 表示String的类型。

**起始版本：** 20

## type GetDelayData

```cangjie
public type GetDelayData = (dtype: String) -> UnifiedData
```

**功能：**对UnifiedData的延迟封装，支持延迟获取数据。当前只支持同设备剪贴板场景，后续场景待开发。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

| 参数名 | 类型   | 必填 | 说明                 |
| :----- | :----- | :--- | :------------------- |
| dtype  | String | 是   | 作为延迟封装的标识。 |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkData.*

let getDelayData: GetDelayData = {
    dtype: String => UnifiedData()
}
```