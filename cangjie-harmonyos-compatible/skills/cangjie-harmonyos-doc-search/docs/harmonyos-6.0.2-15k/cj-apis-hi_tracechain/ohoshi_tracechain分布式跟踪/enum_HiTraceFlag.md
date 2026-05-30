## enum HiTraceFlag

```cangjie
public enum HiTraceFlag {
    | DEFAULT
    | INCLUDE_ASYNC
    | DONOT_CREATE_SPAN
    | TP_INFO
    | NO_BE_INFO
    | DISABLE_LOG
    | FAILURE_TRIGGER
    | D2D_TP_INFO
    | ...
}
```

**功能：** 跟踪标志组合类型枚举。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 12

### D2D_TP_INFO

```cangjie
D2D_TP_INFO
```

**功能：** 设备间埋点标志。TP_INFO的一个子集，设置该标志，只进行设备间的调用埋点。

**起始版本：** 12

### DEFAULT

```cangjie
DEFAULT
```

**功能：** 缺省标志。

**起始版本：** 12

### DISABLE_LOG

```cangjie
DISABLE_LOG
```

**功能：** 日志关联标志。设置该标志，指示隐藏日志中的跟踪信息。

**起始版本：** 12

### DONOT_CREATE_SPAN

```cangjie
DONOT_CREATE_SPAN
```

**功能：** 无分支标志。启动跟踪时，在同步、异步调用时缺省自动创建分支信息。设置该标志，指示不创建分支。

**起始版本：** 12

### FAILURE_TRIGGER

```cangjie
FAILURE_TRIGGER
```

**功能：** 故障触发标志。预置标志，暂时没有作用。

**起始版本：** 12

### INCLUDE_ASYNC

```cangjie
INCLUDE_ASYNC
```

**功能：** 异步调用标志。启动跟踪时，缺省只跟踪同步调用。设置该标志，同时跟踪同步、异步调用。

**起始版本：** 12

### NO_BE_INFO

```cangjie
NO_BE_INFO
```

**功能：** 无起始结束标志。启动跟踪时，缺省打印启动及结束跟踪信息。设置该标志，指示不打印启动及结束跟踪信息。

**起始版本：** 12

### TP_INFO

```cangjie
TP_INFO
```

**功能：** 埋点标志。启动跟踪式时，缺省不进行埋点。调试场景下设置该标志，在同步、异步调用的收发侧自动埋点，输出埋点信息和时间戳。收发埋点按照client、server分为[client send（CS）、server receive（SR）、server send（SS）、client receive（CR）](#enum-hitracetracepointtype)四类信息。一次同步调用输出CS/SR/SS/CR，一次异步调用输出CS/SR/SS三个埋点信息。

**起始版本：** 12

### prop value

```cangjie
public prop value: Int32
```

**功能：** 获取枚举值的值。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12