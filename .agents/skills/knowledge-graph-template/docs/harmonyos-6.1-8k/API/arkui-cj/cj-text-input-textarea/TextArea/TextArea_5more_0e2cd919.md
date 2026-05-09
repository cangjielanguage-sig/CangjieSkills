# TextArea

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

无

## 创建组件

### init(?ResourceStr, ?ResourceStr, ?TextAreaController)

```cangjie
public init(placeholder!: ?ResourceStr = None, text!: ?ResourceStr = None,
    controller!: ?TextAreaController = None)
```

**功能：** 创建一个包含占位符文本、当前文本内容和控制器的TextArea对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|placeholder|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** 占位符文本，无输入时显示的文本。|
|text|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|None| **命名参数。** TextArea的当前值。|
|controller|?[TextAreaController](#class-textareacontroller)|否|None| **命名参数。** TextArea组件的控制器。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。