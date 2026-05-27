## enum AccessFlagType

```cangjie
public enum AccessFlagType {
    LOCAL |
    ...
}
```

**功能：** 表示需要校验的文件位置。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

### LOCAL

```cangjie
LOCAL
```

**功能：** 文件是否在本地。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

## enum AccessModeType

```cangjie
public enum AccessModeType {
    EXIST |
    WRITE |
    READ |
    READ_AND_WRITE |
    ...
}
```

**功能：** 表示需要校验的具体权限。默认为校验文件是否存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

### EXIST

```cangjie
EXIST
```

**功能：** 文件是否存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

### WRITE

```cangjie
WRITE
```

**功能：** 文件是否具有写入权限。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

### READ

```cangjie
READ
```

**功能：** 文件是否具有读取权限。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

### READ_AND_WRITE

```cangjie
READ_AND_WRITE
```

**功能：** 文件是否具有读写权限。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

## enum LocationType

```cangjie
public enum LocationType {
    LOCAL |
    CLOUD |
    ...
}
```

**功能：** 文件位置，表示该文件本地存在或云端存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

### LOCAL

```cangjie
LOCAL
```

**功能：** 文件在本地存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20

### CLOUD

```cangjie
CLOUD
```

**功能：** 文件在云端存在。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 20