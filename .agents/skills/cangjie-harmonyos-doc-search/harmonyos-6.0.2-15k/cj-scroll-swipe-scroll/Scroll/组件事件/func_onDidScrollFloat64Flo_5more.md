### func onDidScroll((Float64,Float64,ScrollState) -> Unit)

```cangjie
public func onDidScroll(callback: (Float64, Float64, ScrollState) -> Unit): This
```

**功能：** 滚动事件回调，Scroll滚动时触发。

返回当前帧滚动的偏移量和当前滚动状态。

触发该事件的条件 ：

1. 滚动组件触发滚动时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用。

3. 越界回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(Float64,Float64,[ScrollState](./cj-common-types.md#enum-scrollstate))->Unit|是|-|回调函数，Scroll滚动时触发。<br>参数一：每帧滚动时水平方向的偏移量，Scroll中的内容向左滚动时偏移量为正，向右滚动时偏移量为负。单位vp。<br>参数二：每帧滚动时竖直方向的偏移量，Scroll中的内容向上滚动时偏移量为正，向下滚动时偏移量为负。单位vp。<br>参数三：当前滚动状态。|

### func onReachEnd(() -> Unit)

```cangjie
public func onReachEnd(callback: () -> Unit): This
```

**功能：** 滚动组件到达末尾位置时触发该事件。滚动组件边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动组件到达末尾位置时触发。|

### func onReachStart(() -> Unit)

```cangjie
public func onReachStart(callback: () -> Unit): This
```

**功能：** 滚动组件到达起始位置时触发该事件。 滚动组件初始化时会触发一次，滚动到起始位置时触发一次。边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|()->Unit|是|-|回调函数，滚动组件到达起始位置时触发。|

### func onScroll((OffsetResult) -> Unit)<sup>deprecated</sup>

```cangjie
public func onScroll(callback: (OffsetResult) -> Unit): This
```

**功能：** 滚动时触发该事件。

触发该事件的条件 ：

1. 滚动组件触发滚动时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用。

3. 越界回弹。

该事件已废弃，可使用onWillScroll事件替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([OffsetResult](#struct-offsetresult))->Unit|是|-|回调函数，Scroll滚动时触发。<br>参数：每帧滚动时水平、竖直方向的偏移量。<br>**说明：**<br>对于水平方向偏移量，Scroll的内容向左滚动时偏移量为正，向右滚动时偏移量为负。对于竖直方向偏移量，Scroll的内容向上滚动时偏移量为正，向下滚动时偏移量为负。<br>单位vp。|

### func onScrollEdge((Edge) -> Unit)

```cangjie
public func onScrollEdge(callback: (Edge) -> Unit): This
```

**功能：** 滚动到边缘时触发该事件。

触发该事件的条件 ：

1. 滚动组件滚动到边缘时触发，支持键鼠操作和其他触发滚动的输入设置。

2. 通过滚动控制器API接口调用。

3. 越界回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|([Edge](./cj-common-types.md#enum-edge))->Unit|是|-|回调函数，滚动到边缘时触发。<br>参数：滚动到的边缘位置。|