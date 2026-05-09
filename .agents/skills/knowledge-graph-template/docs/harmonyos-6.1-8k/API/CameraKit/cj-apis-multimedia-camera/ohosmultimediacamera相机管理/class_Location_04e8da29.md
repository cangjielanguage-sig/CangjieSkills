## class Location

```cangjie
public class Location {
    public var latitude: Float64
    public var longitude: Float64
    public var altitude: Float64
    public init(latitude: Float64, longitude: Float64, altitude: Float64)
}
```

**功能：** 图片地理位置信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var altitude

```cangjie
public var altitude: Float64
```

**功能：** 海拔(米)。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var latitude

```cangjie
public var latitude: Float64
```

**功能：** 纬度（度）。取值范围：[-90, 90]。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var longitude

```cangjie
public var longitude: Float64
```

**功能：** 经度（度）。取值范围：[-180, 180]。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### init(Float64, Float64, Float64)

```cangjie
public init(latitude: Float64, longitude: Float64, altitude: Float64)
```

**功能：** 创建Location对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|latitude|Float64|是|-|纬度（度）。取值范围：[-90, 90]。|
|longitude|Float64|是|-|经度（度）。取值范围：[-180, 180]。|
|altitude|Float64|是|-|海拔(米)。|