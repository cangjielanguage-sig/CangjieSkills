## func accessibilityDescription(String)

```cangjie
public func accessibilityDescription(value: String): This
```

**功能：** 设置无障碍说明。

> **说明：**
>
> 该属性用于为用户进一步说明当前组件，开发人员可为组件设置相对较详细的解释文本，帮助用户理解将要执行的操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|无障碍说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。<br>初始值：“”。|

## func accessibilityDescription(AppResource)

```cangjie
public func accessibilityDescription(value: AppResource): This
```

**功能：** 设置无障碍说明，支持通过Resource引用资源文件。

> **说明：**
>
> 该属性用于为用户进一步说明当前组件，开发人员可为组件设置相对较详细的解释文本，帮助用户理解将要执行的操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|无障碍说明引用资源，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置相对较详细的解释文本，帮助用户理解将要执行的操作。如帮助用户理解将要执行的操作可能导致什么后果，尤其是当这些后果无法从组件本身属性与无障碍文本中了解到时。若组件既拥有文本属性又拥有无障碍说明属性，则组件被选中时，先播报组件的文本属性，再播报无障碍说明属性的内容。|

## func accessibilityLevel(String)

```cangjie
public func accessibilityLevel(value: String): This
```

**功能：** 设置无障碍重要性。

> **说明：**
>
> 该属性用于控制某个组件是否可被无障碍辅助服务所识别。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|无障碍重要性，用于控制某个组件是否可被无障碍辅助服务所识别。<br>支持的值为:<br>"auto"：根据组件不同会转换为“yes”或者“no”。<br>"yes"：当前组件可被无障碍辅助服务所识别。<br>"no"：当前组件不可被无障碍辅助服务所识别。<br>"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。<br>初始值："auto"。<br>以下组件当accessibilityLevel设置成"auto"时，当前组件可被无障碍辅助服务所识别：Checkbox, CheckboxGroup, Gauge, Marquee, MenuItem, MenuItemGroup, Menu, Navigation, DatePicker, Progress, Radio, Rating, ScrollBar, Select, Slider, Stepper, Text, TextClock, TextPicker, TextTimer, TimePicker, Toggle, Web.|

## func accessibilityTextHint(String)

```cangjie
public func accessibilityTextHint(value: String): This
```

**功能：** 设置组件的文本提示信息，供无障碍辅助应用查询。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|无障碍提示说明，用于为用户进一步说明当前组件，开发人员可为组件的该属性设置解释文本，帮助用户理解将要执行的操作。|