## enum EventPriority

```cangjie
public enum EventPriority {
    | IMMEDIATE
    | HIGH
    | LOW
    | IDLE
    | ...
}
```

**功能：** 用于表示事件被发送的优先级。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### HIGH

```cangjie
HIGH
```

**功能：** 表示事件先于LOW优先级投递。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### IDLE

```cangjie
IDLE
```

**功能：** 表示在没有其他事件的情况下，才投递该事件。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### IMMEDIATE

```cangjie
IMMEDIATE
```

**功能：** 表示事件被立即投递。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12

### LOW

```cangjie
LOW
```

**功能：** 表示事件优于IDLE优先级投递，事件的默认优先级是LOW。

**系统能力：** SystemCapability.Notification.Emitter

**起始版本：** 12