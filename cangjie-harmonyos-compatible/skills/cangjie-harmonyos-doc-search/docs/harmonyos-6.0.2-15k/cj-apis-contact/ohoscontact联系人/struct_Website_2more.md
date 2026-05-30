## struct Website

```cangjie
public struct Website {
    public Website(
        public let website: String)
}
```

**功能：** 联系人的网站信息类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### let website

```cangjie
public let website: String
```

**功能：** 联系人的网站信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### Website(String)

```cangjie
public Website(
    public let website: String)
```

**功能：** 创建Website实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|website|String|是|-|联系人的网站信息。|

## enum Attribute

```cangjie
public enum Attribute {
    | ATTR_CONTACT_EVENT
    | ATTR_EMAIL
    | ATTR_GROUP_MEMBERSHIP
    | ATTR_IM
    | ATTR_NAME
    | ATTR_NICKNAME
    | ATTR_NOTE
    | ATTR_ORGANIZATION
    | ATTR_PHONE
    | ATTR_PORTRAIT
    | ATTR_POSTAL_ADDRESS
    | ATTR_RELATION
    | ATTR_SIP_ADDRESS
    | ATTR_WEBSITE
    | ...
}
```

**功能：** 联系人属性列表。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### ATTR_CONTACT_EVENT

```cangjie
ATTR_CONTACT_EVENT
```

**功能：** 联系人的生日、周年纪念等重要日期。

**起始版本：** 19

### ATTR_EMAIL

```cangjie
ATTR_EMAIL
```

**功能：** 联系人的邮箱地址。

**起始版本：** 19

### ATTR_GROUP_MEMBERSHIP

```cangjie
ATTR_GROUP_MEMBERSHIP
```

**功能：** 联系人的群组。

**起始版本：** 19

### ATTR_IM

```cangjie
ATTR_IM
```

**功能：** 联系人的即时消息地址。

**起始版本：** 19

### ATTR_NAME

```cangjie
ATTR_NAME
```

**功能：** 联系人的姓名。

**起始版本：** 19

### ATTR_NICKNAME

```cangjie
ATTR_NICKNAME
```

**功能：** 联系人的昵称。

**起始版本：** 19

### ATTR_NOTE

```cangjie
ATTR_NOTE
```

**功能：** 联系人的备注。

**起始版本：** 19

### ATTR_ORGANIZATION

```cangjie
ATTR_ORGANIZATION
```

**功能：** 联系人的组织信息。

**起始版本：** 19

### ATTR_PHONE

```cangjie
ATTR_PHONE
```

**功能：** 联系人的电话号码。

**起始版本：** 19

### ATTR_PORTRAIT

```cangjie
ATTR_PORTRAIT
```

**功能：** 联系人的头像。

**起始版本：** 19

### ATTR_POSTAL_ADDRESS

```cangjie
ATTR_POSTAL_ADDRESS
```

**功能：** 联系人的邮政地址。

**起始版本：** 19

### ATTR_RELATION

```cangjie
ATTR_RELATION
```

**功能：** 联系人的关系。

**起始版本：** 19

### ATTR_SIP_ADDRESS

```cangjie
ATTR_SIP_ADDRESS
```

**功能：** 联系人的会话发起协议（SIP）地址。

**起始版本：** 19

### ATTR_WEBSITE

```cangjie
ATTR_WEBSITE
```

**功能：** 联系人的网站。

**起始版本：** 19