## class CountryCode

```cangjie
public class CountryCode {
    public var country: String
    public var `type`: CountryCodeType
    public init(country: String, `type`: CountryCodeType)
}
```

**功能：** 国家码信息，包含国家码字符串和国家码的来源信息。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

### var \`type\`

```cangjie
public var `type`: CountryCodeType
```

**功能：** 表示国家码信息来源。

**类型：** [CountryCodeType](#enum-countrycodetype)

**读写能力：** 可读写

**起始版本：** 19

### var country

```cangjie
public var country: String
```

**功能：** 表示国家码字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### init(String, CountryCodeType)

```cangjie
public init(country: String, `type`: CountryCodeType)
```

**功能：** 构造CountryCode对象。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|country|String|是|-|表示国家码字符串。|
|\`type\`|[CountryCodeType](#enum-countrycodetype)|是|-|表示国家码信息来源。|