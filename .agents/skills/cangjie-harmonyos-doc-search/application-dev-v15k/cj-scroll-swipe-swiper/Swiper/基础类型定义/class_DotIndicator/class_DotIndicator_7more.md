### class DotIndicator

```cangjie
public class DotIndicator <: Indicator {
    public init()
}
```

**功能：** DotIndicator的构造函数。

> **说明：**
>
>按压导航点时，导航点会放大至1.33倍显示，因此非按压态时导航点的可见范围边界至实际范围边界存在一定距离，该距离会随着itemWidth、itemHeight、selectedItemWidth、selectedItemHeight等参数变大而变大。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [Indicator](#class-indicator)

#### init()

```cangjie
public init()
```

**功能：** DigitIndicator的构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### func color(ResourceColor)

```cangjie
public func color(value: ResourceColor): This
```

**功能：** Swiper组件圆点导航指示器的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置Swiper组件圆点导航指示器的颜色。<br>初始值：0x182431（10%透明度）。|

#### func itemHeight(Length)

```cangjie
public func itemHeight(value: Length): This
```

**功能：** Swiper组件圆点导航指示器的高，不支持设置百分比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|设置Swiper组件圆点导航指示器的高，不支持设置百分比。<br>初始值：6。<br>单位：vp。|

#### func itemWidth(Length)

```cangjie
public func itemWidth(value: Length): This
```

**功能：** Swiper组件圆点导航指示器的宽，不支持设置百分比。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|设置Swiper组件圆点导航指示器的宽，不支持设置百分比。<br>初始值：6。<br>单位：vp。|

#### func mask(Bool)

```cangjie
public func mask(value: Bool): This
```

**功能：** 是否显示Swiper组件圆点导航指示器的蒙版样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|设置是否显示Swiper组件圆点导航指示器的蒙版样式。<br>初始值：false。|

#### func maxDisplayCount(UInt32)

```cangjie
public func maxDisplayCount(value: UInt32): This
```

**功能：** 圆点导航点指示器样式下，导航点显示个数最大值。

单独导航点组件在没有和Swiper绑定使用时，该属性不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|UInt32|是|-|设置圆点导航点指示器样式下，导航点显示个数最大值，当实际导航点个数大于最大导航点个数时，会生效超长效果样式，样式如示例4所示。<br>初始值：这个属性没有初始值，如果设置异常值那等同于没有超长显示效果。<br>取值范围：6-9。<br> **说明：**<br>1、超长显示场景，目前暂时不支持交互功能（包括：手指点击拖拽、鼠标操作等）。<br>2、在超长显示场景下，中间页面对应的选中导航点的位置，并不是完全固定的，取决于之前的翻页操作序列。<br>3、当前仅支持displayCount为1的场景。|