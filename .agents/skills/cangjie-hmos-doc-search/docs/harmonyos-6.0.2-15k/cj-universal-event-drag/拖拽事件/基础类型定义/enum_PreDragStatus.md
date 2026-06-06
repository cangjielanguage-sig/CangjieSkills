### enum PreDragStatus

```cangjie
public enum PreDragStatus {
    | ACTION_DETECTING_STATUS
    | READY_TO_TRIGGER_DRAG_ACTION
    | PREVIEW_LIFT_STARTED
    | PREVIEW_LIFT_FINISHED
    | PREVIEW_LANDING_STARTED
    | PREVIEW_LANDING_FINISHED
    | ACTION_CANCELED_BEFORE_DRAG
}
```

**功能：** 拖拽启动状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ACTION_CANCELED_BEFORE_DRAG

```cangjie
ACTION_CANCELED_BEFORE_DRAG
```

**功能：** 拖拽浮起落位动效中断。(已满足READY_TO_TRIGGER_DRAG_ACTION状态后，未达到动效阶段，手指抬手时触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ACTION_DETECTING_STATUS

```cangjie
ACTION_DETECTING_STATUS
```

**功能：** 拖拽手势启动阶段。(按下50ms时触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PREVIEW_LANDING_FINISHED

```cangjie
PREVIEW_LANDING_FINISHED
```

**功能：** 拖拽落回动效结束阶段。(落回动效结束时触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PREVIEW_LANDING_STARTED

```cangjie
PREVIEW_LANDING_STARTED
```

**功能：** 拖拽落回动效发起阶段。(落回动效发起时触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PREVIEW_LIFT_FINISHED

```cangjie
PREVIEW_LIFT_FINISHED
```

**功能：** 拖拽浮起动效结束阶段。(浮起动效完全结束时触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### PREVIEW_LIFT_STARTED

```cangjie
PREVIEW_LIFT_STARTED
```

**功能：** 拖拽浮起动效发起阶段。(按下800ms时触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### READY_TO_TRIGGER_DRAG_ACTION

```cangjie
READY_TO_TRIGGER_DRAG_ACTION
```

**功能：** 拖拽准备完成，可发起拖拽阶段。(按下500ms时触发)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19