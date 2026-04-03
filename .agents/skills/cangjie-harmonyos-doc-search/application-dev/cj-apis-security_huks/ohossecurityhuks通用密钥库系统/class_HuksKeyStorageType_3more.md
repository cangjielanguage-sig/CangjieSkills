## class HuksKeyStorageType

```cangjie
public class HuksKeyStorageType {
    public static const HUKS_STORAGE_ONLY_USED_IN_HUKS: UInt32 = 2
    public static const HUKS_STORAGE_KEY_EXPORT_ALLOWED: UInt32 = 3
}
```

**功能：** 表示密钥存储方式。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_STORAGE_KEY_EXPORT_ALLOWED

```cangjie
public static const HUKS_STORAGE_KEY_EXPORT_ALLOWED: UInt32 = 3
```

**功能：** 表示主密钥派生的密钥直接导出给业务方，HUKS不对其进行托管服务。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### static const HUKS_STORAGE_ONLY_USED_IN_HUKS

```cangjie
public static const HUKS_STORAGE_ONLY_USED_IN_HUKS: UInt32 = 2
```

**功能：** 表示主密钥派生的密钥存储于huks中，由HUKS进行托管。

**类型：** UInt32

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

## class HuksOptions

```cangjie
public class HuksOptions {
    public var properties: Array<HuksParam>
    public var inData: Bytes

    public init(properties!: Array<HuksParam> = Array<HuksParam>(), inData!: Bytes =  Bytes<UInt8>())
}
```

**功能：** 调用接口使用的options。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### var inData

```cangjie
public var inData: Bytes
```

**功能：** 输入数据。

**类型：** Bytes

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### var properties

```cangjie
public var properties: Array<HuksParam>
```

**功能：** 属性，用于存HuksParam的数组。

**类型：** Array\<[HuksParam](#class-huksparam)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### init(Array\<HuksParam>, Bytes)

```cangjie
public init(properties!: Array<HuksParam> = Array<HuksParam>(), inData!: Bytes = Bytes())
```

**功能：** 构造调用接口使用的options实例。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|properties|Array\<[HuksParam](#class-huksparam)>|否|Array\<HuksParam>()|**命名参数。** 属性，用于存HuksParam的数组。默认为空。|
|inData|Bytes|否|Bytes()|**命名参数。** 输入数据。默认为空。|

## class HuksParam

```cangjie
public class HuksParam {
    public var tag: UInt32
    public var value: HuksParamValue

    public init(tag: UInt32, value: HuksParamValue)
}
```

**功能：** 调用接口使用的options中的properties数组中的param。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### var tag

```cangjie
public var tag: UInt32
```

**功能：** 标签。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### var value

```cangjie
public var value: HuksParamValue
```

**功能：** 标签对应值。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

### init(UInt32, HuksParamValue)

```cangjie
public init(tag: UInt32, value: HuksParamValue)
```

**功能：** 构造[HuksOptions](#class-huksoptions)中properties数组中的元素实例。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tag|UInt32|是|-|标签。|
|value|[HuksParamValue](#enum-huksparamvalue)|是|-|标签对应值。|