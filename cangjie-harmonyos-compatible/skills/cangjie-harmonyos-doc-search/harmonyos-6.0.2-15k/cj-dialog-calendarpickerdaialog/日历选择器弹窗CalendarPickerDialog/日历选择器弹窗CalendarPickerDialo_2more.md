# 日历选择器弹窗（CalendarPickerDialog）

点击日期弹出日历选择器弹窗，可选择弹窗内任意日期。

## class CalendarPickerDialog

```cangjie
public class CalendarPickerDialog {}
```

**功能：** 构造一个CalendarPickerDialog类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### static func show(?CalendarDialogOptions)

```cangjie
public static func show(options!: ?CalendarDialogOptions = None): Unit
```

**功能：** 定义日历选择器弹窗并弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|?[CalendarDialogOptions](#class-calendardialogoptions)|否|None| **命名参数。** 配置日历选择器弹窗的参数。|