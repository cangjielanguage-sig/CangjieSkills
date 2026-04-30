# SymbolGlyph

显示图标小符号的组件。

## 子组件

无

## 创建组件

### init()

```cangjie
public init()
```

**功能：** 创建SymbolGlyph组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(AppResource)

```cangjie
public init(value: AppResource)
```

**功能：** 创建SymbolGlyph组件。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-|SymbolGlyph组件的资源名，如 @r(sys.symbol.ohos_wifi)。|

> **说明：**
>
> @r(sys.symbol.ohos_wifi)中引用的资源为系统预置，SymbolGlyph仅支持系统预置的symbol资源名，引用非symbol资源将显示异常。

## 通用属性/通用事件

通用属性：支持通用属性，不支持文本通用属性。

通用事件：支持通用事件。