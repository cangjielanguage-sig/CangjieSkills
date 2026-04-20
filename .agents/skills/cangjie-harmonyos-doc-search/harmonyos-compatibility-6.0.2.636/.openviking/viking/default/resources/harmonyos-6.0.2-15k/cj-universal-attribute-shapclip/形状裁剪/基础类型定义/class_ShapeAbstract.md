### class ShapeAbstract

```cangjie
abstract sealed class ShapeAbstract <: ContainerBase {}
```

**功能：** CircleShape，RectShape，PathShape，EllipseShape的基类，重新定义了fill，height，offset，size，width等相关的公共成员方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**父类型：**

[ContainerBase](./cj-ui-framework.md#class-ContainerBase)

#### func fill(ResourceColor)

```cangjie
public func fill(color: ResourceColor): This
```

**功能：** 设置填充区域颜色。异常值按照初始值处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|填充区颜色。</br>初始值：0xff0000。|

#### func height(Length)

```cangjie
public func height(value: Length): This
```

**功能：** 设置组件自身高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|组件高度。</br>单位：vp。|

#### func offset(Length, Length)

```cangjie
public func offset(x!: Length, y!: Length): This
```

**功能：** 设置相对偏移，组件相对原本的布局位置进行偏移。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** x轴坐标。|
|y|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** y轴坐标。|

#### func size(Length, Length)

```cangjie
  public func size(width!: Length, height!: Length): This
 ```

**功能：** 设置组件的高宽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 组件宽度。</br>单位：vp。|
|height|[Length](./cj-common-types.md#interface-length)|是|-| **命名参数。** 组件高度。</br>单位：vp。|

#### func width(Length)

```cangjie
public func width(value: Length): This
```

**功能：** 设置组件自身的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|组件宽度。</br>单位：vp。|