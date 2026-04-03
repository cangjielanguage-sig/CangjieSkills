## class Configuration

```cangjie
public class Configuration {
    public Configuration(
        public let name: String,
        public let windowType: WindowType,
        public let ctx: StageContext,
        public var displayId!: Int64 = -1,
        public var parentId!: Int64 = -1,
        public var decorEnabled!: Bool = false,
        public var title!: String = ""
    )
}
```

**功能：** 创建子窗口或系统窗口时的参数。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

### let name

```cangjie
public let name: String
```

**功能：** 表示窗口名字。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let windowType

```cangjie
public let windowType: WindowType
```

**功能：** 表示窗口类型。

**类型：** [WindowType](#enum-windowtype)

**读写能力：** 只读

**起始版本：** 19

### let ctx

```cangjie
public let ctx: StageContext
```

**功能：** 表示当前应用上下文信息。用于创建悬浮窗、模态窗或系统窗口。

**类型：** [StageContext](../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)

**读写能力：** 只读

**起始版本：** 19

### var displayId

```cangjie
public var displayId: Int64 = -1
```

**功能：** 设置当前物理屏幕id。不设置，则默认为-1。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var parentId

```cangjie
public var parentId: Int64 = -1
```

**功能：** 设置父窗口id。不设置，则默认为-1。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var decorEnabled

```cangjie
public var decorEnabled: Bool = false
```

**功能：** 是否显示窗口装饰，仅在windowType为TYPE_DIALOG时生效。true表示显示，false表示不显示。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: String = ""
```

**功能：** 设置窗口的标题内容。当[decorEnabled](#var-decorenabled)属性设置为true时，才会显示窗口的标题内容。不设置，则默认为空字符串。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Configuration(String, WindowType, StageContext, Int64, Int64, Bool, String)

```cangjie
public Configuration(
    public let name: String,
    public let windowType: WindowType,
    public let ctx: StageContext,
    public var displayId!: Int64 = -1,
    public var parentId!: Int64 = -1,
    public var decorEnabled!: Bool = false,
    public var title!: String = ""
)
```

**功能：** 构建一个Configuration类型的对象。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|窗口名字。|
|windowType|[WindowType](#enum-windowtype)|是|-|窗口类型。|
|ctx|[StageContext](../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|是|-|当前应用上下文信息。用于创建悬浮窗、模态窗或系统窗口。|
|displayId|Int64|否|-1| **命名参数。** 当前物理屏幕id。|
|parentId|Int64|否|-1| **命名参数。** 父窗口id。|
|decorEnabled|Bool|否|false| **命名参数。** 是否显示窗口装饰，仅在[windowType](#enum-windowtype)为TYPE_DIALOG时生效。true表示显示，false表示不显示。<br>**系统能力：** SystemCapability.Window.SessionManager|
|title|String|否|""| **命名参数。** decorEnabled属性设置为true时，窗口的标题内容。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。<br>**系统能力：** SystemCapability.Window.SessionManager|