# 组件快捷键事件

开发者可以设置组件的自定义组合键，每个组件可以设置多个组合键。

即使组件未获焦或是在所在页面未展示，只要已经挂载到获焦窗口的组件树上就会响应自定义组合键。

开发者在设置组合键的同时可以设置自定义事件，组合键按下时，触发该自定义事件，若没有设置自定义事件，则组合键行为与click行为一致。

## func keyboardShortcut(String, Array\<ModifierKey>, () -> Unit)

```cangjie
public func keyboardShortcut(value: String, keys: Array<ModifierKey>, action: () -> Unit): This
```

**功能：** 设置组件的自定义组合键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|热键的单个字符（可以通过键盘输入的字符）。|
|keys|Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|热键组合。仅当value为FunctionKey的情况下可以为空。|
|action|() -> Unit|是|-|组合快捷键触发成功后的自定义事件回调。|

## func keyboardShortcut(FunctionKey, Array\<ModifierKey>, () -> Unit)

```cangjie
public func keyboardShortcut(value: FunctionKey, keys: Array<ModifierKey>, action: () -> Unit): This
```

**功能：** 设置组件的自定义组合键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FunctionKey](./cj-common-types.md#enum-functionkey)|是|-|热键的FunctionKey。|
|keys|Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|热键组合。仅当value为FunctionKey的情况下可以为空。|
|action|() -> Unit|是|-|组合快捷键触发成功后的自定义事件回调。|

## func keyboardShortcut(String, Array\<ModifierKey>)

```cangjie
public func keyboardShortcut(value: String, keys: Array<ModifierKey>): This
```

**功能：** 设置组件的自定义组合键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|热键的单个字符（可以通过键盘输入的字符）。|
|keys|Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|热键组合。仅当value为FunctionKey的情况下可以为空。|

## func keyboardShortcut(FunctionKey, Array\<ModifierKey>)

```cangjie
public func keyboardShortcut(value: FunctionKey, keys: Array<ModifierKey>): This
```

**功能：** 设置组件的自定义组合键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FunctionKey](./cj-common-types.md#enum-functionkey)|是|-|热键的单个字符（可以通过键盘输入的字符）。|
|keys|Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|热键组合。|