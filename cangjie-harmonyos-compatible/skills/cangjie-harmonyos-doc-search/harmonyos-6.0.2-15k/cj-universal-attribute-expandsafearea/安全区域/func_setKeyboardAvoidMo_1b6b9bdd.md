## func setKeyboardAvoidMode(value: KeyboardAvoidMode)

```cangjie
public func setKeyboardAvoidMode(value: KeyboardAvoidMode): void
```

**功能：** 控制虚拟键盘抬起时页面的避让模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :--- | :--- | :--- | :--- | :--- |
| value | [KeyboardAvoidMode](./cj-universal-attribute-expandsafearea.md#enum-keyboardavoidmode) | 是 | - | 配置虚拟键盘抬起时页面的避让模式。<br>初始值：KeyboardAvoidMode.OFFSET，键盘抬起时默认页面避让模式为上抬模式。 |

> **说明：**
>
> - KeyboardAvoidMode的RESIZE模式是压缩Page的大小，Page下设置百分比宽高的组件会跟随Page压缩，直接设置宽高的组件会按设置的固定大小布局。设置KeyboardAvoidMode的RESIZE模式时，expandSafeArea([SafeAreaType.KEYBOARD],[SafeAreaEdge.BOTTOM])不生效。
> - KeyboardAvoidMode.NONE配置Page不避让键盘，Page会被抬起的键盘遮盖。