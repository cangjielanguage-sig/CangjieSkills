## struct Relation

```cangjie
public struct Relation {
    public static const INVALID_LABEL_ID: Int32 = - 1
    public static const CUSTOM_LABEL: Int32 = 0
    public static const RELATION_ASSISTANT: Int32 = 1
    public static const RELATION_BROTHER: Int32 = 2
    public static const RELATION_CHILD: Int32 = 3
    public static const RELATION_DOMESTIC_PARTNER: Int32 = 4
    public static const RELATION_FATHER: Int32 = 5
    public static const RELATION_FRIEND: Int32 = 6
    public static const RELATION_MANAGER: Int32 = 7
    public static const RELATION_MOTHER: Int32 = 8
    public static const RELATION_PARENT: Int32 = 9
    public static const RELATION_PARTNER: Int32 = 10
    public static const RELATION_REFERRED_BY: Int32 = 11
    public static const RELATION_RELATIVE: Int32 = 12
    public static const RELATION_SISTER: Int32 = 13
    public static const RELATION_SPOUSE: Int32 = 14
    public Relation(
        public var relationName: String,
        public var labelName!: String = "",
        public var labelId!: Int32 = INVALID_LABEL_ID
    )
}
```

**功能：** 联系人的关系类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const CUSTOM_LABEL

```cangjie
public static const CUSTOM_LABEL: Int32 = 0
```

**功能：** 自定义关系类型。

**类型：** Int32

**起始版本：** 19

### static const INVALID_LABEL_ID

```cangjie
public static const INVALID_LABEL_ID: Int32 = - 1
```

**功能：** 无效的关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_ASSISTANT

```cangjie
public static const RELATION_ASSISTANT: Int32 = 1
```

**功能：** 助手关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_BROTHER

```cangjie
public static const RELATION_BROTHER: Int32 = 2
```

**功能：** 兄弟关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_CHILD

```cangjie
public static const RELATION_CHILD: Int32 = 3
```

**功能：** 子女关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_DOMESTIC_PARTNER

```cangjie
public static const RELATION_DOMESTIC_PARTNER: Int32 = 4
```

**功能：** 同居同伴关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_FATHER

```cangjie
public static const RELATION_FATHER: Int32 = 5
```

**功能：** 父亲关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_FRIEND

```cangjie
public static const RELATION_FRIEND: Int32 = 6
```

**功能：** 朋友关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_MANAGER

```cangjie
public static const RELATION_MANAGER: Int32 = 7
```

**功能：** 管理者关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_MOTHER

```cangjie
public static const RELATION_MOTHER: Int32 = 8
```

**功能：** 母亲关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_PARENT

```cangjie
public static const RELATION_PARENT: Int32 = 9
```

**功能：** 父母关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_PARTNER

```cangjie
public static const RELATION_PARTNER: Int32 = 10
```

**功能：** 合作伙伴关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_REFERRED_BY

```cangjie
public static const RELATION_REFERRED_BY: Int32 = 11
```

**功能：** 推荐人关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_RELATIVE

```cangjie
public static const RELATION_RELATIVE: Int32 = 12
```

**功能：** 亲属关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_SISTER

```cangjie
public static const RELATION_SISTER: Int32 = 13
```

**功能：** 姐妹关系类型。

**类型：** Int32

**起始版本：** 19

### static const RELATION_SPOUSE

```cangjie
public static const RELATION_SPOUSE: Int32 = 14
```

**功能：** 配偶关系类型。

**类型：** Int32

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32 = INVALID_LABEL_ID
```

**功能：** 关系类型ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19