## struct Email

```cangjie
public struct Email {
    public static const INVALID_LABEL_ID: Int32 = - 1
    public static const CUSTOM_LABEL: Int32 = 0
    public static const EMAIL_HOME: Int32 = 1
    public static const EMAIL_WORK: Int32 = 2
    public static const EMAIL_OTHER: Int32 = 3
    public Email(
        public var email: String,
        public var displayName!: String = "",
        public var labelName!: String = "",
        public var labelId!: Int32 = INVALID_LABEL_ID
    )
}
```

**功能：** 联系人的邮箱。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const CUSTOM_LABEL

```cangjie
public static const CUSTOM_LABEL: Int32 = 0
```

**功能：** 自定义邮箱类型。

**类型：** Int32

**起始版本：** 19

### static const EMAIL_HOME

```cangjie
public static const EMAIL_HOME: Int32 = 1
```

**功能：** 家庭邮箱类型。

**类型：** Int32

**起始版本：** 19

### static const EMAIL_OTHER

```cangjie
public static const EMAIL_OTHER: Int32 = 3
```

**功能：** 其它邮箱类型。

**类型：** Int32

**起始版本：** 19

### static const EMAIL_WORK

```cangjie
public static const EMAIL_WORK: Int32 = 2
```

**功能：** 工作邮箱类型。

**类型：** Int32

**起始版本：** 19

### static const INVALID_LABEL_ID

```cangjie
public static const INVALID_LABEL_ID: Int32 = - 1
```

**功能：** 无效邮箱类型。

**类型：** Int32

**起始版本：** 19

### var displayName

```cangjie
public var displayName: String = ""
```

**功能：** 邮箱的类型名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var email

```cangjie
public var email: String
```

**功能：** 邮箱地址。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32 = INVALID_LABEL_ID
```

**功能：** 邮箱的类型ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var labelName

```cangjie
public var labelName: String = ""
```

**功能：** 邮箱的显示名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Email(String, String, String, Int32)

```cangjie
public Email(
    public var email: String,
    public var displayName!: String = "",
    public var labelName!: String = "",
    public var labelId!: Int32 = INVALID_LABEL_ID
)
```

**功能：** 创建Email实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|email|String|是|-|邮箱地址。|
|displayName|String|否|""| **命名参数。** 邮箱的类型名称。|
|labelName|String|否|""| **命名参数。** 邮箱的显示名称。|
|labelId|Int32|否|INVALID_LABEL_ID| **命名参数。** 邮箱的类型ID。|