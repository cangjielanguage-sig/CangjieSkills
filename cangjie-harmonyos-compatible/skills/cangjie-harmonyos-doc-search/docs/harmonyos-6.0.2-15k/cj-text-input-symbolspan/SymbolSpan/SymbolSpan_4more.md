# SymbolSpan

作为[Text](cj-text-input-text.md)组件的子组件，用于显示图标小符号的组件。

> **说明：**
>
> - 该组件支持继承父组件Text的属性，即如果子组件未设置属性且父组件设置属性，则继承父组件设置的全部属性。
> - SymbolSpan拖拽不会置灰显示。

## 子组件

无

## 创建组件

### init(AppResource)

```cangjie
public init(value: AppResource)
```

**功能：** 创建SymbolSpan组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|SymbolSpan组件的资源名，如@r(sys.symbol.ohos_wifi)。|

> **说明：**
>
> @r(sys.symbol.ohos_wifi)中引用的资源为系统预置，SymbolGlyph仅支持系统预置的symbol资源名，引用非symbol资源将显示异常。

## 通用属性/通用事件

通用属性：全部不支持。

通用事件：全部不支持。