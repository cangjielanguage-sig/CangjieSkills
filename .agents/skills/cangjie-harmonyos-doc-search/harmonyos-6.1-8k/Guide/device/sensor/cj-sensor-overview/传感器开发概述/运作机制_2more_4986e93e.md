## 运作机制

传感器包含如下四个模块：Sensor API、Sensor Framework、Sensor Service和HDF层。

**图1** 传感器

![sensor](figures/sensor.png)

- Sensor API：提供传感器的基础API，主要包含查询传感器列表，订阅/取消传感器的数据、执行控制命令等，简化应用开发。
- Sensor Framework：主要实现传感器的订阅管理，数据通道的创建、销毁、订阅与取消订阅，实现与SensorService的通信。
- Sensor Service：主要实现HD_IDL层数据接收、解析、分发，前后台的策略管控，对该设备Sensor的管理，Sensor权限管控等。
- HDF层：对不同的FIFO、频率进行策略选择，以及适配不同设备。

## 约束与限制

1. 针对下面所列传感器，开发者需要请求相应的权限，才能获取到相应传感器的数据。

   | 传感器  | 权限名  | 敏感级别  | 权限描述  |
   | ------- | -------- | -------- | ---------- |
   | 加速度传感器，加速度未校准传感器，线性加速度传感器 | ohos.permission.ACCELEROMETER  | system_grant | 允许应用读取加速度传感器的数据，包括：加速度传感器、加速度未校准传感器、线性加速度传感器。 |
   | 陀螺仪传感器，陀螺仪未校准传感器    | ohos.permission.GYROSCOPE   | system_grant | 允许应用读取陀螺仪传感器的数据，包括：陀螺仪传感器、陀螺仪未校准传感器。 |
   | 计步器        | ohos.permission.ACTIVITY_MOTION  | user_grant   | 该权限允许应用读取用户当前的运动状态。例如：判断用户是否处于运动中、记录用户行走步数。 |
   | 心率计         | ohos.permission.READ_HEALTH_DATA | user_grant   | 该权限允许应用读取用户的健康数据，如：心率数据等。  |

2. 传感器数据订阅和取消订阅接口成对调用，当不再需要订阅传感器数据时，开发者需要调用取消订阅接口停止数据上报。