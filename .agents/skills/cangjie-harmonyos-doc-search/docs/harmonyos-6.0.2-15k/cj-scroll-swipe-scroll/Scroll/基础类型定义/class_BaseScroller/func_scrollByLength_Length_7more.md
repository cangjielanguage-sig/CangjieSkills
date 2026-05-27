#### func scrollBy(Length, Length)

```cangjie
public func scrollBy(xOffset!: Length, yOffset!: Length): Unit
```

**功能：** 滑动指定距离。

> **说明：**
>
> 支持Scroll、List、Grid、WaterFlow组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| xOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  水平方向滚动距离，不支持百分比形式。 |
| yOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  竖直方向滚动距离，不支持百分比形式。 |

#### func scrollEdge(Edge)

```cangjie
public func scrollEdge(edge: Edge): Unit
```

**功能：** 滚动到容器边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| edge| [Edge](./cj-common-types.md#enum-edge) | 是 | \- | 滚动到的边缘位置。 |

#### func scrollEdge(Edge, Float32)

```cangjie
public func scrollEdge(edge: Edge, velocity!: Float32): Unit
```

**功能：** 滚动到容器边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| edge| [Edge](./cj-common-types.md#enum-edge) | 是 | \- | 滚动到的边缘位置。 |
| velocity| Float32 | 是 | \- | **命名参数。**  设置滚动到容器边缘的固定速度。如果设置小于等于0的值，参数不生效。<br>初始值：0.0<br>单位： vp/s。 |

#### func scrollEdge(Edge, Int32)

```cangjie
public func scrollEdge(edge: Edge, velocity!: Int32): Unit
```

**功能：** 滚动到容器边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| edge| [Edge](./cj-common-types.md#enum-edge) | 是 | \- | 滚动到的边缘位置。 |
| velocity| Int32 | 是 | \- | **命名参数。**  设置滚动到容器边缘的固定速度。如果设置小于等于0的值，参数不生效。单位： vp/s。 |

#### func scrollPage(Bool)

```cangjie
public func scrollPage(next: Bool): Unit
```

**功能：** 滚动到下一页或者上一页。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| next | Bool | 是 | \- | 是否向下翻页。true表示向下翻页，false表示向上翻页。 |

#### func scrollPage(Bool, Bool)

```cangjie
public func scrollPage(next: Bool, animation!: Bool): Unit
```

**功能：** 滚动到下一页或者上一页。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| next | Bool | 是 | \- | 是否向下翻页。true表示向下翻页，false表示向上翻页。 |
| animation| Bool | 是 | \- | **命名参数。**  是否开启翻页动画效果。true有动画，false无动画。 |

#### func scrollTo(Length, Length)

```cangjie
public func scrollTo(xOffset!: Length, yOffset!: Length): Unit
```

**功能：** 滑动到指定位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| xOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  水平滚动偏移（Int64、Float64类型值单位为vp）。<br>**说明：**<br>该参数值不支持设置百分比。<br>仅滚动轴为x轴时生效。<br>当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止。 |
| yOffset | [Length](./cj-common-types.md#interface-length) |  是 | \- | **命名参数。**  竖直滚动偏移（Int64、Float64类型值单位为vp）。<br>**说明：**<br>该参数值不支持设置百分比。<br>仅滚动轴为y轴时生效。<br>当值小于0时，不带动画的滚动，按0处理。带动画的滚动，默认滚动到起始位置后停止。|