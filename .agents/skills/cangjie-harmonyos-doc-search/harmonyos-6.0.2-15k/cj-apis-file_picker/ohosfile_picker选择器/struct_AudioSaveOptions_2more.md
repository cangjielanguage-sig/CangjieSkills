## struct AudioSaveOptions

```cangjie
public struct AudioSaveOptions {
    public AudioSaveOptions(
        public var newFileNames!: Array<String> = Array<String>()
    )
}
```

**功能：** 音频的保存选项。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### var newFileNames

```cangjie
public var newFileNames: Array<String> = Array<String>()
```

**功能：** 拉起audioPicker进行保存音频资源的文件名，若无此参数，则默认需要用户自行输入。

**类型：** Array\<String>

**读写能力：** 可读写

**起始版本：** 12

### AudioSaveOptions(Array\<String>)

```cangjie
public AudioSaveOptions(
    public var newFileNames!: Array<String> = Array<String>()
)
```

**功能：** 创建AudioSaveOptions对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|newFileNames|Array\<String>|否|Array\<String>()| **命名参数。** 拉起audioPicker进行保存音频资源的文件名，若无此参数，则默认需要用户自行输入。|

## struct AudioSelectOptions

```cangjie
public struct AudioSelectOptions {
    public AudioSelectOptions(public var maxSelectNumber!: Int64 = 1) {}
}
```

**功能：** 音频选择选项。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

### var maxSelectNumber

```cangjie
public var maxSelectNumber: Int64 = 1
```

**功能：** 选择文件最大个数，有效值范围1-500。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 12

### AudioSelectOptions(Int64)

```cangjie
public AudioSelectOptions(
    public var maxSelectNumber!: Int64 = 1
)
```

**功能：** 创建AudioSelectOptions对象。

**系统能力：** SystemCapability.FileManagement.UserFileService

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maxSelectNumber|Int64|否|1| **命名参数。** 选择文件最大个数，有效值范围1-500。|