## class GeomagneticResponse

```cangjie
public class GeomagneticResponse {
    public GeomagneticResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32,
        public var geomagneticDip: Float32,
        public var deflectionAngle: Float32,
        public var levelIntensity: Float32,
        public var totalIntensity: Float32
    )
}
```

**功能：** 设置地磁响应对象。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

### var deflectionAngle

```cangjie
public var deflectionAngle: Float32
```

**功能：** 地磁偏角，即地磁北方向与正北方向在水平面上的角度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var geomagneticDip

```cangjie
public var geomagneticDip: Float32
```

**功能：** 地磁倾角，即地球磁场线与水平面的夹角。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var levelIntensity

```cangjie
public var levelIntensity: Float32
```

**功能：** 地磁场的水平强度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var totalIntensity

```cangjie
public var totalIntensity: Float32
```

**功能：** 地磁场的总强度。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var x

```cangjie
public var x: Float32
```

**功能：** 地磁场的北分量。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 地磁场的东分量。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 地磁场的垂直分量。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### GeomagneticResponse(Float32, Float32, Float32, Float32, Float32, Float32, Float32)

```cangjie
public GeomagneticResponse(
    public var x: Float32,
    public var y: Float32,
    public var z: Float32,
    public var geomagneticDip: Float32,
    public var deflectionAngle: Float32,
    public var levelIntensity: Float32,
    public var totalIntensity: Float32
)
```

**功能：** 设置地磁响应对象。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|地磁场的北分量。|
|y|Float32|是|-|地磁场的东分量。|
|z|Float32|是|-|地磁场的垂直分量。|
|geomagneticDip|Float32|是|-|地磁倾角，即地球磁场线与水平面的夹角。|
|deflectionAngle|Float32|是|-|地磁偏角，即地磁北方向与正北方向在水平面上的角度。|
|levelIntensity|Float32|是|-|地磁场的水平强度。|
|totalIntensity|Float32|是|-|地磁场的总强度。|