## func updateContact(Context, Contact, ContactAttributes)

```cangjie
public func updateContact(context: Context, contact: Contact, attrs!: ContactAttributes = ContactAttributes.ALL): Unit
```

**功能：** 更新联系人，当不存在要更新的联系人时会抛出401异常。

**需要权限：** ohos.permission.WRITE_CONTACTS和ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[Context](../AbilityKit/cj-apis-ability.md#class-context)|是|-|应用上下文Context。|
|contact|[Contact](#struct-contact)|是|-|联系人信息，其中需包含联系人id，否则抛出401异常。|
|attrs|[ContactAttributes](#struct-contactattributes)|否|ContactAttributes.ALL| **命名参数。** 联系人的属性列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ContactsKit.*

let contact = Contact(id: 1, name: Name(fullName: "new"))
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
updateContact(abilityContext, contact, attrs: ContactAttributes([Attribute.ATTR_NAME]))
```

## class ContactSelectOptions

```cangjie
public class ContactSelectOptions {
    public ContactSelectOptions(
        public var isMultiSelect!: Bool = false)
}
```

**功能：** 选择联系人条件。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### var isMultiSelect

```cangjie
public var isMultiSelect: Bool = false
```

**功能：** 是否为多选。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### ContactSelectOptions(Bool)

```cangjie
public ContactSelectOptions(
    public var isMultiSelect!: Bool = false)
```

**功能：** 创建ContactSelectOptions实例。

**系统能力：** SystemCapability.Applications.Contacts

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isMultiSelect|Bool|否|false| **命名参数。** 是否为多选。|