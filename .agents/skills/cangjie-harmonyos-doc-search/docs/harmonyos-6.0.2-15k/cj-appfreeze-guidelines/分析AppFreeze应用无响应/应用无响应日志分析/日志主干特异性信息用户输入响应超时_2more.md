### 日志主干特异性信息(用户输入响应超时)

Reason是APP_INPUT_BLOCK，表明用户点击事件超过5s没有得到反馈。

MSG信息是这个事件的说明：用户的输入没有得到响应。

APP_INPUT_BLOCK的日志信息请参见[通用日志信息](#日志主干通用信息)进行分析。需特别说明的是，一般情况下用户输入无响应大概率主线程也会appfreeze。可以结合两个日志的三个堆栈、两个BinderCatcher信息，进行对比查看。如果没有主线程appfreeze的日志，说明有可能在输入事件之前有大量的细碎的其他事件，细碎的事件不足以导致主线程appfreeze，但是数量比较多导致用户的输入事件响应不过来。

### 日志主干特异性信息(生命周期切换超时)

Reason是LIFECYCLE_TIMEOUT的日志与上文THREAD_BLOCK_6S和THREAD_BLOCK_3S一样都是有两个事件。分别是LIFECYCLE_HALF_TIMEOUT和LIFECYCLE_TIMEOUT。

MSG说明当前是什么生命周期的超时。

示例可以看出，LIFECYCLE_TIMEOUT的可以看出Ability在切换后台的时候超时，可以按照上面[生命周期切换超时](#生命周期切换超时)的超时时间来找流水日志等信息。

LIFECYCLE_TIMEOUT：

```text
DOMAIN:AAFWK
STRINGID:LIFECYCLE
TIMEOUT TIMESTAMP:2023/03/10-17:06:53:65
PID:1561
UID:20010039
PACKAGE_NAME:com.example.myapplication
PROCESS_NAME:com.example.myapplication
MSG:ability:EntryAbility background timeout
```

其他的日志信息请参见[通用日志信息](#日志主干通用信息)进行分析。需要特别说明的是，一般情况下生命周期切换大概率主线程也会appfreeze。可以结合两个日志的三个堆栈、两个BinderCatcher信息，进行对比查看。