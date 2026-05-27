## class Location

```cangjie
public class Location {
    public Location(
        public var location!: String = "",
        public var longitude!: Float64 = 0.0,
        public var latitude!: Float64 = 0.0
    )
}
```

**功能：** 日程地点。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

### var latitude

```cangjie
public var latitude: Float64 = 0.0
```

**功能：** 地点纬度。默认为0.0。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 20

### var location

```cangjie
public var location: String = ""
```

**功能：** 地点位置。默认为空字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### var longitude

```cangjie
public var longitude: Float64 = 0.0
```

**功能：** 地点经度。默认为0.0。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 20

### Location(String, Float64, Float64)

```cangjie
public Location(
    public var location!: String = "",
    public var longitude!: Float64 = 0.0,
    public var latitude!: Float64 = 0.0
)
```

**功能：** 构造Location对象。

**系统能力：** SystemCapability.Applications.CalendarData

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|location|String|否|""|地点位置。默认为空字符串。|
|longitude|Float64|否|0.0|地点纬度。默认为0.0。|
|latitude|Float64|否|0.0|地点经度。默认为0.0。|