## class Options

```cangjie
public open class Options {
    public var encoding: String
    public init(
        encoding!: String = "utf-8"
    )
}
```

**功能：** 可选项类型，支持readLines接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### var encoding

```cangjie
public var encoding: String
```

**功能：** 文件编码方式。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### init(String)

```cangjie
public init(
    encoding!: String = "utf-8"
)
```

**功能：** 构造Options对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|encoding|String|否|"utf-8"|**命名参数。** 文件编码方式。可选项。|