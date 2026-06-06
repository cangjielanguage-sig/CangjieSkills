### class TabsAnimationEvent

```cangjie
public class TabsAnimationEvent {
    public TabsAnimationEvent(
        public let currentOffset!: Float32,
        public let targetOffset!: Float32,
        public let velocity!: Float32)
}
```

**功能：** Tabs组件动画相关信息集合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let currentOffset

```cangjie
public let currentOffset: Float32
```

**功能：** Tabs当前显示元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，初始值为0。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

#### let targetOffset

```cangjie
public let targetOffset: Float32
```

**功能：** Tabs动画目标元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，初始值为0。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

#### let velocity

```cangjie
public let velocity: Float32
```

**功能：** Tabs离手动画开始时的离手速度。单位vp/s，初始值为0。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

#### TabsAnimationEvent(Float32, Float32, Float32)

```cangjie
public TabsAnimationEvent(
    public let currentOffset!: Float32,
    public let targetOffset!: Float32,
    public let velocity!: Float32)
```

**功能：** 构造一个TabsAnimationEvent对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|currentOffset|Float32|是|-| **命名参数。** Tabs当前显示元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，初始值为0。|
|targetOffset|Float32|是|-| **命名参数。** Tabs动画目标元素在主轴方向上，相对于Tabs起始位置的位移。单位vp，初始值为0。|
|velocity|Float32|是|-| **命名参数。** Tabs离手动画开始时的离手速度。单位vp/s，初始值为0。|

### enum AnimationMode

```cangjie
public enum AnimationMode {
    | CONTENT_FIRST
    | ACTION_FIRST
    | NO_ANIMATION
}
```

**功能：** 点击TabBar页签时切换TabContent的动画形式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ACTION_FIRST

```cangjie
ACTION_FIRST
```

**功能：** 先开始切换动画，再加载目标页内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CONTENT_FIRST

```cangjie
CONTENT_FIRST
```

**功能：** 先加载目标页内容，再开始切换动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NO_ANIMATION

```cangjie
NO_ANIMATION
```

**功能：** 关闭默认动画。调用TabsController的changeIndex接口切换TabContent时该枚举值不生效。可以通过设置animationDuration为0实现调用TabsController的changeIndex接口时不带动画。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19