### class SwiperAnimationEvent

```cangjie
public class SwiperAnimationEvent {
    public SwiperAnimationEvent(
        public var currentOffset: Float64,
        public var targetOffset: Float64,
        public var velocity: Float64
    )
}
```

**功能：** Swiper组件动画相关信息集合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var currentOffset

```cangjie
public var currentOffset: Float64
```

**功能：** Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。单位vp，初始值为0.0。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### var targetOffset

```cangjie
public var targetOffset: Float64
```

**功能：** Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。单位vp，初始值为0.0。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### var velocity

```cangjie
public var velocity: Float64
```

**功能：** Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。单位vp，初始值为0.0。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

#### SwiperAnimationEvent(Float64, Float64, Float64)

```cangjie
public SwiperAnimationEvent(
    public var currentOffset: Float64,
    public var targetOffset: Float64,
    public var velocity: Float64
)
```

**功能：** SwiperAnimationEvent的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|currentOffset|Float64|是|-|Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。单位vp，初始值为0.0。|
|targetOffset|Float64|是|-|Swiper动画目标元素在主轴方向上，相对于Swiper起始位置的位移。单位vp，初始值为0.0。|
|velocity|Float64|是|-|Swiper离手动画开始时的离手速度。单位vp/s，初始值为0.0。|

### class SwiperAutoFill

```cangjie
public class SwiperAutoFill {
    public var minSize: Length
    public init(minSize: Float64)
    public init(minSize: Int64)
}
```

**功能：** 自适应属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var minSize

```cangjie
public var minSize: Length
```

**功能：** 设置元素显示最小宽度。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(Float64)

```cangjie
public init(minSize: Float64)
```

**功能：** SwiperAutoFill的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minSize|Float64|是|-|设置元素显示最小宽度。<br>初始值：0.0。|

#### init(Int64)

```cangjie
public init(minSize: Int64)
```

**功能：** SwiperAutoFill的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minSize|Int64|是|-|设置元素显示最小宽度。<br>初始值：0。|