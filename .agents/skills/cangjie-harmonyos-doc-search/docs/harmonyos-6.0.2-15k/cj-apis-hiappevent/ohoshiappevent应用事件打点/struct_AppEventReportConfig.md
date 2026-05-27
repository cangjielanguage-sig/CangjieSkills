## struct AppEventReportConfig

```cangjie
public struct AppEventReportConfig {
    public let domain: String
    public let name: String
    public let isRealTime: Bool
    public init(domain!: String = "", name!: String = "", isRealTime!: Bool = false)
}
```

**功能：** 数据处理者可以上报事件的描述配置。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### let domain

```cangjie
public let domain: String
```

**功能：** 事件领域。事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let isRealTime

```cangjie
public let isRealTime: Bool
```

**功能：** 是否实时上报事件。配置值为true表示实时上报事件，false表示不实时上报事件。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 事件名称。首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### init(String, String, Bool)

```cangjie
public init(domain!: String = "", name!: String = "", isRealTime!: Bool = false)
```

**功能：** 创建[AppEventReportConfig](#struct-appeventreportconfig)实例。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|domain|String|否|""| **命名参数。** 事件领域。事件领域名称支持数字、字母、下划线字符，需要以字母开头且不能以下划线结尾，长度非空且不超过32个字符。|
|name|String|否|""| **命名参数。** 事件名称。首字符必须为字母字符或$字符，中间字符必须为数字字符、字母字符或下划线字符，结尾字符必须为数字字符或字母字符，长度非空且不超过48个字符。|
|isRealTime|Bool|否|false| **命名参数。** 是否实时上报事件。配置值为true表示实时上报事件，false表示不实时上报事件。|