## class Stat

```cangjie
public class Stat {}
```

**功能：** 文件具体信息。在调用Stat的方法前，需要先通过[FileFs.stat()](#static-func-statstring)方法来构建一个Stat实例。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**起始版本：** 12

### prop atime

```cangjie
public prop atime: Int64
```

**功能：** 上次访问该文件的时间，表示距1970年1月1日0时0分0秒的秒数。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### prop ctime

```cangjie
public prop ctime: Int64
```

**功能：** 最近改变文件状态的时间，表示距1970年1月1日0时0分0秒的秒数。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### prop gid

```cangjie
public prop gid: Int64
```

**功能：** 文件所有组的ID。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### prop ino

```cangjie
public prop ino: Int64
```

**功能：** 标识该文件。通常同设备上的不同文件的INO不同。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### prop location

```cangjie
public prop location: LocationType
```

**功能：** 文件的位置。表示改文件是本地文件或者云端文件。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** [LocationType](#enum-locationtype)

**读写能力：** 只读

**起始版本：** 20

### prop mode

```cangjie
public prop mode: Int64
```

**功能：** 表示文件权限，各特征位的含义如下。

>**说明：**
>
>以下值为八进制，取得的返回值为十进制，请换算后查看。<br/>-&nbsp;0o400：用户读，对于普通文件，所有者可读取文件；对于目录，所有者可读取目录项。<br/>-&nbsp;0o200：用户写，对于普通文件，所有者可写入文件；对于目录，所有者可创建/删除目录项。<br/>-&nbsp;0o100：用户执行，对于普通文件，所有者可执行文件；对于目录，所有者可在目录中搜索给定路径名。<br/>-&nbsp;0o040：用户组读，对于普通文件，所有用户组可读取文件；对于目录，所有用户组可读取目录项。<br/>-&nbsp;0o020：用户组写，对于普通文件，所有用户组可写入文件；对于目录，所有用户组可创建/删除目录项。<br/>-&nbsp;0o010：用户组执行，对于普通文件，所有用户组可执行文件；对于目录，所有用户组是否可在目录中搜索给定路径名。<br/>-&nbsp;0o004：其他读，对于普通文件，其余用户可读取文件；对于目录，其他用户组可读取目录项。<br/>-&nbsp;0o002：其他写，对于普通文件，其余用户可写入文件；对于目录，其他用户组可创建/删除目录项。<br/>-&nbsp;0o001：其他执行，对于普通文件，其余用户可执行文件；对于目录，其他用户组可在目录中搜索给定路径名。

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### prop mtime

```cangjie
public prop mtime: Int64
```

**功能：** 上次修改该文件的时间，表示距1970年1月1日0时0分0秒的秒数。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### prop size

```cangjie
public prop size: Int64
```

**功能：** 文件的大小，以字节为单位。仅对普通文件有效。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12

### prop uid

```cangjie
public prop uid: Int64
```

**功能：** 文件所有者的ID。

**系统能力：** SystemCapability.FileManagement.File.FileIO

**类型：** Int64

**读写能力：** 只读

**起始版本：** 12