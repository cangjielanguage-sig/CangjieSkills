## class HuksOptions

```cangjie
public class HuksOptions {
    public HuksOptions(
        public var properties: Option<Array<HuksParam>>,
        public var inData: Option<Array<UInt8>>
    )
    public static let NONE = HuksOptions(None, None)
}
```

**功能：** 调用接口使用的options。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### static let NONE

```cangjie
public static let NONE = HuksOptions(None, None)
```

**功能：** 获取一个空的HuksOptions。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksOptions](#class-huksoptions)

**起始版本：** 15

### var inData

```cangjie
public var inData: Option<Array<UInt8>>
```

**功能：** 输入数据。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Option\<Array\<UInt8>>

**读写能力：** 可读写

**起始版本：** 15

### var properties

```cangjie
public var properties: Option<Array<HuksParam>>
```

**功能：** 属性，用于存HuksParam的数组。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** Option\<Array\<[HuksParam](#class-huksparam)>>

**读写能力：** 可读写

**起始版本：** 15

### HuksOptions(Option\<Array\<HuksParam>>, Option\<Array\<UInt8>>)

```cangjie
public HuksOptions(
    public var properties: Option<Array<HuksParam>>,
    public var inData: Option<Array<UInt8>>
)
```

**功能：** 构造调用接口使用的options实例。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|inData|Option\<Array\<UInt8>>|是|输入数据。|
|properties|Option\<Array\<[HuksParam](#class-huksparam)>>|是|属性，用于存HuksParam的数组。|

## class HuksParam

```cangjie
public class HuksParam {
    public HuksParam(
        public let tag: HuksTag,
        public let value: HuksParamValue
    )
}
```

**功能：** [HuksOptions](#class-huksoptions)中properties数组中的元素。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

### let tag

```cangjie
public let tag: HuksTag
```

**功能：** 标签。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksTag](#enum-hukstag)

**读写能力：** 只读

**起始版本：** 15

### let value

```cangjie
public let value: HuksParamValue
```

**功能：** 标签对应值。

**系统能力：** SystemCapability.Security.Huks.Core

**类型：** [HuksParamValue](#enum-huksparamvalue)

**读写能力：** 只读

**起始版本：** 15

### HuksParam(HuksTag, HuksParamValue)

```cangjie
public HuksParam(
    public let tag: HuksTag,
    public let value: HuksParamValue
)
```

**功能：** 构造[HuksOptions](#class-huksoptions)中properties数组中的元素实例。

**系统能力：** SystemCapability.Security.Huks.Core

**起始版本：** 15

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|tag|[HuksTag](#enum-hukstag)|是|标签。|
|value|[HuksParamValue](#enum-huksparamvalue)|是|标签对应值。|