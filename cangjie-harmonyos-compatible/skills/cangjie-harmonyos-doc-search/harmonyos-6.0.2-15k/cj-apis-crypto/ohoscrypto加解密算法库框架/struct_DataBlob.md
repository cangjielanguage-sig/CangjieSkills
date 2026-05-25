## struct DataBlob

```cangjie
public struct DataBlob {
    public DataBlob(
        public let data: Array<UInt8>)
}
```

**功能：** 存储数组的数据类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

### let data

```cangjie
public let data: Array<UInt8>
```

**功能：** 数据。

**系统能力：** SystemCapability.Security.CryptoFramework

**类型：** Array\<UInt8>

**读写能力：** 只读

**起始版本：** 12

### DataBlob(Array\<UInt8>)

```cangjie
public DataBlob(
    public let data: Array<UInt8>)
```

**功能：** 创建DataBlob实例。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<UInt8>|是|-|数据。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CryptoArchitectureKit.*

let blob = DataBlob("test".toArray())
```