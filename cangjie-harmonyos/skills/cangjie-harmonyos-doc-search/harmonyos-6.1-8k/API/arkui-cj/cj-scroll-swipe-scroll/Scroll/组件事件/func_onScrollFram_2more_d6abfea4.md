### func onScrollFrameBegin(?OnScrollFrameBeginCallback)

```cangjie
public func onScrollFrameBegin(event: ?OnScrollFrameBeginCallback): This
```

**功能：** 每帧开始滚动时触发该事件，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。

支持offsetRemain为负值。

若通过onScrollFrameBegin事件和scrollBy方法实现容器嵌套滚动，需设置子滚动节点的EdgeEffect为None。如Scroll嵌套List滚动时，List组件的edgeEffect属性需设置为EdgeEffect.None。

触发该事件的条件：

1. 滚动组件触发滚动时触发，包括键鼠操作和其他触发滚动的输入设置。

2. 调用控制器接口时不触发。

3. 越界回弹不触发。

4. 拖动滚动条不触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[OnScrollFrameBeginCallback](#type-onscrollframebegincallback)|是|-|回调函数，每帧开始滚动时触发。参数一：即将发生的滑动量，单位vp。参数二：当前滑动状态。初始值：{ _, _ => 0.0 }。|

### func onScrollEdge(?OnScrollEdgeCallback)

```cangjie
public func onScrollEdge(event: ?OnScrollEdgeCallback): This
```

**功能：** 滚动到边缘时触发该事件。

触发该事件的条件 ：

1. 滚动组件滚动到边缘时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用。

3. 越界回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?[OnScrollEdgeCallback](#type-onscrolledgecallback)|是|-|回调函数，滚动到边缘时触发。参数：滚动到的边缘位置。初始值：{ _ => 0.0 }。|