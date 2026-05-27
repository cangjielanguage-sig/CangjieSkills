# 组合手势

手势识别组合，即多种手势组合为复合手势，支持连续识别、并行识别和互斥识别。

## 导入模块

```cangjie
import kit.UIkit.*
```

## 权限列表

无

## 创建组件

### init(GestureMode, Array\<GestureType>)

```cangjie
public init(mode: GestureMode, gesture: Array<GestureType>)
```

**功能：** 创建一个手势识别组合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[GestureMode](#enum-gesturemode)|是|-|设置组合手势识别模式。|
|gesture|[TapGesture](./cj-universal-gesture-tapgesture.md)<br>[LongPressGesture](./cj-universal-gesture-longpressgesture.md)<br>[PanGesture](./cj-universal-gesture-pangesture.md)<br>[PinchGesture](./cj-universal-gesture-pinchgesture.md)<br>[RotationGesture](./cj-universal-gesture-rotationgesture.md)<br>[SwipeGesture](./cj-universal-gesture-swipegesture.md)<br>[GestureGroup](./cj-universal-gesture-groupgesture.md)|是|-|设置1个或者多个基础手势类型时，这些手势会被识别为组合手势。若此参数Array长度为0则组合手势识别功能不生效。<br>**说明：**<br>当需要为一个组件同时添加单击和双击手势时，可在组合手势中添加两个TapGesture，需要双击手势在前，单击手势在后，否则不生效。|

## 组件事件

### func onCancel(() -> Unit)

```cangjie
public func onCancel(callback: () -> Unit): This
```

**功能：** 顺序组合手势（GestureMode.Sequence）取消后触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|() \-> Unit|是|-|回调函数，顺序组合手势（GestureMode.Sequence）取消后触发该回调。|

## 基础类型定义

### enum GestureMode

```cangjie
public enum GestureMode {
    | Sequence
    | Parallel
    | Exclusive
}
```

**功能：** 组合手势的识别模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Sequence

```cangjie
Sequence
```

**功能：** 顺序识别，按照手势的注册顺序识别手势，直到所有手势识别成功。若有一个手势识别失败，后续手势识别均失败。顺序识别手势组仅有最后一个手势可以响应onActionEnd。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Parallel

```cangjie
Parallel
```

**功能：** 并发识别，注册的手势同时识别，直到所有手势识别结束，手势识别互相不影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### Exclusive

```cangjie
Exclusive
```

**功能：** 互斥识别，注册的手势同时识别，若有一个手势识别成功，则结束手势识别。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19