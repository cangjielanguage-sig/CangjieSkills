## class HolidayInfoItem

```cangjie
public class HolidayInfoItem {}
```

**功能：** 节假日信息。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### let baseName

```cangjie
public let baseName: String
```

**功能：** 节假日的英文名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let day

```cangjie
public let day: Int32
```

**功能：** 节假日所在日。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let localNames

```cangjie
public let localNames: ?Array<HolidayLocalName>
```

**功能：** 节假日的本地名称列表。

**类型：** ?Array\<[HolidayLocalName](#class-holidaylocalname)>

**读写能力：** 只读

**起始版本：** 19

### let month

```cangjie
public let month: Int32
```

**功能：** 节假日所在月。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let year

```cangjie
public let year: Int32
```

**功能：** 节假日所在年。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

## class HolidayLocalName

```cangjie
public class HolidayLocalName {
    public HolidayLocalName(
        public let name: String,
        public let language: String
    )
}
```

**功能：** 节假日本地名称。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### let language

```cangjie
public let language: String
```

**功能：** 节假日的本地语言，例如ar，en，tr。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 节假日的本地名称，例如Sacrifice Feast（宰牲节）的土耳其语名称为Kurban Bayrami。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### HolidayLocalName(String, String)

```cangjie
public HolidayLocalName(
    public let name: String,
    public let language: String
)
```

**功能：** 构造一个节假日本地名称对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|节假日的本地名称，例如Sacrifice Feast（宰牲节）的土耳其语名称为Kurban Bayrami。|
|language|String|是|-|节假日的本地语言，例如ar，en，tr。|