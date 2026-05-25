## class PageTransitionOptions

```cangjie
public class PageTransitionOptions {
    public PageTransitionOptions(
        public var `type`!: RouteType = RouteType.None,
        public var duration!: Int32 = 1000,
        public var curve!: Curve = Curve.Linear,
        public var delay!: Int32 = 0
    )
}
```

**功能：** 页面转场配置参数类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var curve

```cangjie
public var curve: Curve
```

**功能：** 设置动画曲线。

**类型：** [Curve](./cj-common-types.md#enum-curve)

**读写能力：** 可读写

**起始版本：** 12

### var delay

```cangjie
public var delay: Int32
```

**功能：** 设置动画延迟时长。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var duration

```cangjie
public var duration: Int32
```

**功能：** 设置动画的时长。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 12

### var \`type\`

```cangjie
public var `type`: RouteType
```

**功能：** 设置页面转场效果生效的路由类型。

**类型：** [RouteType](#enum-routetype)

**读写能力：** 可读写

**起始版本：** 12

### PageTransitionOptions(RouteType, Int32, Curve, Int32)

```cangjie
public PageTransitionOptions(
    public var `type`!: RouteType = RouteType.None,
    public var duration!: Int32 = 1000,
    public var curve!: Curve = Curve.Linear,
    public var delay!: Int32 = 0
)
```

**功能：** 构造一个PageTransitionOptionsl类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[RouteType](#enum-routetype)|否|RouteType.None| **命名参数。** 页面转场效果生效的路由类型。|
|duration|Int32|否|1000| **命名参数。** 动画的时长。<br>单位：毫秒。<br>取值范围：[0, +∞)。|
|curve|[Curve](./cj-common-types.md#enum-curve)|否|Curve.Linear| **命名参数。** 动画曲线。|
|delay|Int32|否|0| **命名参数。** 动画延迟时长。<br>单位：毫秒。<br>**说明：**<br>没有匹配时使用系统默认的页面转场效果(根据设备可能会有差异)，如需禁用系统默认页面转场效果，可以指定duration为0。|