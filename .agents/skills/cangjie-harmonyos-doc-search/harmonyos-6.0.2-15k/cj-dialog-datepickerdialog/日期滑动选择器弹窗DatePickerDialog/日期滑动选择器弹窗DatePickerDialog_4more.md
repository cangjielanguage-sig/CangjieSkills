# 日期滑动选择器弹窗（DatePickerDialog）

根据指定的日期范围创建日期滑动选择器，展示在弹窗上。

## 子组件

无

## 通用属性/通用事件

通用属性：不支持。

通用事件：不支持。

## 组件属性

### static func show(?DatePickerDialogOptions)

```cangjie
public static func show(options!: ?DatePickerDialogOptions = None): Unit
```

**功能：** 定义日期滑动选择器弹窗并弹出。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|?[DatePickerDialogOptions](#class-datepickerdialogoptions)|否|None| **命名参数。** 配置日期选择器弹窗的参数。|