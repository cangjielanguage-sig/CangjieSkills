## class Image

```cangjie
public class Image <: File {}
```

**功能：** 图片类型数据，用于描述图片文件。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**父类型：**

- [File](#class-file)

### prop imageUri

```cangjie
public mut prop imageUri: String
```

**功能：** 本地图片数据uri或网络图片uri。本地图片数据uri可通过[getUriFromPath](../../apis/CoreFileKit/cj-apis-file_fileuri.md#static-func-geturifrompathstring)函数获取。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20

## class Options

```cangjie
public class Options {
    public var intention: Intention = Intention.DATA_HUB,
    public var key: String = ""
    public init(intention!: Intention = Intention.DATA_HUB, key!: String = "")
}
```

**功能：** UDMF提供的数据操作接口可选项。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

### var intention

```cangjie
public var intention: Intention
```

**功能：** 表示数据操作相关的数据通路类型。

**类型：** [Intention](#enum-intention)

**读写能力：** 可读写

**起始版本：** 19

### var key

```cangjie
public var key: String
```

**功能：** UDMF中数据对象的唯一标识符。

由udmf:/、intention、bundleName和groupId四部分组成，以'/'连接，比如：udmf://DataHub/com.ohos.test/0123456789。其中udmf:/固定，DataHub为对应枚举的取值，com.ohos.test为包名，0123456789为随机生成的groupId。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### init(Intention, String)

```cangjie
public init(intention!: Intention = Intention.DATA_HUB, key!: String = "")
```

**功能：** Options的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|intention|[Intention](#enum-intention)|是|-| **命名参数。** 表示数据操作相关的数据通路类型。|
|key|String|是|-| **命名参数。** UDMF中数据对象的唯一标识符。<br>由udmf:/、intention、bundleName和groupId四部分组成，以'/'连接，比如：udmf://DataHub/com.ohos.test/0123456789。<br>其中udmf:/固定，DataHub为对应枚举的取值，com.ohos.test为包名，0123456789为随机生成的groupId。|

## class PlainText

```cangjie
public class PlainText <: Text {}
```

**功能：** 纯文本类型数据，用于描述纯文本类型数据。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**父类型：**

- [Text](#class-text)

### prop \`abstract`

```cangjie
public mut prop `abstract`: String
```

**功能：** 纯文本摘要，默认值为空字符串。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20

### prop textContent

```cangjie
public mut prop textContent: String
```

**功能：** 纯文本内容。

**类型：** String

**读写能力：** 可读写。

**起始版本：** 20

## class Text

```cangjie
public open class Text <: UnifiedRecord {}
```

**功能：** 文本类型数据，也是文本类型数据的基类，用于描述文本类数据。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

**起始版本：** 20

**父类型：**

- [UnifiedRecord](#class-unifiedrecord)

### prop details

```cangjie
public mut prop details: HashMap<String, String>
```

**功能：** 是一个字典类型对象，key和value都是String类型，用于描述文本内容。

**类型：** HashMap\<String, String>

**读写能力：** 可读写。

**起始版本：** 20