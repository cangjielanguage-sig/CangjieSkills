### func effectStrategy(SymbolEffectStrategy)

```cangjie
public func effectStrategy(value: SymbolEffectStrategy): This
```

**功能：** 设置SymbolGlyph组件动效策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SymbolEffectStrategy](#enum-symboleffectstrategy)|是|-|SymbolGlyph组件动效策略。<br>初始值：SymbolEffectStrategy.NONE。|

### func fontColor(Array\<Color>)

```cangjie
public func fontColor(value: Array<Color>): This
```

**功能：** 设置SymbolGlyph组件颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[Color](./cj-common-types.md#class-color)>|是|-|SymbolGlyph组件颜色。<br>初始值：不同渲染策略下初始值不同。|

### func fontColor(Array\<UInt32>)

```cangjie
public func fontColor(value: Array<UInt32>): This
```

**功能：** 设置SymbolGlyph组件颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<UInt32>|是|-|SymbolGlyph组件颜色。<br>初始值：不同渲染策略下初始值不同。|

### func fontColor(Array\<AppResource>)

```cangjie
public func fontColor(value: Array<AppResource>): This
```

**功能：** 设置SymbolGlyph组件颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)>|是|-|SymbolGlyph组件颜色。<br>初始值：不同渲染策略下初始值不同。|

### func fontSize(Length)

```cangjie
public func fontSize(size: Length): This
```

**功能：** 设置SymbolGlyph组件大小。

> **说明：**
>
> 组件的图标显示大小由fontSize控制，设置width或height后，其他通用属性仅对组件的占位大小生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Length](./cj-common-types.md#interface-length)|是|-|SymbolGlyph组件大小。不支持设置百分比字符串。单位：fp。<br>初始值：16.fp。|

### func fontWeight(FontWeight)

```cangjie
public func fontWeight(value: FontWeight): This
```

**功能：** 设置SymbolGlyph组件粗细。

> **说明：**
>
> sys.symbol.ohos_lungs图标不支持设置fontWeight。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontWeight](./cj-common-types.md#enum-fontweight)|是|-|SymbolGlyph组件粗细。<br>初始值：FontWeight.Normal。|

### func renderingStrategy(SymbolRenderingStrategy)

```cangjie
public func renderingStrategy(value: SymbolRenderingStrategy): This
```

**功能：** 设置SymbolGlyph组件渲染策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SymbolRenderingStrategy](#enum-symbolrenderingstrategy)|是|-|SymbolGlyph组件渲染策略。<br>初始值：SymbolRenderingStrategy.SINGLE。|

**不同渲染策略效果可参考以下示意图。**
![symbolGlyph](figures/symbolglyphExample1.png)