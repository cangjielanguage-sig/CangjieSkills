## struct PasteDataProperty

```cangjie
public struct PasteDataProperty {
    public PasteDataProperty(
        public var mimeTypes: Array<String>,
        public var tag: String,
        public var timestamp: Int64,
        public var localOnly!: Bool = false,
        public var shareOption!: ShareOption = CROSSDEVICE
    )
}
```

**功能：** 定义了剪贴板中所有内容条目的属性，包含时间戳、数据类型、粘贴范围以及一些附加数据等。 该属性必须通过setProperty方法，才能设置到剪贴板中。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

### var localOnly

```cangjie
public var localOnly: Bool = false
```

**功能：** 配置剪贴板内容是否为“仅在本地”。

配置为true时，表示内容仅在本地，不会在设备之间传递。配置为false时，表示内容将在设备间传递。其功能会被shareOption属性覆盖，推荐使用shareOption。默认false。

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 12

### var mimeTypes

```cangjie
public var mimeTypes: Array<String>
```

**功能：** 剪贴板内容条目的数据类型，非重复的类型列表。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var shareOption

```cangjie
public var shareOption: ShareOption = CROSSDEVICE
```

**功能：** 指示剪贴板数据可以粘贴到的范围，如果未设置或设置不正确，则默认值为CROSSDEVICE。

**类型：** [ShareOption](#enum-shareoption)

**读写能力：** 可读写

**起始版本：** 12

### var tag

```cangjie
public var tag: String
```

**功能：** 用户自定义标签。

**类型：** String

**读写能力：** 可读写

**起始版本：** 12

### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 剪贴板数据的写入时间戳（单位：ms）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

### PasteDataProperty(Array\<String>, String, Int64, Bool, ShareOption)

```cangjie
public PasteDataProperty(
    public var mimeTypes: Array<String>,
    public var tag: String,
    public var timestamp: Int64,
    public var localOnly!: Bool = false,
    public var shareOption!: ShareOption = CROSSDEVICE
)
```

**功能：** PasteDataProperty的构造函数。

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mimeTypes|Array\<String>|是|-|剪贴板内容条目的数据类型，非重复的类型列表。|
|tag|String|是|-|用户自定义标签。|
|timestamp|Int64|是|-|剪贴板数据的写入时间戳（单位：ms）。|
|localOnly|Bool|否|false| **命名参数。** 配置剪贴板内容是否为“仅在本地”，默认false。其功能会被shareOption属性覆盖，推荐使用shareOption。|
|shareOption|[ShareOption](#enum-shareoption)|否|CROSSDEVICE| **命名参数。** 指示剪贴板数据可以粘贴到的范围，如果未设置或设置不正确，则默认值为CROSSDEVICE。|