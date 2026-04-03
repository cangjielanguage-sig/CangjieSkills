### PostalAddress(String, String, String, String, String, String, String, String, String, Int32)

```cangjie
public PostalAddress(
    public var postalAddress: String,
    public var city!: String = "",
    public var country!: String = "",
    public var neighborhood!: String = "",
    public var pobox!: String = "",
    public var postcode!: String = "",
    public var region!: String = "",
    public var street!: String = "",
    public var labelName!: String = "",
    public var labelId!: Int32 = INVALID_LABEL_ID
)
```

**功能：** 创建PostalAddress实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|postalAddress|String|是|-|联系人的邮政地址。|
|city|String|否|""| **命名参数。** 联系人所在的城市。|
|country|String|否|""| **命名参数。** 联系人所在的国家。|
|neighborhood|String|否|""| **命名参数。** 联系人的邻居。|
|pobox|String|否|""| **命名参数。** 联系人的邮箱。|
|postcode|String|否|""| **命名参数。** 联系人所在区域的邮政编码。|
|region|String|否|""| **命名参数。** 联系人所在的区域。|
|street|String|否|""| **命名参数。** 联系人所在的街道。|
|labelName|String|否|""| **命名参数。** 邮政地址类型名称。|
|labelId|Int32|否|INVALID_LABEL_ID| **命名参数。** 邮政地址类型ID。|