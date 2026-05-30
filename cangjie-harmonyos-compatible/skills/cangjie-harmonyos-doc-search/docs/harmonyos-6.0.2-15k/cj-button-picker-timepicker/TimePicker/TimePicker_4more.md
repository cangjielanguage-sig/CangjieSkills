# TimePicker

时间选择组件支持根据指定参数创建选择器，可选择小时和分钟。

## 子组件

无

## 创建组件

### init(DateTime, TimePickerFormat)

```cangjie
public init(selected!: DateTime = DateTime.now(), format!: TimePickerFormat = TimePickerFormat.HourMinute)
```

**功能：** 创建滑动选择器，默认使用24小时的时间区间。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|selected|DateTime|否|DateTime.now()|**命名参数。** 选中项的时间。|
|format|[TimePickerFormat](#enum-timepickerformat)|否|TimePickerFormat.HourMinute|**命名参数。** 指定需要显示的TimePicker的格式。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。