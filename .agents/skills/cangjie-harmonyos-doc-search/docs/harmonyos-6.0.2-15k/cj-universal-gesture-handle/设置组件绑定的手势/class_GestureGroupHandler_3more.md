## class GestureGroupHandler

```cangjie
public class GestureGroupHandler <: GestureHandler {}
```

**功能：** 手势组处理器对象类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [GestureHandler](#class-gesturehandler)

### init(GestureMode, Array\<GestureType>)

```cangjie
public init(mode: GestureMode, gesture: Array<Gesture>)
```

**功能：** 创建一个手势组处理器。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[GestureMode](./cj-universal-gesture-groupgesture.md#enum-GestureMode)|是|-|设置组合手势识别模式。初始值：GestureMode.Sequence。|
|gesture|Array\<GestureType>|是|-|设置1个或者多个基础手势类型时，这些手势会被识别为组合手势。若此参数Array长度为0则组合手势识别功能不生效。|

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
|callback|()->Unit|是|-|回调函数，顺序组合手势（GestureMode.Sequence）取消后触发该回调。|

## enum GesturePriority

```cangjie
public enum GesturePriority {
    | Low
    | High
}
```

**功能：** 组合手势识别模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### Low

```cangjie
Low
```

**功能：** 普通优先级手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### High

```cangjie
High
```

**功能：** 高优先级手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## 示例

见[动态手势设置](./cj-universal-attribute-gesturemodifier.md)。