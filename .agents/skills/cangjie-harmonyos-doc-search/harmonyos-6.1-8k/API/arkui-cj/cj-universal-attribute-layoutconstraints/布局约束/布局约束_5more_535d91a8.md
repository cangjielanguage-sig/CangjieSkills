# 布局约束

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

通过约束组件的尺寸、对齐方式等来控制组件在布局中的表现。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func constraintSize(?Length, ?Length, ?Length, ?Length)

```cangjie
func constraintSize(minWidth!: ?Length, maxWidth!: ?Length, minHeight!: ?Length, maxHeight!: ?Length ): T
```

**功能：** 设置组件约束尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|minWidth|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 组件最小宽度 <br>初始值: 0.vp。|
|maxWidth|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 组件最大宽度 <br>初始值: (Float64.Inf).vp。|
|minHeight|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 组件最小高度 <br>初始值: 0.vp。|
|maxHeight|?[Length](./cj-common-types.md#interface-length)|是|-|**命名参数。** 组件最大高度 <br>初始值: (Float64.Inf).vp。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func align(?Alignment)

```cangjie
func align(value: ?Alignment): T
```

**功能：** 设置组件在父容器中的对齐方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Alignment](cj-common-types.md#enum-alignment)|是|-|设置容器元素绘制区域内的子元素的对齐方式。<br>只在[Stack](cj-row-column-stack-stack.md)、[Shape](cj-graphic-drawing-shape.md)、[Button](cj-button-picker-button.md)、[StepperItem](cj-navigation-switching-stepperitem.md)、[Text](cj-text-input-text.md)、[TextArea](cj-text-input-textarea.md)、[TextInput](cj-text-input-textinput.md)、[RichEditor](cj-text-input-richeditor.md)、[ListItem](cj-scroll-swipe-listitem.md)、[GridItem](cj-scroll-swipe-griditem.md)、[Scroll](cj-scroll-swipe-scroll.md)、[LoadingProgress](cj-information-display-loadingprogress.md)、[PatternLock](cj-information-display-patternlock.md)、[Progress](cj-information-display-progress.md)、[QRCode](cj-information-display-qrcode.md)、[TextClock](cj-information-display-textclock.md)、[TextTimer](cj-information-display-texttimer.md)、[MenuItem](cj-menu-menuitem.md)、[Toggle](cj-button-picker-toggle.md)、[Checkbox](cj-button-picker-checkbox.md)中生效，其中和文本相关的组件[Text](cj-text-input-text.md)、[TextArea](cj-text-input-textarea.md)、[TextInput](cj-text-input-textinput.md)、[RichEditor](cj-text-input-richeditor.md)的align结果参考[textAlign](cj-text-input-text.md#func-textaligntextalign)。<br>不支持textAlign属性的组件则无法设置水平方向的文字对齐。<br>初始值：Alignment.Center。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func direction(?Direction)

```cangjie
func direction(value: ?Direction): T
```

**功能：** 设置组件的布局方向。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[Direction](./cj-common-types.md#enum-direction)|是|-|布局方向<br>初始值：Direction.Auto。|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|