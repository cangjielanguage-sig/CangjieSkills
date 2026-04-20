### func trackThickness(?Length)

```cangjie
public func trackThickness(value: ?Length): This
```

**功能：** 根据指定的Length设置滑轨的粗细。设置为小于等于0的值时，取初始值。

为保证滑块和滑轨的SliderStyle样式，blockSize跟随trackThickness同比例增减。

当style为SliderStyle.OutSet时，trackThickness:blockSize = 1:4，当style为SliderStyle.InSet时，trackThickness:blockSize = 5:3。

在变更trackThickness过程中，若trackThickness的大小或者blockSize的大小超过slider组件的width或者height（SliderStyle.OutSet时可能trackThickness没超过，但是blockSize超过了），取初始值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Length](./cj-common-types.md#interface-length)|是|-|滑轨的粗细。<br/>初始值：当参数style的值设置SliderStyle.OutSet 时为 4.0.vp，SliderStyle.InSet时为20.0.vp。|