### class ReplaceSymbolEffect

```cangjie
public class ReplaceSymbolEffect <: SymbolEffect {
    public init(scope!: EffectScope = EffectScope.LAYER)
}
```

**功能：** 替换动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [SymbolEffect](#class-symboleffect)

#### init(EffectScope)

```cangjie
public init(scope!: EffectScope = EffectScope.LAYER)
```

**功能：** 创建ReplaceSymbolEffect类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scope|[EffectScope](#enum-effectscope)|否|EffectScope.LAYER| **命名参数。** 动效范围。|

### class ScaleSymbolEffect

```cangjie
public class ScaleSymbolEffect <: SymbolEffect {
    public init(scope!: EffectScope = EffectScope.LAYER, direction!: EffectDirection = EffectDirection.DOWN)
}
```

**功能：** 缩放动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [SymbolEffect](#class-symboleffect)

#### init(EffectScope, EffectDirection)

```cangjie
public init(scope!: EffectScope = EffectScope.LAYER, direction!: EffectDirection = EffectDirection.DOWN)
```

**功能：** 创建ScaleSymbolEffect类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scope|[EffectScope](#enum-effectscope)|否|EffectScope.LAYER| **命名参数。** 动效范围。|
|direction|[EffectDirection](#enum-effectdirection)|否|EffectDirection.DOWN| **命名参数。** 动效方向。|

### class SymbolEffect

```cangjie
public open class SymbolEffect {}
```

**功能：** SymbolGlyph组件动效策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum EffectDirection

```cangjie
public enum EffectDirection {
    | DOWN
    | UP
}
```

**功能：** 表示动效方向枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DOWN

```cangjie
DOWN
```

**功能：** 表示图标缩小再复原。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### UP

```cangjie
UP
```

**功能：** 表示图标放大再复原。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum EffectFillStyle

```cangjie
public enum EffectFillStyle {
    | CUMULATIVE
    | ITERATIVE
}
```

**功能：** 表示动效模式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CUMULATIVE

```cangjie
CUMULATIVE
```

**功能：** 表示累加模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ITERATIVE

```cangjie
ITERATIVE
```

**功能：** 表示迭代模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum EffectScope

```cangjie
public enum EffectScope {
    | LAYER
    | WHOLE
}
```

**功能：** 表示动效范围枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### LAYER

```cangjie
LAYER
```

**功能：** 表示分层模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### WHOLE

```cangjie
WHOLE
```

**功能：** 表示整体模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19