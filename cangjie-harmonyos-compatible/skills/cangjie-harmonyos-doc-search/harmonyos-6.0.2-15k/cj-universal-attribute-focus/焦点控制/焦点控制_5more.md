# 焦点控制

自定义组件的走焦效果，可设置组件是否走焦和具体的走焦顺序，tab键或者方向键切换焦点。

> **说明：**
>
> - 自定义组件无获焦能力，当设置[focusable](./cj-universal-attribute-focus.md#func-focusablebool)、[enabled](./cj-universal-attribute-enable.md#func-enabledbool)等属性为false，或者设置[visibility](./cj-universal-attribute-visibility.md#func-visibilityvisibility)属性为Hidden、None时，也不影响其子组件的获焦。
> - 组件主动获取焦点不受窗口焦点的控制。
> - 焦点开发参考[焦点开发指南](./cj-universal-event-focus.md)。

## func defaultFocus(Bool)

```cangjie
public func defaultFocus(isDefaultFocus: Bool): This
```

**功能：** 设置当前组件是否为当前页面上的默认焦点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| isDefaultFocus | Bool | 是 | - | 设置当前组件是否为当前页面上的默认焦点，仅在初次创建的页面第一次进入时生效。<br>初始值:false。<br>**说明：**<br>值为true则表示为默认焦点，值为false无效。|

## func focusable(Bool)

```cangjie
public func focusable(isFocusable: Bool): This
```

**功能：** 设置当前组件是否可以获焦。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| isFocusable | Bool | 是 | \- | 当前组件是否可以获焦。true表示组件可以获焦，false表示组件不可获焦。<br>**说明：**<br>存在默认交互逻辑的组件例如[Button](./cj-button-picker-button.md)、[TextInput](./cj-text-input-textinput.md)等，默认即为可获焦，[Text](./cj-text-input-text.md)、[Image](./cj-image-video-image.md)等组件则默认状态为不可获焦。不可获焦状态下，无法触发[焦点事件](./cj-universal-event-focus.md)。 |

## func focusOnTouch(Bool)

```cangjie
public func focusOnTouch(isFocusOnTouch: Bool): This
```

**功能：** 设置当前组件是否支持点击获焦能力。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| isFocusOnTouch | Bool | 是 | - | 当前组件是否支持点击获焦能力。true表示组件支持点击获焦，false表示不支持点击获焦。<br>初始值：false。<br>**说明：**<br>仅在组件可点击时才能正常获取焦点。|

## func focusBox(FocusBoxStyle)

```cangjie
public func focusBox(style: FocusBoxStyle): This
```

**功能：** 设置当前组件系统焦点框样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| style | [FocusBoxStyle](./cj-universal-attribute-focus.md#class-focusboxstyle) | 是 | \- | 当前组件系统焦点框样式。<br>**说明：**<br>该样式仅影响走焦状态下展示了系统焦点框的组件。|