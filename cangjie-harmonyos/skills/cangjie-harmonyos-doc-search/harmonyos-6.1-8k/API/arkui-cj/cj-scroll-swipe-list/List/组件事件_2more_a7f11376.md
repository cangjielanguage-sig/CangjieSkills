## 组件事件

### func onScrollFrameBegin(?(Float64, ScrollState) -> OnScrollFrameBeginHandlerResult)

```cangjie
public func onScrollFrameBegin(event: ?(Float64, ScrollState) -> OnScrollFrameBeginHandlerResult): This
```

**功能：** 每帧滚动开始时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?(Float64, [ScrollState](./cj-common-types.md#enum-scrollstate)) -> [OnScrollFrameBeginHandlerResult](#class-onscrollframebeginhandlerresult)|是|-|滚动帧开始事件回调。参数一表示即将发生的滑动量，参数二表示当前的滑动的状态，返回值表示实际滑动量。初始值：{ _, _ => OnScrollFrameBeginHandlerResult(offsetRemain: 0.0) }。|

### func onScrollIndex(?(Int32, Int32, Int32) -> Unit)

```cangjie
public func onScrollIndex(event: ?(Int32, Int32, Int32) -> Unit): This
```

**功能：** 当子组件进入或离开列表显示区域时触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|?(Int32, Int32, Int32) -> Unit|是|-|滚动索引事件回调。<br> 参数一表示List显示区域内第一个子组件的索引值；<br> 参数二表示List显示区域内最后一个子组件的索引值；<br> 参数三表示List显示区域内中间位置子组件的索引值。初始值：{ _, _, _ => }。|

## 基础类型定义

### class OnScrollFrameBeginHandlerResult

```cangjie
public class OnScrollFrameBeginHandlerResult {
    public var offsetRemain: ?Float64
    public init(offsetRemain!: ?Float64)
}
```

**功能：** 滚动帧开始处理结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offsetRemain

```cangjie
public var offsetRemain: ?Float64
```

**功能：** 剩余偏移量。

**类型：** ?Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(?Float64)

```cangjie
public init(offsetRemain!: ?Float64)
```

**功能：** 创建OnScrollFrameBeginHandlerResult对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offsetRemain|?Float64|是|-| **命名参数。** 剩余偏移量。初始值：0.0。|