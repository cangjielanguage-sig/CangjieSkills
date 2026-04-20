# Gauge

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

数据量规图表组件，用于将数据展示为环形图表。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

可以包含子组件。

## 创建组件

### init(?Float32, ?Float32, ?Float32, () -> Unit)

```cangjie
public init(value!: ?Float32, min!: ?Float32 = None, max!: ?Float32 = None, child!: () -> Unit = { => })
```

**功能：** 创建一个数据量规图表组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Float32|是|-| **命名参数。** 初始值: 0.0。 量规图的当前数据值，即图中指针指向位置。用于组件创建时量规图初始值的预置。<br>**说明：**<br>value不在min和max范围内时使用min作为默认值。|
|min|?Float32|否|None| **命名参数。** 初始值: 0.0。 当前数据段最小值。|
|max|?Float32|否|None| **命名参数。** 初始值: 100.0。 当前数据段最大值。<br>**说明：**<br>max小于min时使用默认值0.0和100.0。<br>max和min支持负数。|
|child|()->Unit|否|{ => }| **命名参数。** 声明当前组件的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。