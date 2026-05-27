### func showError(AppResource)

```cangjie
public func showError(value: AppResource): This
```

**功能：** 设置错误状态下提示的错误文本或者不显示错误状态。

> **说明：**
>
> 当参数类型为ResourceStr且输入内容不符合定义规范时，提示错误文本，当提示错误单行文本超长时，末尾以省略号显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|错误状态下提示的错误文本或者不显示错误状态。默认不显示错误状态。|

### func showError(String)

```cangjie
public func showError(value: String): This
```

**功能：** 设置错误状态下提示的错误文本或者不显示错误状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|错误状态下提示的错误文本或者不显示错误状态。默认不显示错误状态。|

### func showPassword(Bool)

```cangjie
public func showPassword(visible: Bool): This
```

**功能：** 设置密码的显隐状态。

> **说明：**
>
> - 当[输入框的类型](#enum-inputtype)设置为Password、NEW_PASSWORD和NUMBER_PASSWORD模式时，密码保护功能才能生效。非密码输入模式则不会触发该功能。
> - 密码模式时，由于输入框后端的状态和前端应用侧的状态管理变量会不一致，可能导致末尾图标的状态异常。建议在[onSecurityStateChange](#func-onsecuritystatechangebool---unit)上增加状态同步。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|visible|Bool|是|-|是否显示密码。<br>初始值：false。|

### func showPasswordIcon(Bool)

```cangjie
public func showPasswordIcon(visible: Bool): This
```

**功能：** 设置当密码输入模式时，输入框末尾的图标是否显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|visible|Bool|是|-|密码输入模式时，输入框末尾的图标是否显示。true表示显示，false表示不显示。<br>初始值:true。|

### func showUnderline(Bool)

```cangjie
public func showUnderline(value: Bool): This
```

**功能：** 设置是否开启下划线。

> **说明：**
>
> 下划线默认颜色为0x33182431，默认粗细为1.px，文本框尺寸48.vp，下划线只支持InputType.Normal类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|是否开启下划线。true表示开启，false表示不开启。<br>初始值：false。|

### func showUnit(() -> Unit)

```cangjie
public func showUnit(builder: () -> Unit): This
```

**功能：** 设置控件作为文本框单位。

> **说明：**
>
> 需搭配[showUnderline](#func-showunderlinebool)使用，当showUnderline为true时生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|()->Unit|是|-|文本输入时，文本框的显示单位。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|