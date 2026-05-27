### Contact(Int64, String, Name, NickName, Note, Organization, Portrait, ArrayList\<Email>, ArrayList\<Event>, ArrayList\<Group>, ArrayList\<ImAddress>, ArrayList\<PhoneNumber>, ArrayList\<PostalAddress>, ArrayList\<Relation>, ArrayList\<SipAddress>, ArrayList\<Website>)

```cangjie
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
```

**功能：** 创建Contact实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int64|否|INVALID_CONTACT_ID| **命名参数。** 联系人的id。|
|key|String|否|""| **命名参数。** 联系人的key。|
|name|[Name](#struct-name)|否|Name()| **命名参数。** 联系人的姓名。|
|nickName|[NickName](#struct-nickname)|否|NickName("")| **命名参数。** 联系人的昵称。|
|note|[Note](#struct-note)|否|Note("")| **命名参数。** 联系人的备注。|
|organization|[Organization](#struct-organization)|否|Organization()| **命名参数。** 联系人的组织信息。|
|portrait|[Portrait](#struct-portrait)|否|Portrait("")| **命名参数。** 联系人的头像。|
|emails|ArrayList\<[Email](#struct-email)>|否|ArrayList\<Email>()| **命名参数。** 联系人的邮箱地址列表。|
|events|ArrayList\<[Event](#struct-event)>|否|ArrayList\<Event>()| **命名参数。** 联系人的生日、周年纪念等重要日期列表。|
|groups|ArrayList\<[Group](#struct-group)>|否|ArrayList\<Group>()| **命名参数。** 联系人的群组列表。|
|imAddresses|ArrayList\<[ImAddress](#struct-imaddress)>|否|ArrayList\<ImAddress>()| **命名参数。** 联系人的即时消息地址列表。|
|phoneNumbers|ArrayList\<[PhoneNumber](#struct-phonenumber)>|否|ArrayList\<PhoneNumber>()| **命名参数。** 联系人的电话号码列表。|
|postalAddresses|ArrayList\<[PostalAddress](#struct-postaladdress)>|否|ArrayList\<PostalAddress>()| **命名参数。** 联系人的邮政地址列表。|
|relations|ArrayList\<[Relation](#struct-relation)>|否|ArrayList\<Relation>()| **命名参数。** 联系人的关系列表。|
|sipAddresses|ArrayList\<[SipAddress](#struct-sipaddress)>|否|ArrayList\<SipAddress>()| **命名参数。** 联系人的会话发起协议（SIP）地址列表。|
|websites|ArrayList\<[Website](#struct-website)>|否|ArrayList\<Website>()| **命名参数。** 联系人的网站列表。|