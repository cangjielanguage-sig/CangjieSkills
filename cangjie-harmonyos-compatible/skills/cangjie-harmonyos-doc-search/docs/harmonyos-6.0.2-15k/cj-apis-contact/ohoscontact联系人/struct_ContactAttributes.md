## struct ContactAttributes

```cangjie
public struct ContactAttributes {
    public static let ALL: ContactAttributes = ContactAttributes(ALL_ATTRIBUTES)
    public ContactAttributes(attributes: Array<Attribute>)
}
```

**功能：** 联系人属性列表，一般作为入参用来标识希望查询的联系人属性。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static let ALL

```cangjie
public static let ALL: ContactAttributes = ContactAttributes(ALL_ATTRIBUTES)
```

**功能：** 全部联系人属性，一般作为入参标识希望查询所有联系人属性。

**类型：** [ContactAttributes](#struct-contactattributes)

**起始版本：** 19

### ContactAttributes(Array\<Attribute>)

```cangjie
public ContactAttributes(attributes: Array<Attribute>)
```

**功能：** 构造ContactAttributes对象。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|attributes|Array\<[Attribute](#enum-attribute)>|是|-|联系人属性列表。|