## enum WhenceType

```cangjie
public enum WhenceType {
    | SEEK_SET
    | SEEK_CUR
    | SEEK_END
    | ...
}
```

**功能：** 文件偏移指针相对偏移位置类型，支持lseek接口使用。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### SEEK_CUR

```cangjie
SEEK_CUR
```

**功能：** 当前文件偏置指针位置处。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### SEEK_END

```cangjie
SEEK_END
```

**功能：** 文件末尾位置处。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### SEEK_SET

```cangjie
SEEK_SET
```

**功能：** 文件起始位置处。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### prop whenceType

```cangjie
public prop whenceType: Int32
```

**功能：** 获取该文件偏移指针相对偏移位置类型对应具体数值。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12