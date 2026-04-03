## 概述

运动和方向传感器，如加速度计、陀螺仪等，能够监测设备的运动状态和方向变化，例如设备的旋转、倾斜等。

通过W3C标准协议接口，Web组件能够访问这些传感器的数据，进而实现更加丰富的用户交互功能。例如，开发者在网页应用中可以利用加速度计识别运动模式，指导用户进行健身运动，利用陀螺仪捕获玩家手中设备的倾斜和旋转动作，实现无按钮操控的游戏体验。

通过在JavaScript中调用以下支持的W3C标准协议接口，可以访问运动和方向传感器。

| 接口                      | 名称         | 说明                                                    |
| :------------------------- | :------------ | :-------------------------------------------------------|
| Accelerometer             | 加速度       | 可获取设备X、Y、Z轴方向的加速度数据。                                                                                                                    |
| Gyroscope                 | 陀螺仪       | 可获取设备X、Y、Z轴方向的角速度数据。                                                                                                                    |
| AbsoluteOrientationSensor | 绝对定位     | 可获取表示设备绝对定位方向的四元数，包含X、Y、Z和W分量。                                                                                                 |
| RelativeOrientationSensor | 相对定位     | 可获取表示设备相对定位方向的四元数，包含X、Y、Z和W分量。                                                                                                 |
| DeviceMotionEvent         | 设备运动事件 | 通过监听该事件，可获取设备在X、Y、Z轴方向上的加速度数据，设备在X、Y、Z轴方向上包含重力的加速度数据，以及设备在alpha、beta、gamma轴方向上旋转的速率数据。 |
| DeviceOrientationEvent    | 设备方向事件 | 通过监听该事件，可获取设备绕X、Y、Z轴的角度。                                                                                                            |

## 需要权限

使用加速度、陀螺仪及设备运动事件接口时，需在配置文件module.json5中声明相应的传感器权限。具体配置方法请参见[在配置文件中声明权限](../security/AccessToken/cj-declare-permissions.md)。

```json
"requestPermissions":[
  {
    "name" : "ohos.permission.ACCELEROMETER" // 加速度权限
  },
  {
    "name" : "ohos.permission.GYROSCOPE"     // 陀螺仪权限
  }
]
```

Web组件在对接运动和方向传感器时，需配置[onPermissionRequest](../../API_Reference/source_zh_cn/arkui-cj/cj-web-web.md#func-onpermissionrequestonpermissionrequestevent---unit)接口，通过该接口接收权限请求通知。