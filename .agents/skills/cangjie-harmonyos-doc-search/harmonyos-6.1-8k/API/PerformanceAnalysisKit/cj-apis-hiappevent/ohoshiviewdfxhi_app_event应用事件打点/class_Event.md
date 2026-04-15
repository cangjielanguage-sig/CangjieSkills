## class Event

```cangjie
public class Event {
    public static const USER_LOGIN = "hiappevent.user_login"
    public static const USER_LOGOUT = "hiappevent.user_logout"
    public static const DISTRIBUTED_SERVICE_START = "hiappevent.distributed_service_start"
    public static const APP_CRASH = "APP_CRASH"
    public static const APP_FREEZE = "APP_FREEZE"
}
```

**功能：** 提供事件名称常量。包含系统事件名称常量和应用事件名称常量，其中应用事件名称常量是为开发者在调用[Write](#static-func-writeappeventinfo)接口进行应用事件打点时预留的可选自定义事件名称。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### static const APP_CRASH

```cangjie
public static const APP_CRASH = "APP_CRASH"
```

**功能：** 应用崩溃事件。系统事件名称常量。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### static const APP_FREEZE

```cangjie
public static const APP_FREEZE = "APP_FREEZE"
```

**功能：** 应用冻屏事件。系统事件名称常量。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### static const DISTRIBUTED_SERVICE_START

```cangjie
public static const DISTRIBUTED_SERVICE_START = "hiappevent.distributed_service_start"
```

**功能：** 分布式服务启动事件。预留的应用事件名称常量。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### static const USER_LOGIN

```cangjie
public static const USER_LOGIN = "hiappevent.user_login"
```

**功能：** 用户登录事件。预留的应用事件名称常量。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22

### static const USER_LOGOUT

```cangjie
public static const USER_LOGOUT = "hiappevent.user_logout"
```

**功能：** 用户登出事件。预留的应用事件名称常量。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**起始版本：** 22