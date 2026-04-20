### AnimatorOptions(Int32, String, Int32, AnimatorFill, AnimatorDirection, Int32, Float64, Float64)

```cangjie
public AnimatorOptions(
    public let duration!: Int32 = 0,
    public let easing!: String = "ease",
    public let delay!: Int32 = 0,
    public let fill!: AnimatorFill = None,
    public let direction!: AnimatorDirection = Normal,
    public let iterations!: Int32 = 0,
    public let begin!: Float64 = 0.0,
    public let end!: Float64 = 1.0
)
```

**功能：** 创建动画选项对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Int32|否|0| **命名参数。** 动画播放的时长，单位毫秒。<br>取值范围：[0, +∞)。|
|easing|String|否|"ease"| **命名参数。** 动画插值曲线。<br>"linear"：动画线性变化。<br>"ease"：动画开始和结束时的速度较慢，cubic-bezier(0.25、0.1、0.25、1.0)。<br>"ease-in"：动画播放速度先慢后快，cubic-bezier(0.42, 0.0, 1.0, 1.0)。<br>"ease-out"：动画播放速度先快后慢，cubic-bezier(0.0, 0.0, 0.58, 1.0)。<br>"ease-in-out"：动画播放速度先加速后减速，cubic-bezier(0.42, 0.0, 0.58, 1.0)。<br>"fast-out-slow-in"：标准曲线，cubic-bezier(0.4，0.0，0.2，1.0)。<br>"linear-out-slow-in"：减速曲线，cubic-bezier(0.0，0.0，0.2，1.0)。<br>"fast-out-linear-in"：加速曲线，cubic-bezier(0.4, 0.0, 1.0, 1.0)。<br>"friction"：阻尼曲线，cubic-bezier(0.2, 0.0, 0.2, 1.0)。<br>"extreme-deceleration"：急缓曲线，cubic-bezier(0.0, 0.0, 0.0, 1.0)。<br>"rhythm"：节奏曲线，cubic-bezier(0.7, 0.0, 0.2, 1.0)。<br>"sharp"：锐利曲线，cubic-bezier(0.33, 0.0, 0.67, 1.0)。<br>"smooth"：平滑曲线，cubic-bezier(0.4, 0.0, 0.4, 1.0)。<br>"cubic-bezier(x1,y1,x2,y2)"：三次贝塞尔曲线，x1、x2的值必须处于0-1之间。例如"cubic-bezier(0.42,0.0,0.58,1.0)"。<br>"steps(number,step-position)"：阶梯曲线，number必须设置，为正整数，step-position参数可选，支持设置start或end，默认值为end。例如"steps(3,start)"。<br>"interpolating-spring(velocity,mass,stiffness,damping)"：插值弹簧曲线。velocity、mass、stiffness、damping都是数值类型，且mass、stiffness、damping参数均应该大于0，具体参数含义参考[插值弹簧曲线](./cj-apis-curves.md#static-func-interpolatingspringfloat32-float32-float32-float32)。使用interpolating-spring时，duration不生效，由弹簧参数决定；fill、direction、iterations设置无效，fill固定设置为"forwards"，direction固定设置为"normal"，iterations固定设置为1，且对animator的[reverse](#reverse)函数调用无效。即animator使用interpolating-spring时只能正向播放1次。|
|delay|Int32|否|0| **命名参数。** 动画延时播放时长，单位毫秒，设置为0时，表示不延时。设置为负数时动画提前播放，如果提前播放的时长大于动画总时长，动画直接过渡到终点。|
|fill|[AnimatorFill](#enum-animatorfill)|否|AnimatorFill.None| **命名参数。** 动画执行后是否恢复到初始状态，动画执行后，动画结束时的状态（在最后一个关键帧中定义）将保留。|
|direction|[AnimatorDirection](#enum-animatordirection)|否|AnimatorDirection.Normal| **命名参数。** 动画播放模式。|
|iterations|Int32|否|0| **命名参数。** 动画播放次数。设置为0时不播放，设置为-1时无限次播放,设置大于0时为播放次数。<br />**说明：** <br />设置为除-1外其他负数视为无效取值，无效取值动画默认播放1次。|
|begin|Float64|否|0.0| **命名参数。** 动画插值起点。|
|end|Float64|否|1.0| **命名参数。** 动画插值终点。|