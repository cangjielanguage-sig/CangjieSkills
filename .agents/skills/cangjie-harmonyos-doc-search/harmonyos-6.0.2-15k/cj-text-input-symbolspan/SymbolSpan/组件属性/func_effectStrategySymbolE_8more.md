### func effectStrategy(SymbolEffectStrategy)

```cangjie
public func effectStrategy(value: SymbolEffectStrategy): This
```

**功能：** 设置SymbolSpan动效策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[SymbolEffectStrategy](./cj-text-input-symbolglyph.md#enum-symboleffectstrategy)|是|-|SymbolSpan动效策略。<br>初始值：SymbolEffectStrategy.NONE。|

### func fontColor(Array\<Color>)

```cangjie
public func fontColor(value: Array<Color>): This
```

**功能：** 设置SymbolSpan组件颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[Color](cj-common-types.md#class-color)>|是|-|SymbolSpan组件颜色。<br>初始值：不同渲染策略下默认值不同。|

### func fontColor(Array\<UInt32>)

```cangjie
public func fontColor(value: Array<UInt32>): This
```

**功能：** 设置SymbolSpan组件颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<UInt32>|是|-|SymbolSpan组件颜色。<br>初始值：不同渲染策略下默认值不同。|

### func fontColor(Array\<AppResource>)

```cangjie
public func fontColor(value: Array<AppResource>): This
```

**功能：** 设置SymbolSpan组件颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Array\<[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)>|是|-|SymbolSpan组件颜色。<br>初始值：不同渲染策略下默认值不同。|

### func fontSize(Length)

```cangjie
public func fontSize(value: Length): This
```

**功能：** 设置SymbolSpan组件大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Length](cj-common-types.md#interface-length)|是|-|SymbolSpan组件大小。<br>初始值：16.fp。单位：fp。|

### func fontWeight(Int64)

```cangjie
public func fontWeight(value: Int64): This
```

**功能：** 设置SymbolSpan组件粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|SymbolSpan组件粗细。Int64类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。|

### func fontWeight(String)

```cangjie
public func fontWeight(value: String): This
```

**功能：** 设置SymbolSpan组件粗细。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|SymbolSpan组件粗细。<br>string类型仅支持Int64类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。|

### func fontWeight(FontWeight)

```cangjie
public func fontWeight(value: FontWeight): This
```

**功能：** 设置SymbolSpan组件大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[FontWeight](cj-common-types.md#enum-fontweight)|是|-|SymbolSpan组件粗细。<br>FontWeight类型支持“bold”、“bolder”、“lighter”、“regular” 、“medium”等即对应FontWeight中相应的枚举值。<br>初始值：FontWeight.Normal。|