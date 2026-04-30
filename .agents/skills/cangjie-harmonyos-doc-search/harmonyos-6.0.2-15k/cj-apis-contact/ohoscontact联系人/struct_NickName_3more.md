## struct NickName

```cangjie
public struct NickName {
    public NickName(
        public let nickName: String)
}
```

**功能：** 联系人的昵称类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### let nickName

```cangjie
public let nickName: String
```

**功能：** 联系人的昵称类。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### NickName(String)

```cangjie
public NickName(
    public let nickName: String)
```

**功能：** 创建NickName实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|nickName|String|是|-|联系人的昵称。|

## struct Note

```cangjie
public struct Note {
    public Note(
        public let noteContent: String)
}
```

**功能：** 联系人的备注类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### let noteContent

```cangjie
public let noteContent: String
```

**功能：** 联系人的备注内容。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### Note(String)

```cangjie
public Note(
    public let noteContent: String)
```

**功能：** 创建Note实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|noteContent|String|是|-|联系人的备注内容。|

## struct Organization

```cangjie
public struct Organization {
    public Organization(
        public var name!: String = "",
        public var title!: String = ""
    )
}
```

**功能：** 联系人的组织类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### var name

```cangjie
public var name: String = ""
```

**功能：** 单位名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: String = ""
```

**功能：** 职位名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Organization(String, String)

```cangjie
public Organization(
    public var name!: String = "",
    public var title!: String = ""
)
```

**功能：** 创建Organization实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|否|""| **命名参数。** 单位名称。|
|title|String|否|""| **命名参数。** 职位名称。|