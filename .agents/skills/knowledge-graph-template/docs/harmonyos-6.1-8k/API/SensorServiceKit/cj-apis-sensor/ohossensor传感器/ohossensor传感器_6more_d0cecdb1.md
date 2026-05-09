# ohos.sensor（传感器）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

sensor模块提供了获取传感器数据的能力，包括获取传感器属性列表、订阅传感器数据以及一些通用的传感器算法。

## 导入模块

```cangjie
import kit.SensorServiceKit.*
```

## 权限列表

ohos.permission.ACCELEROMETER

ohos.permission.GYROSCOPE

ohos.permission.READ_HEALTH_DATA

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func getSensorList()

```cangjie
public func getSensorList(): Array<Sensor>
```

**功能：** 获取设备上的所有传感器信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**返回值：**

| 类型                              | 说明         |
|:------------------------------- |:---------- |
| Array\<[Sensor](#class-sensor)> | 返回传感器属性列表。 |

**异常：**

- BusinessException：对应错误码如下表，详见[传感器错误码](./cj-errorcode-sensor.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; 2. Sensor service ipc exception; 3. Sensor data channel exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let sensors = getSensorList()
    for (index in 0..sensors.size) {
        Hilog.info(0, "test", "Succeeded in getting sensor${index}: ${sensors[index].sensorId}", "")
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "Failed to get sensor list. Code: ${e.code}, message: ${e.message}", "")
}
```

## func getSingleSensor(SensorId)

```cangjie
public func getSingleSensor(sensorType: SensorId): Sensor
```

**功能：** 获取指定类型的传感器信息。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名        | 类型                         | 必填  | 默认值 | 说明     |
|:---------- |:-------------------------- |:--- |:--- |:------ |
| sensorType | [SensorId](#enum-sensorid) | 是   | -   | 传感器类型。 |

**返回值：**

| 类型                      | 说明       |
|:----------------------- |:-------- |
| [Sensor](#class-sensor) | 返回传感器信息。 |

**异常：**

- BusinessException：对应错误码如下表，详见[传感器错误码](./cj-errorcode-sensor.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 14500101 | Service exception. Possible causes: 1. Sensor hdf service exception; 2. Sensor service ipc exception; 3. Sensor data channel exception. |
  | 14500102 | The sensor is not supported by the device. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.SensorServiceKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let sensors = getSingleSensor(SensorId.Accelerometer)
    Hilog.info(0, "test", "Succeeded in getting sensor: ${sensors.sensorName}", "")
} catch (e: BusinessException) {
    Hilog.error(0, "test", "Code: ${e.code}, message: ${e.message}", "")
}
```