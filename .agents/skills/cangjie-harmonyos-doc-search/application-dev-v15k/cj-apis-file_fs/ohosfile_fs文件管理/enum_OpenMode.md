## enum OpenMode

```cangjie
public enum OpenMode {
    | READ_ONLY
    | WRITE_ONLY
    | READ_WRITE
    | CREATE
    | TRUNC
    | APPEND
    | NONBLOCK
    | DIR
    | NOFOLLOW
    | SYNC
    | ...
}
```

**功能：** open接口flags参数常量。文件打开标签。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### APPEND

```cangjie
APPEND
```

**功能：** 以追加方式打开，后续写将追加到文件末尾。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### CREATE

```cangjie
CREATE
```

**功能：** 若文件不存在，则创建文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### DIR

```cangjie
DIR
```

**功能：** 如果path不指向目录，则出错。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### NOFOLLOW

```cangjie
NOFOLLOW
```

**功能：** 如果path指向符号链接，则出错。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### NONBLOCK

```cangjie
NONBLOCK
```

**功能：** 如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续IO进行非阻塞操作。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### READ_ONLY

```cangjie
READ_ONLY
```

**功能：** 只读打开。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### READ_WRITE

```cangjie
READ_WRITE
```

**功能：** 读写打开。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### SYNC

```cangjie
SYNC
```

**功能：** 以同步IO的方式打开文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### TRUNC

```cangjie
TRUNC
```

**功能：** 如果文件存在且以只写或读写的方式打开文件，则将其长度裁剪为零。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### WRITE_ONLY

```cangjie
WRITE_ONLY
```

**功能：** 只写打开。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### prop mode

```cangjie
public prop mode: Int64
```

**功能：** 获取文件打开标签类型对应具体数值。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12