### func dateTimeOptions(?String, ?String, ?String)

```cangjie
public func dateTimeOptions(hour!: ?String, minute!: ?String, second!: ?String): This
```

**功能：** 设置时分秒是否显示前导0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hour|?String|是|-|**命名参数。** 小时的显示格式，取值包括："numeric", "2-digit"。<br>24小时制初始为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制初始为"numeric"，即没有前导0。<br>当其值设置为None时，显示效果与其初始值规则一致。|
|minute|?String|是|-|**命名参数。** 分钟的显示格式，取值包括："numeric", "2-digit"。初始为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。<br>当其值设置为None时，显示效果与其初始值规则一致。|
|second|?String|是|-|**命名参数。** 秒钟的显示格式，取值包括："numeric", "2-digit"。初始为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。<br>当其值设置为None时，显示效果与其初始值规则一致。|

### func disappearTextStyle(?PickerTextStyle)

```cangjie
public func disappearTextStyle(style: ?PickerTextStyle): This
```

**功能：** 设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|?[PickerTextStyle](./cj-button-picker-datepicker.md#class-pickertextstyle)|是|-|所有选项中最上和最下两个选项的文本颜色、字号和字体粗细。<br>初始值：<br>color: 0xff182431;<br>font: MyFont(size: 14.fp, weight: FontWeight.Regular)。<br>当style的值为None时，与其初始值规则一致。|

### func enableHapticFeedback(?Bool)

```cangjie
public func enableHapticFeedback(value: ?Bool): This
```

**功能：** 设置是否开启触控反馈。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-| 是否支持触控反馈。</br>初始值：true，表示开启触控反馈。<br>设置为true后，其是否生效取决于系统的硬件支持情况。<br>当value的值为None时，与其初始值规则一致。|

### func loop(?Bool)

```cangjie
public func loop(value: ?Bool): This
```

**功能：** 设置循环模式的启用状态。

**系统能力：**  SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?Bool|是|-|是否启用循环模式。<br>初始值：true，表示启用循环模式。<br>当value的值为None时，与其初始值规则一致。|

### func selectedTextStyle(?PickerTextStyle)

```cangjie
public func selectedTextStyle(style: ?PickerTextStyle): This
```

**功能：** 设置所有选项中最上和最下两个选项的文本颜色、字号、字体粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|?[PickerTextStyle](./cj-button-picker-datepicker.md#class-pickertextstyle)|是|-|选中项的文本颜色、字号、字体粗细。<br>初始值：<br>color: 0xff007dff;<br>font: MyFont(size: 20.fp, weight: FontWeight.Medium)。<br>当style的值为None时，与其初始值规则一致。|