# Text

显示一段文本的组件。

## 子组件

可以包含[Span](./cj-text-input-span.md#span)、[ImageSpan](./cj-text-input-imagespan.md#imagespan)、[SymbolSpan](./cj-text-input-symbolspan.md#symbolspan)子组件。

## 创建组件

### init(AppResource, TextController)

```cangjie
public init(content: AppResource, controller!: TextController = TextController())
```

**功能：** 创建Text组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|文本内容，引入系统资源或者应用资源中的文本。|
|controller|[TextController](#class-textcontroller)|否|TextController()| **命名参数。** Text组件的控制器。|

### init(String, TextController)

```cangjie
public init(content: String, controller!: TextController = TextController())
```

**功能：** 创建Text组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-|文本内容。包含子组件Span且未设置属性字符串时不生效，显示Span内容，并且此时text组件的样式不生效。<br>初始值：''。|
|controller|[TextController](#class-textcontroller)|否|TextController()| **命名参数。** Text组件的控制器。|

### init(() -> Unit)

```cangjie
public init(subcomponent: () -> Unit)
```

**功能：** 创建Text组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|subcomponent|()->Unit|是|-|Text的子组件。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。