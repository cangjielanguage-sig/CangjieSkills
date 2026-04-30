## struct SipAddress

```cangjie
public struct SipAddress {
    public static const INVALID_LABEL_ID: Int32 = - 1
    public static const CUSTOM_LABEL: Int32 = 0
    public static const SIP_HOME: Int32 = 1
    public static const SIP_WORK: Int32 = 2
    public static const SIP_OTHER: Int32 = 3
    public SipAddress(
        public var sipAddress: String,
        public var labelName!: String = "",
        public var labelId!: Int32 = INVALID_LABEL_ID
    )
}
```

**功能：** 联系人的会话发起协议（SIP）地址类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const CUSTOM_LABEL

```cangjie
public static const CUSTOM_LABEL: Int32 = 0
```

**功能：** 自定义会话发起协议（SIP）地址类型。

**类型：** Int32

**起始版本：** 19

### static const INVALID_LABEL_ID

```cangjie
public static const INVALID_LABEL_ID: Int32 = - 1
```

**功能：** 无效会话发起协议（SIP）地址类型。

**类型：** Int32

**起始版本：** 19

### static const SIP_HOME

```cangjie
public static const SIP_HOME: Int32 = 1
```

**功能：** 家庭会话发起协议（SIP）地址类型。

**类型：** Int32

**起始版本：** 19

### static const SIP_OTHER

```cangjie
public static const SIP_OTHER: Int32 = 3
```

**功能：** 其它会话发起协议（SIP）地址类型。

**类型：** Int32

**起始版本：** 19

### static const SIP_WORK

```cangjie
public static const SIP_WORK: Int32 = 2
```

**功能：** 工作会话发起协议（SIP）地址类型。

**类型：** Int32

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32 = INVALID_LABEL_ID
```

**功能：** 会话发起协议（SIP）地址类型ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var labelName

```cangjie
public var labelName: String = ""
```

**功能：** 会话发起协议（SIP）地址类型名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var sipAddress

```cangjie
public var sipAddress: String
```

**功能：** 会话发起协议（SIP）地址。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### SipAddress(String, String, Int32)

```cangjie
public SipAddress(
    public var sipAddress: String,
    public var labelName!: String = "",
    public var labelId!: Int32 = INVALID_LABEL_ID
)
```

**功能：** 创建SipAddress实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|sipAddress|String|是|-|会话发起协议（SIP）地址。|
|labelName|String|否|""| **命名参数。** 会话发起协议（SIP）地址类型名称。|
|labelId|Int32|否|INVALID_LABEL_ID| **命名参数。** 会话发起协议（SIP）地址类型ID。|