## struct Event

```cangjie
public struct Event {
    public static const INVALID_LABEL_ID: Int32 = - 1
    public static const CUSTOM_LABEL: Int32 = 0
    public static const EVENT_ANNIVERSARY: Int32 = 1
    public static const EVENT_OTHER: Int32 = 2
    public static const EVENT_BIRTHDAY: Int32 = 3
    public Event(
        public var eventDate: String,
        public var labelName!: String = "",
        public var labelId!: Int32 = INVALID_LABEL_ID
    )
}
```

**功能：** 联系人事件类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const CUSTOM_LABEL

```cangjie
public static const CUSTOM_LABEL: Int32 = 0
```

**功能：** 自定义事件类型。

**类型：** Int32

**起始版本：** 19

### static const EVENT_ANNIVERSARY

```cangjie
public static const EVENT_ANNIVERSARY: Int32 = 1
```

**功能：** 周年纪念事件类型。

**类型：** Int32

**起始版本：** 19

### static const EVENT_BIRTHDAY

```cangjie
public static const EVENT_BIRTHDAY: Int32 = 3
```

**功能：** 生日事件类型。

**类型：** Int32

**起始版本：** 19

### static const EVENT_OTHER

```cangjie
public static const EVENT_OTHER: Int32 = 2
```

**功能：** 其它事件类型。

**类型：** Int32

**起始版本：** 19

### static const INVALID_LABEL_ID

```cangjie
public static const INVALID_LABEL_ID: Int32 = - 1
```

**功能：** 无效事件类型。

**类型：** Int32

**起始版本：** 19

### var eventDate

```cangjie
public var eventDate: String
```

**功能：** 事件的日期。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32 = INVALID_LABEL_ID
```

**功能：** 事件类型ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var labelName

```cangjie
public var labelName: String = ""
```

**功能：** 事件类型名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Event(String, String, Int32)

```cangjie
public Event(
    public var eventDate: String,
    public var labelName!: String = "",
    public var labelId!: Int32 = INVALID_LABEL_ID
)
```

**功能：** 创建Event实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventDate|String|是|-|事件的日期。|
|labelName|String|否|""| **命名参数。** 事件类型名称。|
|labelId|Int32|否|INVALID_LABEL_ID| **命名参数。** 事件类型名称ID。|