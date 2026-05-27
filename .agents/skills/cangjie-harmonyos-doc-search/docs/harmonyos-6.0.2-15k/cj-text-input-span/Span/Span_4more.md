# Span

作为[Text](cj-text-input-text.md)组件的子组件，用于显示行内文本的组件。

## 子组件

无

## 创建组件

### init(String)

```cangjie
public init(content: String)
```

**功能：** 创建Span组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|String|是|-|文本内容。|

### init(AppResource)

```cangjie
public init(content: AppResource)
```

**功能：** 创建Span组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|content|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|文本内容。|

## 通用属性/通用事件

通用属性：全部支持。

通用事件：全部支持。

> **说明：**
>
> 由于Span组件无尺寸信息，因此点击事件返回的ClickEvent对象的target属性无效。