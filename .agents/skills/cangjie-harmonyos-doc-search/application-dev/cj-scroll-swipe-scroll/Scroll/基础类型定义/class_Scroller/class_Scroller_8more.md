### class Scroller

```cangjie
public class Scroller {
    public init()
}
```

**功能：** 定义可滚动容器组件的控制器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init()

```cangjie
public init()
```

**功能：** 构造函数，用于创建一个Scroller对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### func scrollTo(Length, Length)

```cangjie
public func scrollTo(xOffset!: Length, yOffset!: Length): Unit
```

**功能：** 设置滑动到指定位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 水平滚动偏移。|
|yOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 垂直滚动偏移。|

#### func scrollTo(Length, Length, ?ScrollAnimationOptions)

```cangjie
public func scrollTo(xOffset!: Length, yOffset!: Length, animation!: ?ScrollAnimationOptions): Unit
```

**功能：** 设置滑动到指定位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 水平滚动偏移。|
|yOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 垂直滚动偏移。|
|animation|?ScrollAnimationOptions|是|-|**命名参数。** 滚动动画选项。初始值：ScrollAnimationOptions()。|

#### func scrollTo(Length, Length, ?Bool)

```cangjie
public func scrollTo(xOffset!: Length, yOffset!: Length, animation!: ?Bool): Unit
```

**功能：** 设置滑动到指定位置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 水平滚动偏移。|
|yOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 垂直滚动偏移。|
|animation|?Bool|是|-|**命名参数。** 是否启用动画。初始值：false。|

#### func scrollBy(Length, Length)

```cangjie
public func scrollBy(xOffset!: Length, yOffset!: Length): Unit
```

**功能：** 按偏移量滚动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|xOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 水平滚动偏移。|
|yOffset|[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 垂直滚动偏移。|

#### func scrollEdge(Edge)

```cangjie
public func scrollEdge(value: Edge): Unit
```

**功能：** 滚动到容器边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Edge](./cj-common-types.md#enum-edge)|是|-|滚动到的边缘位置。|

#### func scrollEdge(Edge, ?ScrollEdgeOptions)

```cangjie
public func scrollEdge(value: Edge, options: ?ScrollEdgeOptions): Unit
```

**功能：** 滚动到容器边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Edge](./cj-common-types.md#enum-edge)|是|-|滚动到的边缘位置。|
|options|?[ScrollEdgeOptions](#class-scrolledgeoptions)|是|-|滚动边缘选项。初始值：ScrollEdgeOptions()。|