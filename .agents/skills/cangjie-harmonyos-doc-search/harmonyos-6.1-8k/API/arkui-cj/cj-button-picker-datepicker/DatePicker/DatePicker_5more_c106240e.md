# DatePicker

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

日期选择器组件，用于根据指定日期范围创建日期滑动选择器。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?DateTime, ?DateTime, ?DateTime)

```cangjie
public init(
    start!: ?DateTime = None,
    end!: ?DateTime = None,
    selected!: ?DateTime = None
)
```

**功能：**  根据指定范围的DateTime创建可以选择日期的滑动选择器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

| 参数名      | 类型       | 必填  | 默认值                                                          | 说明                    |
|:-------- |:-------- |:--- |:------------------------------------------------------------ |:--------------------- |
| start    | ?[DateTime](../ImageKit/cj-apis-image.md#datetime) | 否   | None | **命名参数。** 指定选择器的起始日期。<br>初始值: DateTime.of(year: 1970, month: Month.of(1), dayOfMonth: 1)。|
| end      | ?[DateTime](../ImageKit/cj-apis-image.md#datetime) | 否   | None | **命名参数。** 指定选择器的结束日期。<br>初始值: DateTime.of(year: 2100, month: Month.of(12), dayOfMonth: 31)。|
| selected | ?[DateTime](../ImageKit/cj-apis-image.md#datetime) | 否   | None | **命名参数。** 设置选中项的日期。<br>初始值: DateTime.now()。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。