## enum EdgeEffect

```cangjie
public enum EdgeEffect {
    | Spring
    | Fade
    | None
}
```

**功能：** 边缘滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Fade

```cangjie
Fade
```

**功能：** 阴影效果，滑动到边缘后会有圆弧状的阴影。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 滑动到边缘后无效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Spring

```cangjie
Spring
```

**功能：** 弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松手后回弹。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum EllipsisMode

```cangjie
public enum EllipsisMode {
    | START
    | CENTER
    | END
}
```

**功能：** 省略方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### CENTER

```cangjie
CENTER
```

**功能：** 省略行中内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### END

```cangjie
END
```

**功能：** 省略行末内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### START

```cangjie
START
```

**功能：** 省略行首内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum EmbeddedType

```cangjie
public enum EmbeddedType {
    | EMBEDDED_UI_EXTENSION
}
```

**功能：** 用于指定EmbeddedComponent可拉起的提供方类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### EMBEDDED_UI_EXTENSION

```cangjie
EMBEDDED_UI_EXTENSION
```

**功能：** 表示当前拉起的提供方类型为EmbeddedUIExtensionAbility。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

## enum FillMode

```cangjie
public enum FillMode {
    | None
    | Forwards
    | Backwards
    | Both
}
```

**功能：** 当前播放方向下，动画开始前和结束后的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Backwards

```cangjie
Backwards
```

**功能：** 动画将在应用于目标时立即应用第一个关键帧中定义的值，并在delay期间保留此值。第一个关键帧取决于playMode，playMode为Normal或Alternate时为from的状态，playMode为Reverse或AlternateReverse时为to的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Both

```cangjie
Both
```

**功能：** 动画将遵循Forwards和Backwards的规则，从而在两个方向上扩展动画属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### Forwards

```cangjie
Forwards
```

**功能：** 目标将保留动画执行期间最后一个关键帧的状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### None

```cangjie
None
```

**功能：** 动画未执行时不会将任何样式应用于目标，动画播放完成之后恢复初始默认状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

## enum FinishCallbackType

```cangjie
public enum FinishCallbackType {
    | REMOVED
    | LOGICALLY
}
```

**功能：** 动画结束时的回调类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### LOGICALLY

```cangjie
LOGICALLY
```

**功能：** 当动画在逻辑上处于下降状态，但可能仍处于其长尾状态时，将触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 16

### REMOVED

```cangjie
REMOVED
```

**功能：** 当整个动画结束并立即删除时，将触发回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12