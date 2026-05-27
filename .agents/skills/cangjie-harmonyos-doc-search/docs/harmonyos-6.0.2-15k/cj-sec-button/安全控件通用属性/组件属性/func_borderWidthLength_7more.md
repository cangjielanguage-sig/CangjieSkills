### func borderWidth(Length)

```cangjie
public open func borderWidth(style: Length): This
```

**功能：** 设置安全控件的边框的宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|style|[Length](./cj-common-types.md#interface-length)|是|-|安全控件的边框的宽度。默认不设置边框宽度。|

### func borderColor(ResourceColor)

```cangjie
public open func borderColor(value: ResourceColor): This
```

**功能：** 设置安全控件的边框的颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|安全控件的边框的颜色。<br/>默认不设置边框颜色。|

### func borderRadius(Length)

```cangjie
public open func borderRadius(radius: Length): This
```

**功能：** 设置安全控件的边框圆角半径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|[Length](./cj-common-types.md#interface-length)|是|-|安全控件的边框圆角半径。|

### func padding(Length)

```cangjie
public open func padding(value: Length): This
```

**功能：** 设置安全控件的内边距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|安全控件的内边距。|

### func padding(Length, Length, Length, Length)

```cangjie
public open func padding(top!: Length = 8.vp, right!: Length = 16.vp, bottom!: Length = 8.vp, left!: Length = 16.vp): This
```

**功能：** 设置安全控件的内边距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|[Length](./cj-common-types.md#interface-length)|否|8.vp|安全控件的上边距。|
|right|[Length](./cj-common-types.md#interface-length)|否|16.vp|安全控件的右边距。|
|bottom|[Length](./cj-common-types.md#interface-length)|否|8.vp|安全控件的下边距。|
|left|[Length](./cj-common-types.md#interface-length)|否|16.vp|安全控件的左边距。|

### func textIconSpace(Length)

```cangjie
public open func textIconSpace(value: Length): This
```

**功能：** 设置安全控件中图标和文字的间距。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|安全控件中图标和文字的间距。不支持设置百分比字符串。<br/>初始值：4.vp。|

### func width(Length)

```cangjie
public open func width(value: Length): This
```

**功能：** 设置安全控件自身的宽度，缺省时将根据元素内容自适配宽度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](./cj-common-types.md#interface-length)|是|-|安全控件自身的宽度，缺省时将根据元素内容自适配宽度。若设置宽度小于当前属性组合下允许的最小宽度时，宽度会调整为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。|