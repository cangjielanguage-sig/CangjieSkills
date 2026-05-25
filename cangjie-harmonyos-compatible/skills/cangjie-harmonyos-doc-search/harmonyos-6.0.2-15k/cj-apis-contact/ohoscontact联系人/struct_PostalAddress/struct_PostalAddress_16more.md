## struct PostalAddress

```cangjie
public struct PostalAddress {
    public static const INVALID_LABEL_ID: Int32 = - 1
    public static const CUSTOM_LABEL: Int32 = 0
    public static const ADDR_HOME: Int32 = 1
    public static const ADDR_WORK: Int32 = 2
    public static const ADDR_OTHER: Int32 = 3
    public PostalAddress(
        public var postalAddress: String,
        public var city!: String = "",
        public var country!: String = "",
        public var neighborhood!: String = "",
        public var pobox!: String = "",
        public var postcode!: String = "",
        public var region!: String = "",
        public var street!: String = "",
        public var labelName!: String = "",
        public var labelId!: Int32 = INVALID_LABEL_ID
    )
}
```

**功能：** 联系人的邮政地址类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const ADDR_HOME

```cangjie
public static const ADDR_HOME: Int32 = 1
```

**功能：** 家庭地址类型。

**类型：** Int32

**起始版本：** 19

### static const ADDR_OTHER

```cangjie
public static const ADDR_OTHER: Int32 = 3
```

**功能：** 其它地址类型。

**类型：** Int32

**起始版本：** 19

### static const ADDR_WORK

```cangjie
public static const ADDR_WORK: Int32 = 2
```

**功能：** 工作地址类型。

**类型：** Int32

**起始版本：** 19

### static const CUSTOM_LABEL

```cangjie
public static const CUSTOM_LABEL: Int32 = 0
```

**功能：** 自定义邮政地址类型。

**类型：** Int32

**起始版本：** 19

### static const INVALID_LABEL_ID

```cangjie
public static const INVALID_LABEL_ID: Int32 = - 1
```

**功能：** 无效地址类型。

**类型：** Int32

**起始版本：** 19

### var city

```cangjie
public var city: String = ""
```

**功能：** 联系人所在的城市。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var country

```cangjie
public var country: String = ""
```

**功能：** 联系人所在的国家。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32 = INVALID_LABEL_ID
```

**功能：** 邮政地址类型ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var labelName

```cangjie
public var labelName: String = ""
```

**功能：** 邮政地址类型名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var neighborhood

```cangjie
public var neighborhood: String = ""
```

**功能：** 联系人的邻居。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var pobox

```cangjie
public var pobox: String = ""
```

**功能：** 联系人的邮箱。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var postalAddress

```cangjie
public var postalAddress: String
```

**功能：** 联系人的邮政地址。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var postcode

```cangjie
public var postcode: String = ""
```

**功能：** 联系人所在区域的邮政编码。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var region

```cangjie
public var region: String = ""
```

**功能：** 联系人所在的区域。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var street

```cangjie
public var street: String = ""
```

**功能：** 联系人所在的街道。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19