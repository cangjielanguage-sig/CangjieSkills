# DataPanel

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

数据面板组件，用于将多个数据占比情况使用占比图进行展示。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(Array\<Float64>, ?Float64, ?DataPanelType)

```cangjie
public init(values!: Array<Float64>, max!: ?Float64 = None, panelType!: ?DataPanelType = None)
```

**功能：** 创建一个数据面板组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|values|Array\<Float64>|是|-|**命名参数。** 数据值列表，最多包含9个数据，大于9个数据则取前9个数据。若数据值小于0则置为0。|
|max|?Float64|否|None|**命名参数。** 初始值: 100.0 \- max大于0，表示数据的最大值。 <br> \- max小于等于0，max等于value数组各项的和，按比例显示。|
|panelType|?[DataPanelType](./cj-common-types.md#enum-datapaneltype)|否|None|**命名参数。** 初始值: DataPanelType.Circle 数据面板的类型（不支持动态修改）。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。