## func getQuaternion(Array\<Float32>)

```cangjie
public func getQuaternion(rotationVector: Array<Float32>): Array<Float32>
```

**功能：** 根据旋转向量计算归一化四元数。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotationVector|Array\<Float32>|是|-|旋转矢量。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|返回归一化四元数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[传感器错误码](../../errorcodes/cj-errorcode-sensor.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed.|
  |14500101|Service exception.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

try {
    let rotationVector: Array<Float32> = [0.20046076, 0.21907, 0.73978853, 0.60376877]
    let data = getQuaternion(rotationVector)
    AppLog.info("Succeeded in getting quaternion: ${data}")
} catch (e: BusinessException) {
    AppLog.error("Failed to get quaternion. Code: ${e.code}, message: ${e.message}")
}
```

## func getRotationMatrix(Array\<Float32>)

```cangjie
public func getRotationMatrix(rotationVector: Array<Float32>): Array<Float32>
```

**功能：** 根据旋转矢量计算旋转矩阵。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotationVector|Array\<Float32>|是|-|旋转矢量。|

**返回值：**

|类型|说明|
|----|----|
|[RotationMatrixResponse](#class-rotationmatrixresponse)|返回旋转矩阵。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[传感器错误码](../../errorcodes/cj-errorcode-sensor.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息                                                     |
  |:----|:----|
  | 401      | Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
  | 14500101 | Service exception.                                           |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import ohos.base.*

try {
    let rotationVector: Array<Float32> = [0.20046076, 0.21907, 0.73978853, 0.60376877]
    let data = getRotationMatrix(rotationVector)
} catch (e: BusinessException) {
    AppLog.error("Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}")
}
```