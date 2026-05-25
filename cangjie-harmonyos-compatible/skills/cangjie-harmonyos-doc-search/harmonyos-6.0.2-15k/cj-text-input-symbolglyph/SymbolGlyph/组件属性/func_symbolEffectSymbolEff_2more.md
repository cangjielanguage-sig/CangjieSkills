### func symbolEffect(SymbolEffect, ?Bool)

```cangjie
public func symbolEffect(symbolEffect: SymbolEffect, isActive!: ?Bool = None ): This
```

**功能：** 设置SymbolGlyph组件动效策略及播放状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|symbolEffect|[SymbolEffect](#class-symboleffect)|是|-|SymbolGlyph组件动效策略。<br>初始值：[SymbolEffect](#class-symboleffect)。|
|isActive|?Bool|否|None| **命名参数。** SymbolGlyph组件动效播放状态。true表示播放，false表示不播放。<br>初始值：false。|

### func symbolEffect(SymbolEffect, Int32)

```cangjie
public func symbolEffect(symbolEffect: SymbolEffect, triggerValue!: Int32): This
```

**功能：** 设置SymbolGlyph组件动效策略及播放触发器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|symbolEffect|[SymbolEffect](#class-symboleffect)|是|-|SymbolGlyph组件动效策略。<br>初始值：[SymbolEffect](#class-symboleffect)。|
|triggerValue|Int32|是|-| **命名参数。** SymbolGlyph组件动效播放触发器，在数值变更时触发动效。<br/>如果首次不希望触发动效，设置-1。|