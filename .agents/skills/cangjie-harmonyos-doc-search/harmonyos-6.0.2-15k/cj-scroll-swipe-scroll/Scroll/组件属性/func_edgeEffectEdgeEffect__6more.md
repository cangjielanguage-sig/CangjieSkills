### func edgeEffect(EdgeEffect, EdgeEffectOptions)

```cangjie
public func edgeEffect(value: EdgeEffect, options: EdgeEffectOptions): This
```

**功能：** 设置边缘滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EdgeEffect](cj-common-types.md#enum-edgeeffect)|是|-|Scroll组件的边缘滑动效果，支持弹簧效果和阴影效果。<br>初始值：EdgeEffect.None。|
|options|[EdgeEffectOptions](./cj-scroll-swipe-common.md#class-edgeeffectoptions)|是|-|组件内容大小小于组件自身时，是否开启滑动效果。alwaysEnabled设置为true会开启滑动效果，alwaysEnabled设置为false不开启。<br>初始值：alwaysEnabled参数初始为true。|

### func edgeEffect(EdgeEffect, Bool)

```cangjie
public func edgeEffect(edgeEffect: EdgeEffect, alwaysEnabled!: Bool = true): This
```

**功能：** 设置边缘滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|edgeEffect|[EdgeEffect](cj-common-types.md#enum-edgeeffect)|是|-|Scroll组件的边缘滑动效果，支持弹簧效果和阴影效果。<br>初始值：EdgeEffect.None。|
|alwaysEnabled|Bool|否|true| **命名参数。** 组件内容大小小于组件自身时，是否开启滑动效果。设置为true开启滑动效果，设置为false则不开启。|

### func enablePaging(Bool)

```cangjie
public func enablePaging(value: Bool): This
```

**功能：** 设置是否支持划动翻页。如果同时设置了划动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效，enablePaging不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否支持划动翻页。设置为true支持滑动翻页，false不支持。<br>初始值：false。|

### func enableScrollInteraction(Bool)

```cangjie
public func enableScrollInteraction(value: Bool): This
```

**功能：** 设置是否支持滚动手势，当设置为false时，无法通过手指或者鼠标滚动，但不影响控制器的滚动接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否支持滚动手势。初始值：true。|

### func friction(Float64)

```cangjie
public func friction(value: Float64): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|摩擦系数。非可穿戴设备初始值为0.75，可穿戴设备初始值为0.9。<br>取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|

### func friction(AppResource)

```cangjie
public func friction(value: AppResource): This
```

**功能：** 设置摩擦系数，手动划动滚动区域时生效，只对惯性滚动过程有影响，对惯性滚动过程中的链式效果有间接影响。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|摩擦系数。非可穿戴设备初始值为0.75，可穿戴设备初始值为0.9。<br>取值范围：(0, +∞)，设置为小于等于0的值时，按初始值处理。|