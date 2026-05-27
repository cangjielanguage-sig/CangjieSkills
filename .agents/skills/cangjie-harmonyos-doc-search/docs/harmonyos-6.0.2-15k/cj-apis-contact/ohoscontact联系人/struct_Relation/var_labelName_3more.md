### var labelName

```cangjie
public var labelName: String = ""
```

**功能：** 关系类型名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var relationName

```cangjie
public var relationName: String
```

**功能：** 关系名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### Relation(String, String, Int32)

```cangjie
public Relation(
    public var relationName: String,
    public var labelName!: String = "",
    public var labelId!: Int32 = INVALID_LABEL_ID
)
```

**功能：** 创建Relation实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|relationName|String|是|-|关系名称。|
|labelName|String|否|""| **命名参数。** 关系类型名称。|
|labelId|Int32|否|INVALID_LABEL_ID| **命名参数。** 关系类型ID。|