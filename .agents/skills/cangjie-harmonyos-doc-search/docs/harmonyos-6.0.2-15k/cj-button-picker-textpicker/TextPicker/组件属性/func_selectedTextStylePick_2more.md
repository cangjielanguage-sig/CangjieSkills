### func selectedTextStyle(PickerTextStyle)

```cangjie
public func selectedTextStyle(value: PickerTextStyle): This
```

**功能：** 设置选中项的文本颜色、字号、字体粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[PickerTextStyle](./cj-button-picker-datepicker.md#class-PickerTextStyle)|是|-|选中项的文本颜色、字号、字体粗细。<br/>初始值：PickerTextStyle(0xff007dff, MyFont(size: 20.vp,weight: FontWeight.Medium))|

### func textStyle(PickerTextStyle)

```cangjie
public func textStyle(value: PickerTextStyle): This
```

**功能：** 设置所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[PickerTextStyle](./cj-button-picker-datepicker.md#class-PickerTextStyle)|是|-|所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。<br/>初始值：PickerTextStyle(0xff007dff, MyFont(size: 20.vp,weight: FontWeight.Medium))。|