## enum HiTraceTracepointType

```cangjie
public enum HiTraceTracepointType {
    | CS
    | CR
    | SS
    | SR
    | GENERAL
    | ...
}
```

**功能：** 跟踪埋点类型枚举。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

### CR

```cangjie
CR
```

**功能：** 客户端接收类型，标识client侧的接收埋点。

**起始版本：** 12

### CS

```cangjie
CS
```

**功能：** 客户端发送类型，标识client侧的发送埋点。

**起始版本：** 12

### GENERAL

```cangjie
GENERAL
```

**功能：** 一般类型，标识CS、CR、SS、SR四种场景之外的埋点。

**起始版本：** 12

### SR

```cangjie
SR
```

**功能：** 服务端接收类型，标识server侧的接收埋点。

**起始版本：** 12

### SS

```cangjie
SS
```

**功能：** 服务端发送类型，标识server侧的发送埋点。

**起始版本：** 12

### prop value

```cangjie
public prop value: UInt64
```

**功能：** 获取枚举值的值。

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 12