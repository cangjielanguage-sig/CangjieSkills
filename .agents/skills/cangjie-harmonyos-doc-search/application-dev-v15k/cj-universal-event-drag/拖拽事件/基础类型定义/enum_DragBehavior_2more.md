### enum DragBehavior

```cangjie
public enum DragBehavior {
    | COPY
    | MOVE
    | UNKNOWN
}
```

**功能：** 当设置[DragResult](#enum-dragresult)为DROP_ENABLED后，可设置DragBehavior为复制（copy）或剪切（move）。DragBehavior用来向开发者描述数据的处理方式是复制（copy）还是剪切（move），但无法最终决定对数据的实际处理方式。DragBehavior会通过onDragEnd带回给数据拖出方，发起拖拽的一方可通过DragBehavior来区分做出的是复制还是剪切数据的不同行为。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### COPY

```cangjie
COPY
```

**功能：** 指定对数据的处理方式为复制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### MOVE

```cangjie
MOVE
```

**功能：** 指定对数据的处理方式为剪切。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 未知行为，可用于错误处理。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### enum DragResult

```cangjie
public enum DragResult {
    | DRAG_SUCCESSFUL
    | DRAG_FAILED
    | DRAG_CANCELED
    | DROP_ENABLED
    | DROP_DISABLED
    | DRAG_DEFAULT
}
```

**功能：** 拖拽结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DRAG_CANCELED

```cangjie
DRAG_CANCELED
```

**功能：** 拖拽取消，在onDrop中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DRAG_DEFAULT

```cangjie
DRAG_DEFAULT
```

**功能：** 默认拖拽结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DRAG_FAILED

```cangjie
DRAG_FAILED
```

**功能：** 拖拽失败，在onDrop中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DRAG_SUCCESSFUL

```cangjie
DRAG_SUCCESSFUL
```

**功能：** 拖拽成功，在onDrop中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DROP_DISABLED

```cangjie
DROP_DISABLED
```

**功能：** 组件不允许落入，在onDragMove中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### DROP_ENABLED

```cangjie
DROP_ENABLED
```

**功能：** 组件允许落入，在onDragMove中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19