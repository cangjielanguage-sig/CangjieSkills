# Text

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

显示一段文本的组件。

<!--RP3--><!--RP3End-->

## 导入模块

```cangjie
import kit.ArkUI.*
```

## 子组件

可以包含[Span](./cj-text-input-span.md)、[ImageSpan](./cj-text-input-imagespan.md)子组件。

## 创建组件

### init(?ResourceStr, ?TextController, () -> Unit)

```cangjie
public init(content: ?ResourceStr, controller!: ?TextController = None, child!: () -> Unit = { =>})
```

**功能：** 创建一个包含文本内容、控制器和子组件的Text对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|?[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-|文本内容。|
|controller|?[TextController](#class-textcontroller)|否|None| **命名参数。** 给组件绑定一个控制器。|
|child|() -> Unit|否|{=>}| **命名参数。** Text容器的子组件。|

### init(?TextController, () -> Unit)

```cangjie
public init(controller!: ?TextController = None, child!: () -> Unit)
```

**功能：** 创建一个包含控制器和子组件的Text对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|controller|?[TextController](#class-textcontroller)|否|None| **命名参数。** 给组件绑定一个控制器。|
|child|() -> Unit|是|-| **命名参数。** Text容器的子组件。|

### init(?TextController)

```cangjie
public init(controller!: ?TextController = None)
```

**功能：** 创建一个包含控制器的Text对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|controller|?[TextController](#class-textcontroller)|否|None| **命名参数。** 给组件绑定一个控制器。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。