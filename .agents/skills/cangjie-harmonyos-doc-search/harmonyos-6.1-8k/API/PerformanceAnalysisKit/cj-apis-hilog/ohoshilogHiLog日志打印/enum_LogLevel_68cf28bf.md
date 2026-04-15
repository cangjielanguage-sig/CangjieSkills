## enum LogLevel

```cangjie
public enum LogLevel {
    | Debug
    | Info
    | Warning
    | Error
    | Fatal
    | ...
}
```

**功能：** 日志级别。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

### Debug

```cangjie
Debug
```

**功能：** 详细的流程记录，通过该级别的日志可以更详细地分析业务流程和定位分析问题。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

### Error

```cangjie
Error
```

**功能：** 应用发生了错误，该错误会影响功能的正常运行或用户的正常使用，可以恢复但恢复代价较高，如重置数据等。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

### Fatal

```cangjie
Fatal
```

**功能：** 重大致命异常，表明应用即将崩溃，故障无法恢复。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

### Info

```cangjie
Info
```

**功能：** 用于记录业务关键流程节点，可以还原业务的主要运行过程；

用于记录可预料的非正常情况信息，如无网络信号、登录失败等。

这些日志都应该由该业务内处于支配地位的模块来记录，避免在多个被调用的模块或低级函数中重复记录。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22

### Warning

```cangjie
Warning
```

**功能：** 用于记录较为严重的非预期情况，但是对用户影响不大，应用可以自动恢复或通过简单的操作就可以恢复的问题。

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 22