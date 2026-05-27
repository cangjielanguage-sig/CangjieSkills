# Progress

进度条组件，用于显示内容加载或操作处理等进度。

## 子组件

无

## 创建组件

### init(ProgressOptions)

```cangjie
public init(option: ProgressOptions)
```

**功能：** 创建进度条组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|option|[ProgressOptions](#class-progressoptions)|是|-|按进度条类型不同，设置不同属性的进度条组件参数。|

### init(Float64, Float64, ProgressType)

```cangjie
public init(value!: Float64, total!: Float64 = 100.0, `type`!: ProgressType = ProgressType.Linear)
```

**功能：** 创建进度条组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-| **命名参数。** 指定当前进度值。设置小于0的数值时置为0.0，设置大于total的数值时置为total。<br/>初始值：0.0|
|total|Float64|否|100.0| **命名参数。** 指定进度总长。设置小于等于0的数值时置为100.0。|
|\`type\`|[ProgressType](./cj-common-types.md#enum-progresstype)|否|ProgressType.Linear|指定进度条类型。|

## 通用属性/通用事件

通用属性：全部支持。

> **说明：**
>
> 该组件重写了通用属性backgroundColor，直接添加在Progress组件上，生效进度条的底色。如需设置整个Progress组件的背景色，需要在外层容器上添加backgroundColor，容器再包裹Progress组件。

通用事件：全部支持。