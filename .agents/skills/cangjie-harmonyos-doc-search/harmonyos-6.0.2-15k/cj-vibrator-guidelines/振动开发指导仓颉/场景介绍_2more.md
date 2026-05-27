## 场景介绍

当设备需要设置不同的振动效果时，可以调用Vibrator模块，例如：设备的按键可以设置不同强度和不同时长的振动，闹钟和来电可以设置不同强度和时长的单次或周期振动。

详细的API介绍请参见[Vibrator API](../../../API_Reference/source_zh_cn/apis/SensorServiceKit/cj-apis-vibrator.md)。

## 接口说明

| 名称                                 | 描述                                     |
| --------------------------------------| -----------------------------------------|
| startVibration(effect: VibrateEffect, attribute: VibrateAttribute): Unit | 根据指定振动效果和振动属性触发马达振动。 |
| stopVibration(stopMode: Option&lt;VibratorStopMode&gt;): Unit| 按照指定模式停止马达的振动。           |
| isSupportEffect(effectId: EffectId): Bool| 查询是否支持传入的参数effectId。返回true则表示支持，否则不支持。 |