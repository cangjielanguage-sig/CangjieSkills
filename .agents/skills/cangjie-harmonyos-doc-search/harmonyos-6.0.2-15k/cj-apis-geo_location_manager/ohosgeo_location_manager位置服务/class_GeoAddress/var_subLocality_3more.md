### var subLocality

```cangjie
public var subLocality: String
```

**功能：** 表示子城市信息，一般是区/县。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var subRoadName

```cangjie
public var subRoadName: String
```

**功能：** 表示子路名信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### GeoAddress(Float64, Float64, String, String, String, String, String, String, String, String, String, String, String, String, String, String, Array\<String>, Int32)

```cangjie
public GeoAddress (
    public var latitude: Float64,
    public var longitude: Float64,
    public var locale: String,
    public var placeName: String,
    public var countryCode: String,
    public var countryName: String,
    public var administrativeArea: String,
    public var subAdministrativeArea: String,
    public var locality: String,
    public var subLocality: String,
    public var roadName: String,
    public var subRoadName: String,
    public var premises: String,
    public var postalCode: String,
    public var phoneNumber: String,
    public var addressUrl: String,
    public var descriptions: Array<String>,
    public var descriptionsSize: Int32
)
```

**功能：** 创建GeoAddress对象

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|latitude|Float64|是|-|表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。|
|longitude|Float64|是|-|表示经度信息，正值表示东经，负值表是西经。取值范围为-180到180。仅支持WGS84坐标系。|
|locale|String|是|-|表示位置描述信息的语言，“zh”代表中文，“en”代表英文。|
|placeName|String|是|-|表示详细地址信息。|
|countryCode|String|是|-|表示国家码信息。|
|countryName|String|是|-|表示国家信息。|
|administrativeArea|String|是|-|表示国家以下的一级行政区，一般是省/州。|
|subAdministrativeArea|String|是|-|表示国家以下的二级行政区，一般是市。|
|locality|String|是|-|表示城市信息，一般是市。|
|subLocality|String|是|-|表示子城市信息，一般是区/县。|
|roadName|String|是|-|表示路名信息。|
|subRoadName|String|是|-|表示子路名信息。|
|premises|String|是|-|表示门牌号信息。|
|postalCode|String|是|-|表示邮政编码信息。|
|phoneNumber|String|是|-|表示联系方式信息。|
|addressUrl|String|是|-|表示位置信息附件的网址信息。|
|descriptions|Array\<String>|是|-|表示附加的描述信息。目前包含城市编码cityCode（Array下标为0）和区划编码adminCode（Array下标为1），例如["025","320114001"]。|
|descriptionsSize|Int32|是|-|表示附加的描述信息数量。取值范围为大于等于0，推荐该值小于10。|