## class PhoneNumberFormatOptions

```cangjie
public class PhoneNumberFormatOptions {
    public PhoneNumberFormatOptions(
        public let formatType: ?String = None
    )
}
```

**功能：** 电话号码格式化时可设置的配置项。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### let formatType

```cangjie
public let formatType: ?String = None
```

**功能：** 表示对电话号码格式化的类型，取值包括："E164", "INTERNATIONAL", "NATIONAL", "RFC3966", "TYPING"。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### PhoneNumberFormatOptions(?String)

```cangjie
public PhoneNumberFormatOptions(
    public let formatType: ?String = None
)
```

**功能：** 构造PhoneNumberFormatOptions对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|formatType|?String|否|None|表示对电话号码格式化的类型，取值包括："E164", "INTERNATIONAL", "NATIONAL", "RFC3966", "TYPING"。|