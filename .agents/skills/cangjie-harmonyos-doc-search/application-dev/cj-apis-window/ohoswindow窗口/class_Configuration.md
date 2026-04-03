## class Configuration

```cangjie
public class Configuration {
    public var name: String
    public var windowType: WindowType
    public var ctx: BaseContext
    public var displayId: Int64 = -1
    public var parentId: Int64 = -1
    public init(
        name!: String,
        windowType!: WindowType,
        ctx!: BaseContext,
        displayId!: Int64 = -1,
        parentId!: Int64 = -1
    )
}
```

**功能：** 创建子窗口或系统窗口时的参数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

### var ctx

```cangjie
public var ctx: BaseContext
```

**功能：** 当前应用上下文信息。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [BaseContext](../AbilityKit/cj-apis-app-ability.md#class-basecontext)

**读写能力：** 可读写

**起始版本：** 22

### var displayId

```cangjie
public var displayId: Int64 = -1
```

**功能：** 当前物理屏幕ID。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 22

### var name

```cangjie
public var name: String
```

**功能：** 窗口名字。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 22

### var parentId

```cangjie
public var parentId: Int64 = -1
```

**功能：** 父窗口ID。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 22

### var windowType

```cangjie
public var windowType: WindowType
```

**功能：** 窗口类型。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**类型：** [WindowType](#enum-windowtype)

**读写能力：** 可读写

**起始版本：** 22

### init(String, WindowType, BaseContext, Int64, Int64)

```cangjie
public init(
    name!: String,
    windowType!: WindowType,
    ctx!: BaseContext,
    displayId!: Int64 = -1,
    parentId!: Int64 = -1
)
```

**功能：** Configuration构造函数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-| **命名参数。** 窗口名称。|
|windowType|[WindowType](#enum-windowtype)|是|-| **命名参数。** 窗口类型。|
|ctx|[BaseContext](../AbilityKit/cj-apis-app-ability.md#class-basecontext)|是|-| **命名参数。** 当前应用上下文信息。|
|displayId|Int64|否|-1| **命名参数。** 当前物理屏幕ID。|
|parentId|Int64|否|-1| **命名参数。** 父窗口ID。|