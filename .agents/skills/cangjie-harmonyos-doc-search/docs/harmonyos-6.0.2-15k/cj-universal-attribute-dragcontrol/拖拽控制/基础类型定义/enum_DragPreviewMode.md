### enum DragPreviewMode

```cangjie
public enum DragPreviewMode {
    | AUTO
    | DISABLE_SCALE
    | ENABLE_DEFAULT_SHADOW
    | ENABLE_DEFAULT_RADIUS
}
```

**功能：** 拖拽行为控制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### AUTO

```cangjie
AUTO
```

**功能：** 系统根据拖拽场景自动改变跟手点位置，根据规则自动对拖拽背板图进行缩放变换等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DISABLE_SCALE

```cangjie
DISABLE_SCALE
```

**功能：** 禁用系统对拖拽背板图的缩放行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ENABLE_DEFAULT_SHADOW

```cangjie
ENABLE_DEFAULT_SHADOW
```

**功能：** 启用非文本类组件默认阴影效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ENABLE_DEFAULT_RADIUS

```cangjie
ENABLE_DEFAULT_RADIUS
```

**功能：** 启用非文本类组件统一圆角效果，默认值12vp。当应用自身设置的圆角值大于默认值或modifier设置的圆角时，则显示应用自定义圆角效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19