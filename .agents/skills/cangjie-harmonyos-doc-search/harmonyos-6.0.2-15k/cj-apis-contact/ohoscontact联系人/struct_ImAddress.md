## struct ImAddress

```cangjie
public struct ImAddress {
    public static const INVALID_LABEL_ID: Int32 = - 2
    public static const CUSTOM_LABEL: Int32 = - 1
    public static const IM_AIM: Int32 = 0
    public static const IM_MSN: Int32 = 1
    public static const IM_YAHOO: Int32 = 2
    public static const IM_SKYPE: Int32 = 3
    public static const IM_QQ: Int32 = 4
    public static const IM_ICQ: Int32 = 6
    public static const IM_JABBER: Int32 = 7
    public ImAddress(
        public var imAddress: String,
        public var labelName!: String = "",
        public var labelId!: Int32 = INVALID_LABEL_ID
    )
}
```

**功能：** 联系人的即时消息地址。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const CUSTOM_LABEL

```cangjie
public static const CUSTOM_LABEL: Int32 = - 1
```

**功能：** 自定义即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const IM_AIM

```cangjie
public static const IM_AIM: Int32 = 0
```

**功能：** AIM即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const IM_ICQ

```cangjie
public static const IM_ICQ: Int32 = 6
```

**功能：** ICQ即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const IM_JABBER

```cangjie
public static const IM_JABBER: Int32 = 7
```

**功能：** JABBER即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const IM_MSN

```cangjie
public static const IM_MSN: Int32 = 1
```

**功能：** MSN即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const IM_QQ

```cangjie
public static const IM_QQ: Int32 = 4
```

**功能：** QQ即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const IM_SKYPE

```cangjie
public static const IM_SKYPE: Int32 = 3
```

**功能：** SKYPE即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const IM_YAHOO

```cangjie
public static const IM_YAHOO: Int32 = 2
```

**功能：** YAHOO即时消息类型。

**类型：** Int32

**起始版本：** 19

### static const INVALID_LABEL_ID

```cangjie
public static const INVALID_LABEL_ID: Int32 = - 2
```

**功能：** 无效的即时消息类型。

**类型：** Int32

**起始版本：** 19

### var imAddress

```cangjie
public var imAddress: String
```

**功能：** 即时消息地址。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32 = INVALID_LABEL_ID
```

**功能：** 即时消息类型ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var labelName

```cangjie
public var labelName: String = ""
```

**功能：** 即时消息类型名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### ImAddress(String, String, Int32)

```cangjie
public ImAddress(
    public var imAddress: String,
    public var labelName!: String = "",
    public var labelId!: Int32 = INVALID_LABEL_ID
)
```

**功能：** 创建ImAddress实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|imAddress|String|是|-|即时消息地址。|
|labelName|String|否|""| **命名参数。** 即时消息类型名称。|
|labelId|Int32|否|INVALID_LABEL_ID| **命名参数。** 即时消息类型ID。|