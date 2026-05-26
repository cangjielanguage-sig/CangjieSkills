### enum SymbolEffectStrategy

```cangjie
public enum SymbolEffectStrategy {
    | NONE
    | SCALE
    | HIERARCHICAL
}
```

**功能：** 动效类型的枚举值。设置动效后，动效启动即生效，无需触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### HIERARCHICAL

```cangjie
HIERARCHICAL
```

**功能：** 表示层级动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### NONE

```cangjie
NONE
```

**功能：** 表示无动效（默认值）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SCALE

```cangjie
SCALE
```

**功能：** 表示整体缩放动效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum SymbolRenderingStrategy

```cangjie
public enum SymbolRenderingStrategy {
    | SINGLE
    | MULTIPLE_COLOR
    | MULTIPLE_OPACITY
}
```

**功能：** 渲染模式的枚举值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### MULTIPLE_COLOR

```cangjie
MULTIPLE_COLOR
```

**功能：** 表示多色模式。

> **说明：**
>
> - 最多可以设置三个颜色。当只设置一个颜色时，修改symbol图标的第一层颜色，其他颜色保持默认颜色。
> - 颜色设置顺序与图标分层顺序匹配，当颜色数量大于图标分层时，多余的颜色不生效。
> - 仅支持设置颜色，不透明度设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### MULTIPLE_OPACITY

```cangjie
MULTIPLE_OPACITY
```

**功能：** 表示分层模式。

> **说明：**
>
> - 默认为黑色，可以设置一个颜色。当用户设置多个颜色时，仅生效第一个颜色。
> - 不透明度与图层相关，symbol图标的第一层透明度为100%、第二层透明度为50%、第三层透明度为20%。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SINGLE

```cangjie
SINGLE
```

**功能：** 表示单色模式（默认值）。

> **说明：**
>
> 可以设置一个或者多个颜色，默认为黑色。当设置多个颜色时，仅生效第一个颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19