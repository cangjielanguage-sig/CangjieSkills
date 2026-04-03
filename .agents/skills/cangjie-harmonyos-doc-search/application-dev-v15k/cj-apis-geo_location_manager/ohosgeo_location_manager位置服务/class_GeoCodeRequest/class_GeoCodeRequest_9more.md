## class GeoCodeRequest

```cangjie
public class GeoCodeRequest {
    public var locale: String
    public var country: String
    public var description: String
    public var maxItems: Int32
    public var minLatitude: Float64
    public var minLongitude: Float64
    public var maxLatitude: Float64
    public var maxLongitude: Float64
    public init(description: String, locale!: String = System.getSystemLanguage(), country!: String = System.getSystemRegion(),
        maxItems!: Int32 = 1, minLatitude!: Float64 = -90.0, minLongitude!: Float64 = -180.0, maxLatitude!: Float64 = 90.0,
        maxLongitude!: Float64 = 180.0)
}
```

**功能：** 地理编码请求参数。

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

### var country

```cangjie
public var country: String
```

**功能：** 限制查询结果在指定的国家内，采用ISO 3166-1 alpha-2 。“CN”代表中国。默认值从设置中的“语言和地区”获取。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var description

```cangjie
public var description: String
```

**功能：** 表示位置信息描述，如“上海市浦东新区xx路xx号”。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var locale

```cangjie
public var locale: String
```

**功能：** 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var maxItems

```cangjie
public var maxItems: Int32
```

**功能：** 表示返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var maxLatitude

```cangjie
public var maxLatitude: Float64
```

**功能：** 表示最大纬度信息。取值范围为-90到90。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var maxLongitude

```cangjie
public var maxLongitude: Float64
```

**功能：** 表示最大经度信息。取值范围为-180到180。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var minLatitude

```cangjie
public var minLatitude: Float64
```

**功能：** 表示最小纬度信息，与下面三个参数一起，表示一个经纬度范围。取值范围为-90到90。仅支持WGS84坐标系。如果该参数有值时，下面三个参数必填。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var minLongitude

```cangjie
public var minLongitude: Float64
```

**功能：** 表示最小经度信息。取值范围为-180到180。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19