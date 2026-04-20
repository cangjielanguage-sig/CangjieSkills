## 组件事件

### func onDateChange(?Callback\<DateTime,Unit>)

```cangjie
public func onDateChange(callback: ?Callback<DateTime, Unit>): This
```

**功能：** 选择日期时触发该事件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

| 参数名      | 类型                                                                                                                                       | 必填  | 默认值 | 说明                                      |
|:-------- |:---------------------------------------------------------------------------------------------------------------------------------------- |:--- |:--- |:--------------------------------------- |
| callback | ?[Callback](./cj-common-types.md#type-callbackt-v)\<[DateTime](../ImageKit/cj-apis-image.md#datetime),Unit> | 是   | -   | 返回选中的时间，年月日为选中的日期，时分取决于当前系统时间的时分，秒恒为00。<br>初始值: { _ => } |

## 基础类型定义

### class DatePickerResult

```cangjie
public class DatePickerResult {
    public var year: Int64
    public var month: Int64
    public var day: Int64
    public init(
        year: Int64,
        month: Int64,
        day: Int64
    )
}
```

**功能：** 记录日期选择器弹窗的选择结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var year

```cangjie
public var year: Int64
```

**功能：** 选中日期的年。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var month

```cangjie
public var month: Int64
```

**功能：** 选中日期的月。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var day

```cangjie
public var day: Int64
```

**功能：** 选中日期的日。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(Int64, Int64, Int64)

```cangjie
public init(
    year: Int64,
    month: Int64,
    day: Int64
)
```

**功能：** 记录日期选择器弹窗的选择结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

| 参数名   | 类型    | 必填  | 默认值 | 说明                           |
|:----- |:----- |:--- |:--- |:---------------------------- |
| year  | Int64 | 是   | -   | 选中日期的年。                      |
| month | Int64 | 是   | -   | 选中日期的月。(0~11)，0表示1月，11表示12月。 |
| day   | Int64 | 是   | -   | 选中日期的日。                      |