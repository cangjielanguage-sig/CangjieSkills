## class LocationOptions

```cangjie
public class LocationOptions {
    public LocationOptions(
        public var latitude: Float32,
        public var longitude: Float32,
        public var altitude: Float32
    )
}
```

**功能：** 指示地理位置。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

### var altitude

```cangjie
public var altitude: Float32
```

**功能：** 海拔高度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var latitude

```cangjie
public var latitude: Float32
```

**功能：** 纬度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var longitude

```cangjie
public var longitude: Float32
```

**功能：** 经度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### LocationOptions(Float32, Float32, Float32)

```cangjie
public LocationOptions(
    public var latitude: Float32,
    public var longitude: Float32,
    public var altitude: Float32
)
```

**功能：** 指示地理位置。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|latitude|Float32|是|-|纬度。|
|longitude|Float32|是|-|经度。|
|altitude|Float32|是|-|海拔高度。|

## class RotationMatrixResponse

```cangjie
public class RotationMatrixResponse {
    public RotationMatrixResponse(
        public var rotation: Array<Float32>,
        public var inclination: Array<Float32>
    )
}
```

**功能：** 设置旋转矩阵响应对象。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

### var inclination

```cangjie
public var inclination: Array<Float32>
```

**功能：** 倾斜矩阵。

**类型：** Array\<Float32>

**读写能力：** 可读写

**起始版本：** 19

### var rotation

```cangjie
public var rotation: Array<Float32>
```

**功能：** 旋转矩阵。

**类型：** Array\<Float32>

**读写能力：** 可读写

**起始版本：** 19

### RotationMatrixResponse(Array\<Float32>, Array\<Float32>)

```cangjie
public RotationMatrixResponse(
    public var rotation: Array<Float32>,
    public var inclination: Array<Float32>
)
```

**功能：** 设置旋转矩阵响应对象。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotation|Array\<Float32>|是|-|旋转矩阵。|
|inclination|Array\<Float32>|是|-|倾斜矩阵。|