# 组件快捷键事件

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

开发者可以设置组件的自定义组合键，每个组件可以设置多个组合键。

即使组件未获焦或是在所在页面未展示，只要已经挂载到获焦窗口的组件树上就会响应自定义组合键。

开发者在设置组合键的同时可以设置自定义事件，组合键按下时，触发该自定义事件，若没有设置自定义事件，则组合键行为与click行为一致。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## func keyboardShortcut(?FunctionKey, ?Array\<ModifierKey>)

```cangjie
func keyboardShortcut(value: ?FunctionKey, keys: ?Array<ModifierKey>): T
```

**功能：** 为组件设置键盘快捷键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[FunctionKey](./cj-common-types.md#enum-functionkey)|是|-|功能键<br>初始值：""。|
|keys|?Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|修饰键数组|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func keyboardShortcut(?String, ?Array\<ModifierKey>)

```cangjie
func keyboardShortcut(value: ?String, keys: ?Array<ModifierKey>): T
```

**功能：** 为组件设置键盘快捷键。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?String|是|-|快捷键字符串<br>初始值：""。|
|keys|?Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|修饰键数组|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func keyboardShortcut(?FunctionKey, ?Array\<ModifierKey>, ?() -> Unit)

```cangjie
func keyboardShortcut(value: ?FunctionKey, keys: ?Array<ModifierKey>, action: ?() -> Unit): T
```

**功能：** 为组件设置键盘快捷键并指定触发的操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?[FunctionKey](./cj-common-types.md#enum-functionkey)|是|-|功能键<br>初始值：""。|
|keys|?Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|修饰键数组|
|action|?() -> Unit|是|-|触发的操作|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|

## func keyboardShortcut(?String, ?Array\<ModifierKey>, ?() -> Unit)

```cangjie
func keyboardShortcut(value: ?String, keys: ?Array<ModifierKey>, action: ?() -> Unit): T
```

**功能：** 为组件设置键盘快捷键并指定触发的操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|?String|是|-|快捷键字符串<br>初始值：""。|
|keys|?Array\<[ModifierKey](./cj-common-types.md#enum-modifierkey)>|是|-|修饰键数组|
|action|?() -> Unit|是|-|触发的操作|

**返回值：**

|类型|说明|
|:---|:---|
|T|返回通用方法接口类型。|