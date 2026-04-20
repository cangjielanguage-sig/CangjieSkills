## class Location

```cangjie
public class Location {
    public var latitude: Float64
    public var longitude: Float64
    public var altitude: Float64
    public var accuracy: Float64
    public var speed: Float64
    public var timestamp: Int64
    public var direction: Float64
    public var timeSinceBoot: Int64
    public var additions: ?Array<String>
    public var additionsMap: ?Map<String, String>
    public var additionSize: ?Int64
    public var altitudeAccuracy: ?Float64
    public var speedAccuracy: ?Float64
    public var directionAccuracy: ?Float64
    public var uncertaintyOfTimeSinceBoot: ?Int64
    public var sourceType: ?LocationSourceType
}
```

**功能：** 位置信息。

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var accuracy

```cangjie
public var accuracy: Float64
```

**功能：** 表示精度信息，单位米。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var additionSize

```cangjie
public var additionSize: ?Int64
```

**功能：** 附加信息数量。取值范围为大于等于0。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var additions

```cangjie
public var additions: ?Array<String>
```

**功能：** 附加信息。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var additionsMap

```cangjie
public var additionsMap: ?Map<String, String>
```

**功能：** 附加信息。具体内容和顺序与additions一致。

**类型：** ?Map\<String, String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var altitude

```cangjie
public var altitude: Float64
```

**功能：** 表示高度信息，单位米。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var altitudeAccuracy

```cangjie
public var altitudeAccuracy: ?Float64
```

**功能：** 表示高度信息的精度，单位米。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var direction

```cangjie
public var direction: Float64
```

**功能：** 表示航向信息。单位是“度”，取值范围为0到360。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var directionAccuracy

```cangjie
public var directionAccuracy: ?Float64
```

**功能：** 表示航向信息的精度。单位是“度”，取值范围为0到360。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var latitude

```cangjie
public var latitude: Float64
```

**功能：** 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var longitude

```cangjie
public var longitude: Float64
```

**功能：** 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var sourceType

```cangjie
public var sourceType: ?LocationSourceType
```

**功能：** 表示定位结果的来源。

**类型：** [LocationSourceType](#enum-locationsourcetype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22

### var speed

```cangjie
public var speed: Float64
```

**功能：** 表示速度信息，单位米每秒。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 22