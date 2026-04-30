## struct Group

```cangjie
public struct Group {
    public Group(
        public var title: String,
        public var groupId!: Int64 = INVALID_GROUP_ID
    )
}
```

**功能：** 联系人的群组类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### var groupId

```cangjie
public var groupId: Int64 = INVALID_GROUP_ID
```

**功能：** 联系人群组的ID。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: String
```

**功能：** 联系人群组的名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Group(String, Int64)

```cangjie
public Group(
    public var title: String,
    public var groupId!: Int64 = INVALID_GROUP_ID
)
```

**功能：** 创建Group实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|String|是|-|联系人群组的名称。|
|groupId|Int64|否|INVALID_GROUP_ID| **命名参数。** 联系人群组的ID。|

## struct Holder

```cangjie
public struct Holder {
    public Holder(
        public var displayName: String,
        public var holderId: Int64,
        public var bundleName!: String = BUNDLE_NAME_DEFAULT
    )
}
```

**功能：** 创建联系人的应用信息类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### var bundleName

```cangjie
public var bundleName: String = BUNDLE_NAME_DEFAULT
```

**功能：** Bundle名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var displayName

```cangjie
public var displayName: String
```

**功能：** 应用名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var holderId

```cangjie
public var holderId: Int64
```

**功能：** 应用ID。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 19

### Holder(String, Int64, String)

```cangjie
public Holder(
    public var displayName: String,
    public var holderId: Int64,
    public var bundleName!: String = BUNDLE_NAME_DEFAULT
)
```

**功能：** 创建Holder实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|displayName|String|是|-|应用名称。|
|holderId|Int64|是|-|应用ID。|
|bundleName|String|否|BUNDLE_NAME_DEFAULT| **命名参数。** Bundle名称。|