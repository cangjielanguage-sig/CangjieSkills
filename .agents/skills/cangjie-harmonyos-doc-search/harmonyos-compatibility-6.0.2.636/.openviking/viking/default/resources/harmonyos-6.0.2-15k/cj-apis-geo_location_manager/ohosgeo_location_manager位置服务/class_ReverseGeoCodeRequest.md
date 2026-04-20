## class ReverseGeoCodeRequest

```cangjie
public class ReverseGeoCodeRequest {
    public var locale: String
    public var country: String
    public var latitude: Float64
    public var longitude: Float64
    public var maxItems: Int32
    public init(latitude: Float64, longitude: Float64, locale!: String = System.getSystemLanguage(), country!: String = System.getSystemRegion(), maxItems!: Int32 = 1)
}
```

**功能：** 逆地理编码请求参数。

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

**功能：** 指定位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var longitude

```cangjie
public var longitude: Float64
```

**功能：** 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var maxItems

```cangjie
public var maxItems: Int32
```

**功能：** 指定返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### init(Float64, Float64, String, String, Int32)

```cangjie
public init(latitude: Float64, longitude: Float64, locale!: String = System.getSystemLanguage(), country!: String = System.getSystemRegion(), maxItems!: Int32 = 1)
```

**功能：** 构造ReverseGeoCodeRequest对象。

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|latitude|Float64|是|-| 指定位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。|
|longitude|Float64|是|-| 限制查询结果在指定的国家内，采用ISO 3166-1 alpha-2 。“CN”代表中国。默认值从设置中的“语言和地区”获取。|
|locale|String|否|System.getSystemLanguage()| **命名参数。** 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。|
|country|String|否|System.getSystemRegion()| **命名参数。** 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。|
|maxItems|Int32|否|1| **命名参数。** 指定返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。|