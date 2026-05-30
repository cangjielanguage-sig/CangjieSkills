### class AppearSymbolEffect

```cangjie
public class AppearSymbolEffect <: SymbolEffect {
    public init(scope!: EffectScope = EffectScope.LAYER)
}
```

**功能：** 出现动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [SymbolEffect](#class-symboleffect)

#### init(EffectScope)

```cangjie
public init(scope!: EffectScope = EffectScope.LAYER)
```

**功能：** 创建AppearSymbolEffect类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scope|[EffectScope](#enum-effectscope)|否|EffectScope.LAYER| **命名参数。** 动效范围。|

### class BounceSymbolEffect

```cangjie
public class BounceSymbolEffect <: SymbolEffect {
    public init(scope!: EffectScope = EffectScope.LAYER, direction!: EffectDirection = EffectDirection.DOWN)
}
```

**功能：** 弹跳动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [SymbolEffect](#class-symboleffect)

#### init(EffectScope, EffectDirection)

```cangjie
public init(scope!: EffectScope = EffectScope.LAYER, direction!: EffectDirection = EffectDirection.DOWN)
```

**功能：** 创建BounceSymbolEffect类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scope|[EffectScope](#enum-effectscope)|否|EffectScope.LAYER| **命名参数。** 动效范围。|
|direction|[EffectDirection](#enum-effectdirection)|否|EffectDirection.DOWN| **命名参数。** 动效方向。|

### class DisappearSymbolEffect

```cangjie
public class DisappearSymbolEffect <: SymbolEffect {
    public init(scope!: EffectScope = EffectScope.LAYER)
}
```

**功能：** 消失动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [SymbolEffect](#class-symboleffect)

#### init(EffectScope)

```cangjie
public init(scope!: EffectScope = EffectScope.LAYER)
```

**功能：** 创建DisappearSymbolEffect类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scope|[EffectScope](#enum-effectscope)|否|EffectScope.LAYER| **命名参数。** 动效范围。|

### class HierarchicalSymbolEffect

```cangjie
public class HierarchicalSymbolEffect <: SymbolEffect {
    public init(fillStyle!: EffectFillStyle = EffectFillStyle.CUMULATIVE)
}
```

**功能：** 层级动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [SymbolEffect](#class-symboleffect)

#### init(EffectFillStyle)

```cangjie
public init(fillStyle!: EffectFillStyle = EffectFillStyle.CUMULATIVE)
```

**功能：** 创建HierarchicalSymbolEffect类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fillStyle|[EffectFillStyle](#enum-effectfillstyle)|否|EffectFillStyle.CUMULATIVE| **命名参数。** 动效模式。|

### class PulseSymbolEffect

```cangjie
public class PulseSymbolEffect <: SymbolEffect {
    public init()
}
```

**功能：** 脉冲动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [SymbolEffect](#class-symboleffect)

#### init()

```cangjie
public init()
```

**功能：** 创建PulseSymbolEffect类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19