### static const NUM_TELEX

```cangjie
public static const NUM_TELEX: Int32 = 15
```

**功能：** 电传电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_TTY_TDD

```cangjie
public static const NUM_TTY_TDD: Int32 = 16
```

**功能：** 电传打字机（TTY）或测试驱动开发（TDD）电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_WORK

```cangjie
public static const NUM_WORK: Int32 = 3
```

**功能：** 工作电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_WORK_MOBILE

```cangjie
public static const NUM_WORK_MOBILE: Int32 = 17
```

**功能：** 工作移动电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_WORK_PAGER

```cangjie
public static const NUM_WORK_PAGER: Int32 = 18
```

**功能：** 工作寻呼机电话类型。

**类型：** Int32

**起始版本：** 19

### var labelId

```cangjie
public var labelId: Int32 = INVALID_LABEL_ID
```

**功能：** 电话号码类型ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var labelName

```cangjie
public var labelName: String = ""
```

**功能：** 电话号码类型名称。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var phoneNumber

```cangjie
public var phoneNumber: String
```

**功能：** 电话号码。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### PhoneNumber(String, String, Int32)

```cangjie
public PhoneNumber(
    public var phoneNumber: String,
    public var labelName!: String = "",
    public var labelId!: Int32 = INVALID_LABEL_ID
)
```

**功能：** 创建PhoneNumber实例。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|phoneNumber|String|是|-|电话号码。|
|labelName|String|否|""| **命名参数。** 电话号码类型名称。|
|labelId|Int32|否|INVALID_LABEL_ID| **命名参数。** 电话号码类型ID。|