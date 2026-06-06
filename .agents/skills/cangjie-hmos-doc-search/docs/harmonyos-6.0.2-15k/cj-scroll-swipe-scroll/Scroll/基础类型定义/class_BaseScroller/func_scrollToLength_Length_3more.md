#### func scrollTo(Length, Length, Float64, Curve)

```cangjie
public func scrollTo(xOffset!: Length, yOffset!: Length, duration!: Float64, curve!: Curve): Unit
```

**功能：** 滑动到指定位置，并设置时长和滚动曲线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| xOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  水平滚动偏移（Int64、Float64类型值单位为vp）。<br>**说明：**<br>该参数值不支持设置百分比。<br>仅滚动轴为x轴时生效。<br>当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止。|
| yOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  竖直滚动偏移（Int64、Float64类型值单位为vp）。<br>**说明：**<br>该参数值不支持设置百分比。<br>仅滚动轴为y轴时生效。<br>当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止。|
| duration | Float64 | 是 | \- | **命名参数。**  滚动时长设置。<br>初始值：1000.0<br>**说明：**<br>设置为小于0的值时，按初始值显示。|
| curve | [Curve](./cj-common-types.md#enum-curve) | 是 | \- | **命名参数。**  滚动曲线设置。 <br>初始值：Curve.Ease。|

#### func scrollTo(Length, Length, ScrollAnimationOptions)

```cangjie
public func scrollTo(xOffset!: Length, yOffset!: Length, animation!: ScrollAnimationOptions): Unit
```

**功能：** 滑动到指定位置，并设置时长和滚动曲线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| xOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  水平滚动偏移（Int64、Float64类型值单位为vp）。<br>**说明：**<br>该参数值不支持设置百分比。<br>仅滚动轴为x轴时生效。<br>当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止，可通过设置animation参数，使滚动在越界时启动回弹动画。 |
| yOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  竖直滚动偏移（Int64、Float64类型值单位为vp）。<br>**说明：**<br>该参数值不支持设置百分比。<br>仅滚动轴为y轴时生效。<br>当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止，可通过设置animation参数，使滚动在越界时启动回弹动画。 |
| animation | [ScrollAnimationOptions](#class-scrollanimationoptions) | 是 | \- | **命名参数。**  动画配置，自定义滚动动效。 |

#### func scrollTo(Length, Length, Bool)

```cangjie
public func scrollTo(xOffset!: Length, yOffset!: Length, animation!: Bool): Unit
```

**功能：** 滑动到指定位置，并设置时长和滚动曲线。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| xOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  水平滑动偏移（Int64、Float64类型值单位为vp）。 |
| yOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  竖直滑动偏移（Int64、Float64类型值单位为vp）。 |
| animation | Bool | 是 | \- | **命名参数。**  动画配置，使能默认弹簧动效。<br>初始值：false。|