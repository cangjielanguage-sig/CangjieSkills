### func nextMargin(Length, Bool)

```cangjie
public func nextMargin(value: Length, ignoreBlank !: Bool = false): This
```

**功能：** 设置后边距，用于露出后一项的一小部分。仅当Swiper子组件的布局方式为拉伸时生效，主要包括两种场景：1、displayMode属性设置为SwiperDisplayMode.STRETCH；2、displayCount属性设置为Int32类型。

当主轴方向为横向布局时，nextMargin/prevMargin中任意一个大于子组件测算的宽度，nextMargin和prevMargin均不显示。

当主轴方向为纵向布局时，nextMargin/prevMargin中任意一个大于子组件测算的高度，nextMargin和prevMargin均不显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|后边距。不支持设置百分比。<br/>初始值：0。|
|ignoreBlank|Bool|否|false| **命名参数。** 非loop场景下尾页不显示nextMargin。在非loop场景下，设置为true时，尾页不显示空白的nextMargin，尾页的右边缘与Swiper视窗右边缘对齐；设置false时，尾页显示空白nextMargin，尾页的右边缘与Swiper视窗右边缘的距离为nextMargin。<br/>初始值：false。 <br/> **说明：**<br/>尾页场景下，prevMargin和nextMargin的值相加作为左边边距显示前一个页面。|

### func prevMargin(Length, Bool)

```cangjie
public func prevMargin(value: Length, ignoreBlank !: Bool = false): This
```

**功能：** 设置前边距，用于露出前一项的一小部分。仅当Swiper子组件的布局方式为拉伸时生效，主要包括两种场景：1、displayMode属性设置为SwiperDisplayMode.STRETCH；2、displayCount属性设置为Int32类型。

当主轴方向为横向布局时，nextMargin/prevMargin中任意一个大于子组件测算的宽度，nextMargin和prevMargin均不显示。

当主轴方向为纵向布局时，nextMargin/prevMargin中任意一个大于子组件测算的高度，nextMargin和prevMargin均不显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|前边距。不支持设置百分比。<br/>初始值：0。|
|ignoreBlank|Bool|否|false| **命名参数。** 非loop场景下首页不显示prevMargin。在非loop场景下，设置为true时，首页不显示空白的prevMargin，首页的左边缘与Swiper视窗左边缘对齐；设置false时，首页显示空白prevMargin，首页的左边缘与Swiper视窗左边缘的距离为prevMargin。<br/>初始值：false。 <br/> **说明：**<br/>首页场景下，prevMargin和nextMargin的值相加作为右边边距显示后一个页面。|

### func vertical(Bool)

```cangjie
public func vertical(value: Bool): This
```

**功能：** 设置是否纵向滑动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否为纵向滑动。true为纵向滑动，false为横向滑动。<br>初始值：false。|