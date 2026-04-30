## 场景介绍

当设备需要获取传感器数据时，可以使用sensor模块，例如：通过订阅方向传感器数据感知用户设备当前的朝向，通过订阅计步传感器数据统计用户的步数等。

详细的API介绍请参见[Sensor API](../../../API_Reference/source_zh_cn/apis/SensorServiceKit/cj-apis-sensor.md)。

## 接口说明

| 名称 | 描述 |
| -------- | -------- |
| on\<T>(\`type\`:SensorId, callback:Callback1Argument\<T>, option:?SensorOptions):Unit where T <: Response | 持续监听传感器数据变化。 |
| once\<T>(\`type\`:SensorId, callback:Callback1Argument\<T>):Unit  where T <: Response | 获取一次传感器数据变化。 |
| off(\`type\`: SensorId, callback!: ?CallbackObject = None): Unit | 注销传感器数据的监听。 |
| getSensorList():Array\<Sensor> | 获取设备上的所有传感器信息。 |