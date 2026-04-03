# 无障碍属性

组件可以设置相应的无障碍属性和事件来更好地使用无障碍能力。

## func accessibilityGroup(Bool)

```cangjie
public func accessibilityGroup(value: Bool): This
```

**功能：** 设置是否启用无障碍分组。

> **说明：**
>
> - 启用无障碍分组后该组件及其所有子组件将作为一整个可以选中的组件，无障碍服务将不再关注其子组件内容。
> - 若组件启用无障碍分组，当组件不包含通用文本属性，同时未设置[无障碍文本](#func-accessibilitytextstring)时，将默认拼接其子组件的通用文本属性作为组件的合并文本，若某一子组件没有通用文本属性，则忽略该子组件不进行拼接。此时合并文本不使用子组件的无障碍文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|无障碍组，设置为true时表示该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容。初始值：false。|

## func accessibilityText(String)

```cangjie
public func accessibilityText(value: String): This
```

**功能：** 设置无障碍文本。

> **说明：**
>
> 当组件不包含文本属性时，开发人员可通过设置无障碍文本属性，使不包含文字信息的组件能够播报无障碍文本的内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|无障碍文本，当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。<br>初始值：“”。<br>若组件既拥有文本属性，又拥有无障碍文本属性，则组件被选中时，仅播报无障碍文本内容。<br>若组件设置了无障碍分组属性为true，但是即没有无障碍文本属性，也没有文本属性，会对其子节点的组件进行文本拼接（深度优先）。<br>不对无障碍文本属性进行拼接，如需优先拼接无障碍文本，则需设置accessibilityGroup的accessibilityPreferred。|

## func accessibilityText(AppResource)

```cangjie
public func accessibilityText(value: AppResource): This
```

**功能：** 设置无障碍文本，支持通过Resource引用资源文件。

> **说明：**
>
> 当组件不包含文本属性时，开发人员可通过设置无障碍文本属性，使不包含文字信息的组件能够播报无障碍文本的内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|无障碍文本引用资源，当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。<br>若组件既拥有文本属性，又拥有无障碍文本属性，则组件被选中时，仅播报无障碍文本内容。<br>若组件设置了无障碍分组属性为true，但是即没有无障碍文本属性，也没有文本属性，会对其子节点的组件进行文本拼接（深度优先）。<br>不对无障碍文本属性进行拼接，如需优先拼接无障碍文本，则需设置accessibilityGroup的accessibilityPreferred。|