## class DataBlob

```cangjie
public class DataBlob {
    public var data: Array<UInt8>
    public init(data: Array<UInt8>)
}
```

**功能：** buffer数组，提供blob数据类型。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 22

### var data

```cangjie
public var data: Array<UInt8>
```

**功能：** 数据。

**类型：** Array\<UInt8>

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 22

### init(Array\<UInt8>)

```cangjie
public init(data: Array<UInt8>)
```

**功能：** 创建DataBlob对象。

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<UInt8>|是|-|存储的数组。|