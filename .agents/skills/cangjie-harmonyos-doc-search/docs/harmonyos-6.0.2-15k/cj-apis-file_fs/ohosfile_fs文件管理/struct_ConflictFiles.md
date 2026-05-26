## struct ConflictFiles

```cangjie
public struct ConflictFiles {
    public ConflictFiles(
        public let srcFile: String,
        public let destFile: String
    )
}
```

**功能：** 冲突文件信息，支持copyDir及moveDir接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### let destFile

```cangjie
public let destFile: String
```

**功能：** 目标冲突文件路径。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let srcFile

```cangjie
public let srcFile: String
```

**功能：** 源冲突文件路径。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### ConflictFiles(String, String)

```cangjie
public ConflictFiles(
    public let srcFile: String,
    public let destFile: String
)
```

**功能：** 构造ConflictFiles对象。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|srcFile|String|是|-|源冲突文件路径。|
|destFile|String|是|-|目标冲突文件路径。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[文件管理错误码](../../errorcodes/cj-errorcode-filemanagement.md#文件管理错误码)。