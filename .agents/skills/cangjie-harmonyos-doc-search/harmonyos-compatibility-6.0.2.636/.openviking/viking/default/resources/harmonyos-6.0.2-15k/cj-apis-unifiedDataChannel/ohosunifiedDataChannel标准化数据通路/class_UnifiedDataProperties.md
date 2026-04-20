## class UnifiedDataProperties

```cangjie
public class UnifiedDataProperties(
    public var extras: HashMap<String, ValueTypeEx> = HashMap<String, ValueTypeEx>()
    public var tag: String = ""
    public var timestamp: DateTime = DateTime.UnixEpoch
    public var shareOptions: ShareOptions = ShareOptions.CROSS_APP
    public var getDelayData: ?GetDelayData = None

    public init(extras!: HashMap<String, ValueTypeEx> = HashMap<String, ValueTypeEx>(), tag!: String = "",
        timestamp!: DateTime = DateTime.UnixEpoch, shareOptions!: ShareOptions = ShareOptions.CROSS_APP,
        getDelayData!: ?GetDelayData = None)
)
```

**功能：** 定义统一数据对象中所有数据记录的属性，包含时间戳、标签、粘贴范围以及一些附加数据等。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

### var extras

```cangjie
public var extras: HashMap<String, ValueTypeEx> = HashMap<String, ValueTypeEx>()
```

**功能：** 是一个HashMap类型对象，用于设置其他附加属性数据。非必填字段，默认值为空HashMap。

**类型：** HashMap\<String, ValueTypeEx>

**读写能力：** 可读写。

**起始版本：** 20

### var getDelayData

```cangjie
public var getDelayData: ?GetDelayData = None
```

**功能：** 延迟获取数据回调。当前只支持同设备剪贴板场景，后续场景待开发。非必填字段，默认值为None。

**类型：** ?[GetDelayData](#type-getdelaydata)

**读写能力：** 可读写。

**起始版本：** 20

### var shareOptions

```cangjie
public var shareOptions: ShareOptions = ShareOptions.CROSS_APP
```

**功能：** 指示[UnifiedData](#class-unifieddata)持的设备内使用范围，非必填字段，默认值为CROSS_APP。

**类型：** [ShareOptions](#enum-shareoptions)

**读写能力：** 可读写。

**起始版本：** 20

### var tag

```cangjie
public var tag: String = ""
```

**功能：** 用户自定义标签。非必填字段，默认值为空字符串。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20

### var timestamp

```cangjie
public var timestamp: DateTime = DateTime.UnixEpoch
```

**功能：** [UnifiedData](#class-unifieddata)的生成时间戳。默认值为1970年1月1日（UTC）。

**类型：** DateTime

**读写能力：** 可读写。

**起始版本：** 20

### init(HashMap<String, ValueTypeEx>, String, DateTime, ShareOptions, ?GetDelayData)

```cangjie
public init(extras!: HashMap<String, ValueTypeEx> = HashMap<String, ValueTypeEx>(), tag!: String = "",
        timestamp!: DateTime = DateTime.UnixEpoch, shareOptions!: ShareOptions = ShareOptions.CROSS_APP,
        getDelayData!: ?GetDelayData = None)
```

**功能：** UnifiedDataProperties的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|extras|HashMap\<String, [ValueTypeEx](#enum-valuetypeex)>|否|HashMap\<String, [ValueTypeEx](#enum-valuetypeex)()|用于设置其他附加属性数据。|
|tag|String|否|""|用户自定义标签。 |
|timestamp|DateTime|否|DateTime.UnixEpoch|UnifiedData的生成时间戳。|
|shareOptions|ShareOptions|否|CROSS_APP|指示UnifiedData支持的设备内使用范围。|
|getDelayData|?[GetDelayData](#type-getdelaydata)|否|None|延迟获取数据回调函数。|