# Marquee

跑马灯组件，用于滚动展示一段单行文本。仅当文本内容宽度超过跑马灯组件宽度时滚动，不超过时不滚动。

> **说明：**
>
> 为了不影响滚动帧率，建议在滚动类组件中Marquee的个数不超过4个，或者使用[Text](./cj-text-input-text.md)组件的[TextOverflow.MARQUEE](./cj-common-types.md#enum-textoverflow)替代。

## 子组件

无

## 创建组件

### init(Bool, String, Float64, Int32, Bool)

```cangjie
public init(
    start!: Bool,
    src!: String,
    step!: Float64 = 6.0,
    loop!: Int32 = -1,
    fromStart!: Bool = true
)
```

**功能：** 创建跑马灯组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Bool|是|-| **命名参数。** 控制跑马灯是否进入播放状态。<br>有限的滚动次数播放完毕后，不可以通过改变start重置滚动次数重新开始播放。|
|src|String|是|-| **命名参数。** 需要滚动的文本。|
|step|Float64|否|6.0| **命名参数。** 滚动动画文本滚动步长，当step大于Marquee的文本宽度时，取默认值。|
|loop|Int32|否|-1| **命名参数。** 设置重复滚动的次数，小于等于零时无限循环。|
|fromStart|Bool|否|true| **命名参数。** 设置文本从头开始滚动或反向滚动。|

### init(Bool, String, Int64, Int32, Bool)

```cangjie
public init(
    start!: Bool,
    src!: String,
    step!: Int64,
    loop!: Int32 = -1,
    fromStart!: Bool = true
)
```

**功能：** 创建跑马灯组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|start|Bool|是|-| **命名参数。** 控制跑马灯是否进入播放状态。<br>有限的滚动次数播放完毕后，不可以通过改变start重置滚动次数重新开始播放。|
|src|String|是|-| **命名参数。** 需要滚动的文本。|
|step|Int64|是|-| **命名参数。** 滚动动画文本滚动步长。|
|loop|Int32|否|-1| **命名参数。** 设置重复滚动的次数，小于等于零时无限循环。|
|fromStart|Bool|否|true| **命名参数。** 设置文本从头开始滚动或反向滚动。|

## 通用属性/通用事件

通用属性：全部支持

通用事件：不支持