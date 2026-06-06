### init(String, String, String, Int32, Float64, Float64, Float64, Float64)

```cangjie
public init(description: String, locale!: String = System.getSystemLanguage(), country!: String = System.getSystemRegion(),
    maxItems!: Int32 = 1, minLatitude!: Float64 = -90.0, minLongitude!: Float64 = -180.0, maxLatitude!: Float64 = 90.0,
    maxLongitude!: Float64 = 180.0)
```

**功能：** 构造GeoCodeRequest对象。

**系统能力：** SystemCapability.Location.Location.Geocoder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|description|String|是|-|表示位置信息描述，如“上海市浦东新区xx路xx号”。|
|locale|String|否|System.getSystemLanguage()| **命名参数。** 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。|
|country|String|否|System.getSystemRegion()| **命名参数。** 限制查询结果在指定的国家内，采用ISO 3166-1 alpha-2 。“CN”代表中国。默认值从设置中的“语言和地区”获取。|
|maxItems|Int32|否|1| **命名参数。** 表示返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。|
|minLatitude|Float64|否|- 90.0| **命名参数。** 表示最小纬度信息，与下面三个参数一起，表示一个经纬度范围。取值范围为-90到90。仅支持WGS84坐标系。如果该参数有值时，下面三个参数必填。|
|minLongitude|Float64|否|- 180.0| **命名参数。** 表示最小经度信息。取值范围为-180到180。仅支持WGS84坐标系。|
|maxLatitude|Float64|否|90.0| **命名参数。** 表示最大纬度信息。取值范围为-90到90。仅支持WGS84坐标系。|
|maxLongitude|Float64|否|180.0| **命名参数。** 表示最大经度信息。取值范围为-180到180。仅支持WGS84坐标系。|