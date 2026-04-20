## func transformRotationMatrix(Array\<Float32>, CoordinatesOptions)

```cangjie
public func transformRotationMatrix(inRotationVector: Array<Float32>, coordinates: CoordinatesOptions): Array<Float32>
```

**功能：** 根据指定坐标系映射旋转矩阵。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|inRotationVector|Array\<Float32>|是|-|旋转矩阵。|
|coordinates|[CoordinatesOptions](#class-coordinatesoptions)|是|-|指定坐标系方向。|

**返回值：**

|类型|说明|
|----|----|
|Array\<Float32>|返回转换后的旋转矩阵。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[传感器错误码](../../errorcodes/cj-errorcode-sensor.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                                     |
  | -------- | ------------------------------------------------------------ |
  | 401      | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
  | 14500101 | Service exception.                                           |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

try {
    let rotationMatrix: Array<Float32> = [1.0, 0.0, 0.0, 0.0, 0.87, -0.50, 0.0, 0.50, 0.87]
    let data = transformRotationMatrix(rotationMatrix, CoordinatesOptions(1, 3))
    AppLog.info("Succeeded in getting transform rotationMatrix: ${data}")
} catch (e: BusinessException) {
    AppLog.error("Failed to get transform rotationMatrix. Code: ${e.code}, message: ${e.message}")
}
```

## class AccelerometerResponse

```cangjie
public class AccelerometerResponse <: Response {
    public AccelerometerResponse(
        public var x: Float32,
        public var y: Float32,
        public var z: Float32
    )
}
```

**功能：** 加速度传感器数据，继承自[Response](#class-response)。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**父类型：**

- [Response](#class-response)

### var x

```cangjie
public var x: Float32
```

**功能：** 施加在设备x轴的加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 施加在设备y轴的加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var z

```cangjie
public var z: Float32
```

**功能：** 施加在设备z轴的加速度，单位：m/s²。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### AccelerometerResponse(Float32, Float32, Float32)

```cangjie
public AccelerometerResponse(
    public var x: Float32,
    public var y: Float32,
    public var z: Float32
)
```

**功能：** 构造加速度传感器数据。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|施加在设备x轴的加速度，单位：m/s²。|
|y|Float32|是|-|施加在设备y轴的加速度，单位：m/s²。|
|z|Float32|是|-|施加在设备z轴的加速度，单位：m/s²。|