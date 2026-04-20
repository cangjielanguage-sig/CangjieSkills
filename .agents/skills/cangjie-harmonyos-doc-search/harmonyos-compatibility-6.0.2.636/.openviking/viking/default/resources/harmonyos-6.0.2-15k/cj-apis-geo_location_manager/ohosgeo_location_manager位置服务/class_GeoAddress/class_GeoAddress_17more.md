## class GeoAddress

```cangjie
public class GeoAddress {
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
}
```

**功能：** 地理编码地址信息。

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

### var addressUrl

```cangjie
public var addressUrl: String
```

**功能：** 表示位置信息附件的网址信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var administrativeArea

```cangjie
public var administrativeArea: String
```

**功能：** 表示国家以下的一级行政区，一般是省/州。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var countryCode

```cangjie
public var countryCode: String
```

**功能：** 表示国家码信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var countryName

```cangjie
public var countryName: String
```

**功能：** 表示国家信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var descriptions

```cangjie
public var descriptions: Array<String>
```

**功能：** 表示附加的描述信息。目前包含城市编码cityCode（Array下标为0）和区划编码adminCode（Array下标为1），例如["025","320114001"]。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var descriptionsSize

```cangjie
public var descriptionsSize: Int32
```

**功能：** 表示附加的描述信息数量。取值范围为大于等于0，推荐该值小于10。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var latitude

```cangjie
public var latitude: Float64
```

**功能：** 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var locale

```cangjie
public var locale: String
```

**功能：** 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var locality

```cangjie
public var locality: String
```

**功能：** 表示城市信息，一般是市。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var longitude

```cangjie
public var longitude: Float64
```

**功能：** 表示经度信息，正值表示东经，负值表是西经。取值范围为-180到180。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var phoneNumber

```cangjie
public var phoneNumber: String
```

**功能：** 表示联系方式信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var placeName

```cangjie
public var placeName: String
```

**功能：** 表示详细地址信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var postalCode

```cangjie
public var postalCode: String
```

**功能：** 表示邮政编码信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var premises

```cangjie
public var premises: String
```

**功能：** 表示门牌号信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var roadName

```cangjie
public var roadName: String
```

**功能：** 表示路名信息。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var subAdministrativeArea

```cangjie
public var subAdministrativeArea: String
```

**功能：** 表示国家以下的二级行政区，一般是市。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19