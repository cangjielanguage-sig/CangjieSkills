## struct Contact

```cangjie
public struct Contact {
    public static const INVALID_CONTACT_ID: Int64 = - 1
    public Contact(
        public var id!: Int64 = INVALID_CONTACT_ID,
        public var key!: String = "",
        public var name!: Name = Name(),
        public var nickName!: NickName = NickName(""),
        public var note!: Note = Note(""),
        public var organization!: Organization = Organization(),
        public var portrait!: Portrait = Portrait(""),
        public var emails!: ArrayList<Email> = ArrayList<Email>(),
        public var events!: ArrayList<Event> = ArrayList<Event>(),
        public var groups!: ArrayList<Group> = ArrayList<Group>(),
        public var imAddresses!: ArrayList<ImAddress> = ArrayList<ImAddress>(),
        public var phoneNumbers!: ArrayList<PhoneNumber> = ArrayList<PhoneNumber>(),
        public var postalAddresses!: ArrayList<PostalAddress> = ArrayList<PostalAddress>(),
        public var relations!: ArrayList<Relation> = ArrayList<Relation>(),
        public var sipAddresses!: ArrayList<SipAddress> = ArrayList<SipAddress>(),
        public var websites!: ArrayList<Website> = ArrayList<Website>()
    )
}
```

**功能：** 联系人对象类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const INVALID_CONTACT_ID

```cangjie
public static const INVALID_CONTACT_ID: Int64 = - 1
```

**功能：** 默认联系人的id。

**类型：** Int64

**起始版本：** 19

### var emails

```cangjie
public var emails: ArrayList<Email> = ArrayList<Email>()
```

**功能：** 联系人的邮箱地址列表。

**类型：** ArrayList\<[Email](#struct-email)>

**读写能力：** 可读写

**起始版本：** 19

### var events

```cangjie
public var events: ArrayList<Event> = ArrayList<Event>()
```

**功能：** 联系人的生日、周年纪念等重要日期列表。

**类型：** ArrayList\<[Event](#struct-event)>

**读写能力：** 可读写

**起始版本：** 19

### var groups

```cangjie
public var groups: ArrayList<Group> = ArrayList<Group>()
```

**功能：** 联系人的群组列表。

**类型：** ArrayList\<[Group](#struct-group)>

**读写能力：** 可读写

**起始版本：** 19

### var id

```cangjie
public var id: Int64 = INVALID_CONTACT_ID
```

**功能：** 联系人的id。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var imAddresses

```cangjie
public var imAddresses: ArrayList<ImAddress> = ArrayList<ImAddress>()
```

**功能：** 联系人的即时消息地址列表。

**类型：** ArrayList\<[ImAddress](#struct-imaddress)>

**读写能力：** 可读写

**起始版本：** 19

### var key

```cangjie
public var key: String = ""
```

**功能：** 联系人的key。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var name

```cangjie
public var name: Name = Name()
```

**功能：** 联系人的姓名。

**类型：** [Name](#struct-name)

**读写能力：** 可读写

**起始版本：** 19

### var nickName

```cangjie
public var nickName: NickName = NickName("")
```

**功能：** 联系人的昵称。

**类型：** [NickName](#struct-nickname)

**读写能力：** 可读写

**起始版本：** 19

### var note

```cangjie
public var note: Note = Note("")
```

**功能：** 联系人的备注。

**类型：** [Note](#struct-note)

**读写能力：** 可读写

**起始版本：** 19

### var organization

```cangjie
public var organization: Organization = Organization()
```

**功能：** 联系人的组织信息。

**类型：** [Organization](#struct-organization)

**读写能力：** 可读写

**起始版本：** 19

### var phoneNumbers

```cangjie
public var phoneNumbers: ArrayList<PhoneNumber> = ArrayList<PhoneNumber>()
```

**功能：** 联系人的电话号码列表。

**类型：** ArrayList\<[PhoneNumber](#struct-phonenumber)>

**读写能力：** 可读写

**起始版本：** 19

### var portrait

```cangjie
public var portrait: Portrait = Portrait("")
```

**功能：** 联系人的头像。

**类型：** [Portrait](#struct-portrait)

**读写能力：** 可读写

**起始版本：** 19