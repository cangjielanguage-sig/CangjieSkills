## 备注

传感器的开发均同上述加速度传感器ACCELEROMETER。需要注意的是，传感器按采集数据方式分为周期传感器和瞬时传感器。周期传感器按预先设定的固定时间间隔采集并输出数据，如环境温度传感器AMBIENT_TEMPERATURE，订阅后，传感器按设计的时间间隔上报数据。周期传感器有GRAVITY、AMBIENT_TEMPERATURE、HUMIDITY、BAROMETER等。瞬时传感器受特定触发事件影响才采集并输出数据，如计步传感器PEDOMETER，步数有变化会上报。瞬时传感器有HALL、PROXIMITY、WEAR_DETECTION、PEDOMETER、PEDOMETER_DETECTION。
<!--Del-->

## 示例代码

[获取传感器信息](https://gitcode.com/openharmony/applications_app_samples_cangjie/tree/master/code/BasicFeature/DeviceManagement/Sensor)
<!--DelEnd-->