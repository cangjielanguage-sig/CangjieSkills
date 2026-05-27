## struct Name

```cangjie
public struct Name {
    public Name(
        public var familyName!: String = "",
        public var familyNamePhonetic!: String = "",
        public var fullName!: String = "",
        public var givenName!: String = "",
        public var givenNamePhonetic!: String = "",
        public var middleName!: String = "",
        public var middleNamePhonetic!: String = "",
        public var namePrefix!: String = "",
        public var nameSuffix!: String = ""
    )
}
```

**功能：** 联系人的名字类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### var familyName

```cangjie
public var familyName: String = ""
```

**功能：** 联系人的家庭姓名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var familyNamePhonetic

```cangjie
public var familyNamePhonetic: String = ""
```

**功能：** 联系人的家庭姓名拼音。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var fullName

```cangjie
public var fullName: String = ""
```

**功能：** 联系人的全名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var givenName

```cangjie
public var givenName: String = ""
```

**功能：** 联系人的名称（firstName）。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var givenNamePhonetic

```cangjie
public var givenNamePhonetic: String = ""
```

**功能：** 联系人的名称拼音。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var middleName

```cangjie
public var middleName: String = ""
```

**功能：** 联系人的中间名。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var middleNamePhonetic

```cangjie
public var middleNamePhonetic: String = ""
```

**功能：** 联系人的中间名拼音。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var namePrefix

```cangjie
public var namePrefix: String = ""
```

**功能：** 联系人的姓名前缀。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var nameSuffix

```cangjie
public var nameSuffix: String = ""
```

**功能：** 联系人的姓名后缀。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Name(String, String, String, String, String, String, String, String, String)

```cangjie
public Name(
    public var familyName!: String = "",
    public var familyNamePhonetic!: String = "",
    public var fullName!: String = "",
    public var givenName!: String = "",
    public var givenNamePhonetic!: String = "",
    public var middleName!: String = "",
    public var middleNamePhonetic!: String = "",
    public var namePrefix!: String = "",
    public var nameSuffix!: String = ""
)
```

**功能：** 创建Name实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|familyName|String|否|""| **命名参数。** 联系人的家庭姓名。|
|familyNamePhonetic|String|否|""| **命名参数。** 联系人的家庭姓名拼音。|
|fullName|String|否|""| **命名参数。** 联系人的全名。|
|givenName|String|否|""| **命名参数。** 联系人的名称（firstName）。|
|givenNamePhonetic|String|否|""| **命名参数。** 联系人的名称拼音。|
|middleName|String|否|""| **命名参数。** 联系人的中间名。|
|middleNamePhonetic|String|否|""| **命名参数。** 联系人的中间名拼音。|
|namePrefix|String|否|""| **命名参数。** 联系人的姓名前缀。|
|nameSuffix|String|否|""| **命名参数。** 联系人的姓名后缀。|