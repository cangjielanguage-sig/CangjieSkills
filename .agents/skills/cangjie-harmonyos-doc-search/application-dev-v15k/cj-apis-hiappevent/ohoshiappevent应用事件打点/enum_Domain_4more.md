## enum Domain

```cangjie
public enum Domain {
    | OS
    | ...
}
```

**功能：** 提供了所有预定义事件的领域名称常量。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### OS

```cangjie
OS
```

**功能：** 系统领域。

**起始版本：** 12

### prop value

```cangjie
public prop value: String
```

**功能：** 获取枚举的值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

## enum Event

```cangjie
public enum Event {
    | USER_LOGIN
    | USER_LOGOUT
    | DISTRIBUTED_SERVICE_START
    | APP_CRASH
    | APP_FREEZE
    | APP_LAUNCH
    | SCROLL_JANK
    | CPU_USAGE_HIGH
    | BATTERY_USAGE
    | RESOURCE_OVERLIMIT
    | ADDRESS_SANITIZER
    | MAIN_THREAD_JANK
    | ...
}
```

**功能：** 提供了所有预定义事件的事件名称常量。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### APP_CRASH

```cangjie
APP_CRASH
```

**功能：** 应用崩溃事件。

**起始版本：** 12

### APP_FREEZE

```cangjie
APP_FREEZE
```

**功能：** 应用卡死事件。

**起始版本：** 12

### APP_LAUNCH

```cangjie
APP_LAUNCH
```

**功能：** 应用启动耗时事件。系统事件名称常量。

**起始版本：** 20

### ADDRESS_SANITIZER

```cangjie
ADDRESS_SANITIZER
```

**功能：** 应用踩内存事件。系统事件名称常量。

**起始版本：** 20

### BATTERY_USAGE

```cangjie
BATTERY_USAGE
```

**功能：** 应用24h功耗器件分解统计事件。系统事件名称常量。

**起始版本：** 20

### CPU_USAGE_HIGH

```cangjie
CPU_USAGE_HIGH
```

**功能：** 应用CPU高负载事件。系统事件名称常量。

**起始版本：** 20

### DISTRIBUTED_SERVICE_START

```cangjie
DISTRIBUTED_SERVICE_START
```

**功能：** 分布式服务启动事件。

**起始版本：** 12

### MAIN_THREAD_JANK

```cangjie
MAIN_THREAD_JANK
```

**功能：** 应用主线程超时事件。系统事件名称常量。

**起始版本：** 20

### RESOURCE_OVERLIMIT

```cangjie
RESOURCE_OVERLIMIT
```

**功能：** 应用资源泄露事件。系统事件名称常量。

**起始版本：** 20

### SCROLL_JANK

```cangjie
SCROLL_JANK
```

**功能：** 应用滑动丢帧事件。系统事件名称常量。

**起始版本：** 20

### USER_LOGIN

```cangjie
USER_LOGIN
```

**功能：** 用户登录事件。

**起始版本：** 12

### USER_LOGOUT

```cangjie
USER_LOGOUT
```

**功能：** 用户登出事件。

**起始版本：** 12

### prop value

```cangjie
public prop value: String
```

**功能：** 获取枚举的值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

## enum EventType

```cangjie
public enum EventType {
    | FAULT
    | STATISTIC
    | SECURITY
    | BEHAVIOR
    | ...
}
```

**功能：** 事件类型枚举。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### BEHAVIOR

```cangjie
BEHAVIOR
```

**功能：** 行为类型事件。

**起始版本：** 12

### FAULT

```cangjie
FAULT
```

**功能：** 故障类型事件。

**起始版本：** 12

### SECURITY

```cangjie
SECURITY
```

**功能：** 安全类型事件。

**起始版本：** 12

### STATISTIC

```cangjie
STATISTIC
```

**功能：** 统计类型事件。

**起始版本：** 12

### prop value

```cangjie
public prop value: UInt32
```

**功能：** 获取枚举的值。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

## enum Param

```cangjie
public enum Param {
    | USER_ID
    | DISTRIBUTED_SERVICE_NAME
    | DISTRIBUTED_SERVICE_INSTANCE_ID
    | ...
}
```

**功能：** 提供了所有预定义参数的参数名称常量。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 12

### DISTRIBUTED_SERVICE_INSTANCE_ID

```cangjie
DISTRIBUTED_SERVICE_INSTANCE_ID
```

**功能：** 分布式服务实例ID。

**起始版本：** 12

### DISTRIBUTED_SERVICE_NAME

```cangjie
DISTRIBUTED_SERVICE_NAME
```

**功能：** 分布式服务名称。

**起始版本：** 12

### USER_ID

```cangjie
USER_ID
```

**功能：** 用户自定义ID。

**起始版本：** 12

### prop value

```cangjie
public prop value: String
```

**功能：** 获取枚举的值。

**类型：** String

**读写能力：** 只读

**起始版本：** 12