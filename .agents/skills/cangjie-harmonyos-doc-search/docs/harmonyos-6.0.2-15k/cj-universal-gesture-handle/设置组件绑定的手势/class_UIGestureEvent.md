## class UIGestureEvent

```cangjie
public class UIGestureEvent {}
```

**功能：** 用于设置组件绑定的手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### func addGesture(GestureHandler, GesturePriority, GestureMask)

```cangjie
public func addGesture(gesture: GestureHandler, priority!: GesturePriority = GesturePriority.Low, mask!: GestureMask = GestureMask.Normal): Unit
```

**功能：** 添加手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gesture|[GestureHandler](#class-gesturehandler)|是|-|手势处理器对象。|
|priority|[GesturePriority](#enum-gesturepriority)|否|GesturePriority.Low| **命名参数。** 绑定手势的优先级。|
|mask|[GestureMask](./cj-universal-gesture-bind.md#enum-GestureMask)|否|GestureMask.Normal| **命名参数。** 事件响应设置。|

### func addParallelGesture(GestureHandler, GestureMask)

```cangjie
public func addParallelGesture(gesture: GestureHandler, mask!: GestureMask = GestureMask.Normal): Unit
```

**功能：** 绑定可与子组件手势同时触发的手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|gesture|[GestureHandler](#class-gesturehandler)|是|-|手势处理器对象。|
|mask|[GestureMask](./cj-universal-gesture-bind.md#enum-GestureMask)|否|GestureMask.Normal| **命名参数。** 事件响应设置。|

### func removeGestureByTag(String)

```cangjie
public func removeGestureByTag(tag: String): Unit
```

**功能：** 移除该组件上通过modifier绑定的设置为指定标志的手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|tag|String|是|-|手势处理器标志。|

### func clearGestures()

```cangjie
public func clearGestures(): Unit
```

**功能：** 清除该组件上通过modifier绑定的所有手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19