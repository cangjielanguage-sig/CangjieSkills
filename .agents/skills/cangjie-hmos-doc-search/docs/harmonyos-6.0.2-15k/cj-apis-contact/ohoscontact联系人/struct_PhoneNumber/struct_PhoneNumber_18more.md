## struct PhoneNumber

```cangjie
public struct PhoneNumber {
    public static const INVALID_LABEL_ID: Int32 = - 1
    public static const CUSTOM_LABEL: Int32 = 0
    public static const NUM_HOME: Int32 = 1
    public static const NUM_MOBILE: Int32 = 2
    public static const NUM_WORK: Int32 = 3
    public static const NUM_FAX_WORK: Int32 = 4
    public static const NUM_FAX_HOME: Int32 = 5
    public static const NUM_PAGER: Int32 = 6
    public static const NUM_OTHER: Int32 = 7
    public static const NUM_CALLBACK: Int32 = 8
    public static const NUM_CAR: Int32 = 9
    public static const NUM_COMPANY_MAIN: Int32 = 10
    public static const NUM_ISDN: Int32 = 11
    public static const NUM_MAIN: Int32 = 12
    public static const NUM_OTHER_FAX: Int32 = 13
    public static const NUM_RADIO: Int32 = 14
    public static const NUM_TELEX: Int32 = 15
    public static const NUM_TTY_TDD: Int32 = 16
    public static const NUM_WORK_MOBILE: Int32 = 17
    public static const NUM_WORK_PAGER: Int32 = 18
    public static const NUM_ASSISTANT: Int32 = 19
    public static const NUM_MMS: Int32 = 20
    public PhoneNumber(
        public var phoneNumber: String,
        public var labelName!: String = "",
        public var labelId!: Int32 = INVALID_LABEL_ID
    )
}
```

**功能：** 联系人电话号码类。

**系统能力：** SystemCapability.Applications.ContactsData

**起始版本：** 19

### static const CUSTOM_LABEL

```cangjie
public static const CUSTOM_LABEL: Int32 = 0
```

**功能：** 自定义电话类型。

**类型：** Int32

**起始版本：** 19

### static const INVALID_LABEL_ID

```cangjie
public static const INVALID_LABEL_ID: Int32 = - 1
```

**功能：** 无效电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_ASSISTANT

```cangjie
public static const NUM_ASSISTANT: Int32 = 19
```

**功能：** 助理电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_CALLBACK

```cangjie
public static const NUM_CALLBACK: Int32 = 8
```

**功能：** 回呼电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_CAR

```cangjie
public static const NUM_CAR: Int32 = 9
```

**功能：** 车机电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_COMPANY_MAIN

```cangjie
public static const NUM_COMPANY_MAIN: Int32 = 10
```

**功能：** 公司电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_FAX_HOME

```cangjie
public static const NUM_FAX_HOME: Int32 = 5
```

**功能：** 家庭传真电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_FAX_WORK

```cangjie
public static const NUM_FAX_WORK: Int32 = 4
```

**功能：** 工作传真电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_HOME

```cangjie
public static const NUM_HOME: Int32 = 1
```

**功能：** 家庭电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_ISDN

```cangjie
public static const NUM_ISDN: Int32 = 11
```

**功能：** 综合业务数字网（ISDN）电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_MAIN

```cangjie
public static const NUM_MAIN: Int32 = 12
```

**功能：** 主电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_MMS

```cangjie
public static const NUM_MMS: Int32 = 20
```

**功能：** 彩信电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_MOBILE

```cangjie
public static const NUM_MOBILE: Int32 = 2
```

**功能：** 移动电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_OTHER

```cangjie
public static const NUM_OTHER: Int32 = 7
```

**功能：** 其它电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_OTHER_FAX

```cangjie
public static const NUM_OTHER_FAX: Int32 = 13
```

**功能：** 其它传真类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_PAGER

```cangjie
public static const NUM_PAGER: Int32 = 6
```

**功能：** 寻呼机电话类型。

**类型：** Int32

**起始版本：** 19

### static const NUM_RADIO

```cangjie
public static const NUM_RADIO: Int32 = 14
```

**功能：** 无线电话类型。

**类型：** Int32

**起始版本：** 19