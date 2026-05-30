## struct DocumentSaveOptions

```cangjie
public struct DocumentSaveOptions {
    public DocumentSaveOptions(
        public var newFileNames!: Array<String> = Array<String>(),
        public var defaultFilePathUri!: ?String = None,
        public var fileSuffixChoices!: Array<String> = Array<String>(),
        public var pickerMode!: DocumentPickerMode = DocumentPickerMode.DEFAULT
    )
}
```

**功能：** 文档保存选项。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### var defaultFilePathUri

```cangjie
public var defaultFilePathUri: ?String = None
```

**功能：** 指定保存的文件或者目录路径。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 12

### var fileSuffixChoices

```cangjie
public var fileSuffixChoices: Array<String> = Array<String>()
```

**功能：** 保存文件的后缀类型。传入字符串数组，每一项代表一个后缀选项，每一项内部用。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var newFileNames

```cangjie
public var newFileNames: Array<String> = Array<String>()
```

**功能：** 拉起documentPicker进行保存的文件名，若无此参数，则默认需要用户自行输入。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### var pickerMode

```cangjie
public var pickerMode: DocumentPickerMode = DocumentPickerMode.DEFAULT
```

**功能：** 拉起picker的类型，默认为DEFAULT。当pickerMode设置为DOWNLOAD时，用户配置的参数newFileNames、defaultFilePathUri和fileSuffixChoices将不会生效。

**类型：** [DocumentPickerMode](#enum-documentpickermode)

**读写能力：** 可读写

**起始版本：** 12

### DocumentSaveOptions(Array\<String>, ?String, Array\<String>, DocumentPickerMode)

```cangjie
public DocumentSaveOptions(
   public var newFileNames!: Array<String> = Array<String>(),
   public var defaultFilePathUri!: ?String = None,
   public var fileSuffixChoices!: Array<String> = Array<String>(),
   public var pickerMode!: DocumentPickerMode = DocumentPickerMode.DEFAULT
)
```

**功能：** 创建DocumentSaveOptions对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newFileNames|Array\<String>|否|Array\<String>()| **命名参数。** 拉起documentPicker进行保存的文件名，若无此参数，则默认需要用户自行输入。|
|defaultFilePathUri|?String|否|None| **命名参数。** 指定保存的文件或者目录路径。|
|fileSuffixChoices|Array\<String>|否|Array\<String>()| **命名参数。** 保存文件的后缀类型。传入字符串数组，每一项代表一个后缀选项，每一项内部用。|
|pickerMode|[DocumentPickerMode](#enum-documentpickermode)|否|DocumentPickerMode.DEFAULT| **命名参数。** 拉起picker的类型，默认为DEFAULT。当pickerMode设置为DOWNLOAD时，用户配置的参数newFileNames、defaultFilePathUri和fileSuffixChoices将不会生效。|