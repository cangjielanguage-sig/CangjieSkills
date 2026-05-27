## class BundleStats

```cangjie
public class BundleStats {
    public var appSize: Int64
    public var cacheSize: Int64
    public var dataSize: Int64
}
```

**功能：** 应用存储空间大小，包含安装文件、缓存文件、文件存储大小信息。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**起始版本：** 20

### var appSize

```cangjie
public var appSize: Int64
```

**功能：** 应用安装文件大小（单位为Byte）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20

### var cacheSize

```cangjie
public var cacheSize: Int64
```

**功能：** 应用缓存文件大小（单位为Byte）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20

### var dataSize

```cangjie
public var dataSize: Int64
```

**功能：** 应用文件存储大小（除应用安装文件和缓存文件）（单位为Byte）。

**类型：** Int64

**读写能力：** 可读写

**起始版本：** 20