## struct Location

```cangjie
public struct Location {
    public var latitude: Float64
    public var longtitude: Float64
    public var altitude: Float64
    public init(latitude: Float64, longtitude: Float64, altitude: Float64)
}
```

**功能：** 图片地理位置信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var altitude

```cangjie
public var altitude: Float64
```

**功能：** 海拔(米)。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var latitude

```cangjie
public var latitude: Float64
```

**功能：** 纬度(度)。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var longtitude

```cangjie
public var longtitude: Float64
```

**功能：** 经度(度)。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### init(Float64, Float64, Float64)

```cangjie
public init(latitude: Float64, longtitude: Float64, altitude: Float64)
```

**功能：** 创建Location对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|latitude|Float64|是|-|纬度(度)。|
|longtitude|Float64|是|-|经度(度)。|
|altitude|Float64|是|-|海拔(米)。|