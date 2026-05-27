## class NativeMemInfo

```cangjie
public class NativeMemInfo {
    public let privateClean: UInt64
    public let privateDirty: UInt64
    public let pss: UInt64
    public let rss: UInt64
    public let sharedClean: UInt64
    public let sharedDirty: UInt64
    public let vss: UInt64
}
```

**功能：** 描述应用进程内存信息。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**起始版本：** 19

### let privateClean

```cangjie
public let privateClean: UInt64
```

**功能：** 专用干净内存的大小，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let privateDirty

```cangjie
public let privateDirty: UInt64
```

**功能：** 专用脏内存的大小，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let pss

```cangjie
public let pss: UInt64
```

**功能：** 实际占用的物理内存的大小(比例分配共享库占用的内存)，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let rss

```cangjie
public let rss: UInt64
```

**功能：** 实际占用的物理内存的大小(包括共享库占用)，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let sharedClean

```cangjie
public let sharedClean: UInt64
```

**功能：** 共享干净内存的大小，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let sharedDirty

```cangjie
public let sharedDirty: UInt64
```

**功能：** 共享脏内存的大小，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19

### let vss

```cangjie
public let vss: UInt64
```

**功能：** 占用虚拟内存大小(包括共享库所占用的内存)，以KB为单位。

**系统能力：** SystemCapability.HiviewDFX.HiProfiler.HiDebug

**类型：** UInt64

**读写能力：** 只读

**起始版本：** 19