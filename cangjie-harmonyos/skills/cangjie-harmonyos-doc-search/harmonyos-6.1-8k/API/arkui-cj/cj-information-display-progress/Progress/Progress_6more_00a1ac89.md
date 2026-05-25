# Progress

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

进度条组件，用于显示内容加载或操作处理等进度。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?Float64, ?Float64, ?ProgressType)

```cangjie
public init(value!: ?Float64, total!: ?Float64 = None, progressType!: ?ProgressType = None)
```

**功能：** 创建进度条组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|**命名参数。** 指定当前进度值。设置小于0的数值时置为0.0，设置大于total的数值时置为total。初始值：0.0|
|total|?Float64|否|None|**命名参数。** 指定进度总长。设置小于等于0的数值时置为100.0。|
|progressType|?[ProgressType](./cj-common-types.md#enum-progresstype)|否|None|**命名参数。** 指定进度条类型。|

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> 该组件重写了通用属性backgroundColor，直接添加在Progress组件上，生效进度条的底色。如需设置整个Progress组件的背景色，需要在外层容器上添加backgroundColor，容器再包裹Progress组件。

通用事件：全部支持。

## 组件属性

### func color(?ResourceColor)

```cangjie
public func color(value: ?ResourceColor): This
```

**功能：** 设置进度条前景色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|进度条前景色。|

### func style(?Length, ?Int32, ?Length)

```cangjie
public func style(strokeWidth!: ?Length = None, scaleCount!: ?Int32 = None, scaleWidth!: ?Length = None): This
```

**功能：** 设置进度条的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置进度条宽度（不支持百分比设置）。初始值：4.vp。|
|scaleCount|?Int32|否|None|**命名参数。** 设置环形进度条总刻度数。初始值：120。|
|scaleWidth|?[Length](./cj-common-types.md#interface-length)|否|None|**命名参数。** 设置环形进度条刻度粗细（不支持百分比设置），刻度粗细大于进度条宽度时，为系统默认粗细。初始值：2.vp。|

### func style(?RingStyleOptions)

```cangjie
public func style(value: ?RingStyleOptions): This
```

**功能：** 设置进度条Ring的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[RingStyleOptions](#class-ringstyleoptions)|是|-|设置Ring的样式。<br>初始值：RingStyleOptions()。|

### func value(?Float64)

```cangjie
public func value(value: ?Float64): This
```

**功能：** 设置当前进度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float64|是|-|当前进度值。初始值：0.0。|