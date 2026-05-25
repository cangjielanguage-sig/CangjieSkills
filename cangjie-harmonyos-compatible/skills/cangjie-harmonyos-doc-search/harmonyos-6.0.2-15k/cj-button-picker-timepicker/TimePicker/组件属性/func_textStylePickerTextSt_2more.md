### func textStyle(?PickerTextStyle)

```cangjie
public func textStyle(style: ?PickerTextStyle): This
```

**功能：** 设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|?[PickerTextStyle](./cj-button-picker-datepicker.md#class-pickertextstyle)|是|-|所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细。<br>初始值：<br>color: 0xff182431;<br>font: MyFont(size: 16.fp, weight: FontWeight.Regular)。<br>当style的值为None时，与其初始值规则一致。|

### func useMilitaryTime(?Bool)

```cangjie
public func useMilitaryTime(value: ?Bool): This
```

**功能：** 设置展示时间是否为24小时制。如果展示时间为12小时制，上下午与小时无联动。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|展示时间是否为24小时制。<br>初始值：false。<br>false表示展示时间为12小时制，true表示展示时间为24小时制。<br>当value的值为None时，与其初始值规则一致。|