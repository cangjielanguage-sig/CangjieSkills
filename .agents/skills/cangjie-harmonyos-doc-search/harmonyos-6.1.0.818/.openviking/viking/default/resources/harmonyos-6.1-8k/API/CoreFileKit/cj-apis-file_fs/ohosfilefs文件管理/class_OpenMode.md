## class OpenMode

```cangjie
public class OpenMode {
    public static const READ_ONLY: Int64 = 0o0
    public static const WRITE_ONLY: Int64 = 0o1
    public static const READ_WRITE: Int64 = 0o2
    public static const CREATE: Int64 = 0o100
    public static const TRUNC: Int64 = 0o1000
    public static const APPEND: Int64 = 0o2000
    public static const NONBLOCK: Int64 = 0o4000
    public static const DIR: Int64 = 0o200000
    public static const NOFOLLOW: Int64 = 0o400000
    public static const SYNC: Int64 = 0o4010000
}
```

**功能：** open接口flags参数常量。文件打开标签。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const APPEND

```cangjie
public static const APPEND: Int64 = 0o2000
```

**功能：** 以追加方式打开，后续写将追加到文件末尾。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const CREATE

```cangjie
public static const CREATE: Int64 = 0o100
```

**功能：** 若文件不存在，则创建文件。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const DIR

```cangjie
public static const DIR: Int64 = 0o200000
```

**功能：** 如果path不指向目录，则出错。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const NOFOLLOW

```cangjie
public static const NOFOLLOW: Int64 = 0o400000
```

**功能：** 如果path指向符号链接，则出错。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const NONBLOCK

```cangjie
public static const NONBLOCK: Int64 = 0o4000
```

**功能：** 如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const READ_ONLY

```cangjie
public static const READ_ONLY: Int64 = 0o0
```

**功能：** 只读打开。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const READ_WRITE

```cangjie
public static const READ_WRITE: Int64 = 0o2
```

**功能：** 读写打开。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const SYNC

```cangjie
public static const SYNC: Int64 = 0o4010000
```

**功能：** 以同步IO的方式打开文件。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const TRUNC

```cangjie
public static const TRUNC: Int64 = 0o1000
```

**功能：** 如果文件存在且以只写或读写的方式打开，则将其长度裁剪为零。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22

### static const WRITE_ONLY

```cangjie
public static const WRITE_ONLY: Int64 = 0o1
```

**功能：** 只写打开。

**类型：** Int64

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 22