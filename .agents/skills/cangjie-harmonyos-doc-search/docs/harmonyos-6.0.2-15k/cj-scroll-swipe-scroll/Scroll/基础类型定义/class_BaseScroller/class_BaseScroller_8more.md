### class BaseScroller

```cangjie
sealed abstract class BaseScroller {
    public init(id: Int64)
}
```

**功能：** Scroller的基类，提供内容滚动功能。不支持开发者直接继承该基类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(Int64)

```cangjie
public init(id: Int64)
```

**功能：** 框架内部对象管理相关构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### func currentOffset()

```cangjie
public func currentOffset(): OffsetResult
```

**功能：** 获取当前的滚动偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[OffsetResult](#struct-offsetresult)|返回当前的滚动偏移量。<br>**说明：**<br>当scroller控制器未绑定容器组件或者容器组件被异常释放时，currentOffset的返回值为空。|

#### func fling(Float64)

```cangjie
public func fling(velocity: Float64): Unit
```

**功能：** 滚动类组件开启按传入的初始速度进行惯性滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| velocity| Float64 | 是 | \- | 惯性滚动的初始速度值。单位：vp/s。<br/>**说明：** <br/>velocity值设置为0.0，视为异常值，本次滚动不生效。如果值为正数，则向顶部滚动；如果值为负数，则向底部滚动。 |

#### func fling(Int64)

```cangjie
public func fling(velocity: Int64): Unit
```

**功能：** 滚动类组件开启按传入的初始速度进行惯性滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| velocity| Int64 | 是 | \- | 惯性滚动的初始速度值。单位：vp/s。<br/>**说明：** <br/>velocity值设置为0，视为异常值，本次滚动不生效。如果值为正数，则向下滚动；如果值为负数，则向上滚动。 |

#### func getItemIndex(Length, Length)

```cangjie
public func getItemIndex(x: Length, y: Length): Int32
```

**功能：** 通过坐标获取子组件的索引。

> **说明：**
>
> 支持List、Grid、WaterFlow组件。
> 非法值返回的索引为-1

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
| x | [Length](./cj-common-types.md#interface-length) |  是 | \- | x轴坐标，单位为vp。 |
| y | [Length](./cj-common-types.md#interface-length) |  是 | \- | y轴坐标，单位为vp。 |

#### func getItemRect(Int32)

```cangjie
public func getItemRect(index: Int32): RectResult
```

**功能：** 获取子组件的大小及相对容器组件的位置。

> **说明：**
>
> 支持Scroll、List、Grid、WaterFlow组件。
>
> - index必须是当前显示区域显示的子组件的索引值，否则视为非法值。
> - 非法值返回的大小和位置均为0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- |:--- |
| index | Int32 | 是 | \- | 子组件的索引值。 |

**返回值：**

|类型|说明|
|:----|:----|
| [RectResult](./cj-common-types.md#class-rectresult) | 子组件的大小和相对于组件的位置。单位：vp。|

#### func isAtEnd()

```cangjie
public func isAtEnd(): Bool
```

**功能：** 查询组件是否滚动到底部。

> **说明：**
>
> 支持Scroll、List、Grid、WaterFlow组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
| Bool | true表示组件已经滚动到底部，false表示组件还没滚动到底部。|