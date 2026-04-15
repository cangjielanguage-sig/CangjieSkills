# 传感器开发指导

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 场景介绍

当设备需要获取传感器数据时，可以使用sensor模块，例如：通过订阅方向传感器数据感知用户设备当前的朝向，通过订阅计步传感器数据统计用户的步数等。

详细的API介绍请参见[Sensor API](../../reference/SensorServiceKit/cj-apis-sensor.md)。

## 接口说明

| 名称 | 描述 |
| -------- | -------- |
| on\<T>(sensorType: SensorId, callback: Callback1Argument\<T>, option!: ?Options = None): Unit where T \<: Response | 持续监听传感器数据变化。 |
| once\<T>(sensorType: SensorId, callback: Callback1Argument\<T>): Unit where T \<: Response | 获取一次传感器数据变化。 |
| off(sensorType: SensorId, callback!: ?CallbackObject = None): Unit | 注销传感器数据的监听。 |
| getSensorList():Array\<Sensor> | 获取设备上的所有传感器信息。 |