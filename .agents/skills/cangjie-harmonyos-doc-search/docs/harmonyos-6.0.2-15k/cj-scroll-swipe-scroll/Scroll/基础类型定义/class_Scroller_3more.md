### class Scroller

```cangjie
public class Scroller <: BaseScroller {
    public init()
}
```

**功能：** 可滚动容器组件的控制器，可以将此组件绑定至容器组件，然后通过它控制容器组件的滚动，同一个控制器不可以控制多个容器组件，目前支持绑定到List、Scroll、ScrollBar、Grid、WaterFlow上。

> **说明：**
>
> 1、Scroller控制器与滚动容器组件的绑定发生在组件创建阶段。
>
> 2、Scroller控制器与滚动容器组件绑定后才可以正常调用Scroller方法，否则根据调用接口不同会不生效或者抛异常。
>
> 3、以[aboutToAppear](./cj-custom-component-lifecycle.md#func-abouttoappear)为例，aboutToAppear在创建自定义组件的新实例后，在执行其build()方法之前执行。因此如果滚动组件在自定义组件build内，在该自定义组件aboutToAppear执行时，内部滚动组件还没有创建，是不能正常调用上述Scroller方法的。
>
> 4、以[onAppear](./cj-universal-event-appear.md#func-onappear---unit)为例，组件挂载显示后触发此回调。因此在滚动组件的onAppear回调执行时，滚动组件已经创建并已经和Scroller绑定成功，是可以正常调用Scroller方法的。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

- [BaseScroller](#class-basescroller)

#### init()

```cangjie
public init()
```

**功能：** 构造一个Scroller对象。

**起始版本：** 12

### struct OffsetResult

```cangjie
public struct OffsetResult {
    public OffsetResult(
        public let xOffset: Float64,
        public let yOffset: Float64
    )
}
```

**功能：** 滑动偏移量对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let xOffset

```cangjie
public let xOffset: Float64
```

**功能：** 水平滑动偏移。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

#### let yOffset

```cangjie
public let yOffset: Float64
```

**功能：** 竖直滑动偏移。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 19

#### OffsetResult(Float64, Float64)

```cangjie
public OffsetResult(
    public let xOffset: Float64,
    public let yOffset: Float64
)
```

**功能：** 构造一个OffsetResult对象。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xOffset|Float64|是|-|水平滑动偏移。单位为vp。|
|yOffset|Float64|是|-|竖直滑动偏移。单位为vp。|

### enum ScrollAlign

```cangjie
public enum ScrollAlign {
    | START
    | CENTER
    | END
    | AUTO
    | NONE
}
```

**功能：** 对齐方式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### AUTO

```cangjie
AUTO
```

**功能：** 自动对齐。

若指定item完全处于显示区，不做调整。否则依照滑动距离最短的原则，将指定item首部对齐或尾部对齐于List，使指定item完全处于显示区。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### CENTER

```cangjie
CENTER
```

**功能：** 居中对齐。指定item主轴方向居中对齐于List。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### END

```cangjie
END
```

**功能：** 尾部对齐。指定item尾部与List尾部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### NONE

```cangjie
NONE
```

**功能：** 不进行对齐操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### START

```cangjie
START
```

**功能：** 首部对齐。指定item首部与List首部对齐。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12