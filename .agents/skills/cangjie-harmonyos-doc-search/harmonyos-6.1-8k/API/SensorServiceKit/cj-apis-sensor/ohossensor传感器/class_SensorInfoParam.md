## class SensorInfoParam

```cangjie
public class SensorInfoParam {
    public var deviceId: Int32
    public var sensorIndex: Int32
    public init(deviceId!: Int32 = -1, sensorIndex!: Int32 = 0)
}
```

**功能：** 传感器传入设置参数，多传感器情况下通过deviceId、sensorIndex控制指定传感器。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: Int32
```

**功能：** 设备ID：设置为-1，表示本地设备，设备ID需通过[getSensorList](#func-getsensorlist)查询或者监听设备上下线接口[on](#func-ontsensorid-callback1argumentt-options-where-t--response)获取。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### var sensorIndex

```cangjie
public var sensorIndex: Int32
```

**功能：** 传感器索引：设置为0，为设备上的默认传感器，其它传感器ID需通过[getSensorList](#func-getsensorlist)查询或者监听设备上下线接口[on](#func-ontsensorid-callback1argumentt-options-where-t--response)获取。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

### init(Int32, Int32)

```cangjie
public init(deviceId!: Int32 = -1, sensorIndex!: Int32 = 0)
```

**功能：** 构造函数，创建SensorInfoParam实例。

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 22

**参数：**

| 参数名         | 类型    | 必填  | 默认值 | 说明     |
|:----------- |:----- |:--- |:--- |:------ |
| deviceId    | Int32 | 否   | - 1 | **命名参数。** 设备ID：默认值为-1，表示本地设备，设备ID需通过[getSensorList](#func-getsensorlist)查询或者监听设备上下线接口[on](#func-ontsensorid-callback1argumentt-options-where-t--response)获取。  |
| sensorIndex | Int32 | 否   | 0   | **命名参数。** 传感器索引：默认值为0，为设备上的默认传感器，其它传感器ID需通过[getSensorList](#func-getsensorlist)查询或者监听设备上下线接口[on](#func-ontsensorid-callback1argumentt-options-where-t--response)获取。 |