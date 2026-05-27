### class GestureInfo

```cangjie
public class GestureInfo {
    public let tag: String,
    public let `type`: GestureTypes,
}
```

**功能：** 手势基础信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let `type`

```cangjie
public let `type`: GestureTypes
```

**功能：** 手势类型。

**类型：** [GestureTypes](#enum-gesturetypes)

**读写能力：** 只读

**起始版本：** 19

#### let isSystemGesture

```cangjie
public let isSystemGesture: Bool
```

**功能：** 判断当前手势是否是组件自带的手势。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

#### let tag

```cangjie
public let tag: String
```

**功能：** 手势标记。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### enum GestureTypes

```cangjie
public enum GestureTypes {
    | TAP_GESTURE
    | LONG_PRESS_GESTURE
    | PAN_GESTURE
    | PINCH_GESTURE
    | SWIPE_GESTURE
    | ROTATION_GESTURE
    | DRAG
    | CLICK
}
```

**功能：** 手势类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CLICK

```cangjie
CLICK
```

**功能：** 点击。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DRAG

```cangjie
DRAG
```

**功能：** 拖拽。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### LONG_PRESS_GESTURE

```cangjie
LONG_PRESS_GESTURE
```

**功能：** 长按手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PAN_GESTURE

```cangjie
PAN_GESTURE
```

**功能：** 拖动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PINCH_GESTURE

```cangjie
PINCH_GESTURE
```

**功能：** 捏合手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ROTATION_GESTURE

```cangjie
ROTATION_GESTURE
```

**功能：** 旋转手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### SWIPE_GESTURE

```cangjie
SWIPE_GESTURE
```

**功能：** 滑动手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### TAP_GESTURE

```cangjie
TAP_GESTURE
```

**功能：** 点击手势。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum GestureJudgeResult

```cangjie
public enum GestureJudgeResult {
    | CONTINUE
    | REJECT
}
```

**功能：** 自定义的手势判定结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### CONTINUE

```cangjie
CONTINUE
```

**功能：** 不影响系统手势判定流程。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### REJECT

```cangjie
REJECT
```

**功能：** 对于用户自定义的手势判定结果为失败。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19