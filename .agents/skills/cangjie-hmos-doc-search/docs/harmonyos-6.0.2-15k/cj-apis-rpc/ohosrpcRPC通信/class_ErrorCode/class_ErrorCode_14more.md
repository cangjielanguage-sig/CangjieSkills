## class ErrorCode

```cangjie
public class ErrorCode {
    public static const CHECK_PARAM_ERROR: Int32 = 401
    public static const OS_MMAP_ERROR: Int32 = 1900001
    public static const OS_IOCTL_ERROR: Int32 = 1900002
    public static const WRITE_TO_ASHMEM_ERROR: Int32 = 1900003
    public static const READ_FROM_ASHMEM_ERROR: Int32 = 1900004
    public static const ONLY_PROXY_OBJECT_PERMITTED_ERROR: Int32 = 1900005
    public static const ONLY_REMOTE_OBJECT_PERMITTED_ERROR: Int32 = 1900006
    public static const COMMUNICATION_ERROR: Int32 = 1900007
    public static const PROXY_OR_REMOTE_OBJECT_INVALID_ERROR: Int32 = 1900008
    public static const WRITE_DATA_TO_MESSAGE_SEQUENCE_ERROR: Int32 = 1900009
    public static const READ_DATA_FROM_MESSAGE_SEQUENCE_ERROR: Int32 = 1900010
    public static const PARCEL_MEMORY_ALLOC_ERROR: Int32 = 1900011
    public static const CALL_JS_METHOD_ERROR: Int32 = 1900012
    public static const OS_DUP_ERROR: Int32 = 1900013
}
```

**功能：** 错误码对应数值及含义。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### static const CALL_JS_METHOD_ERROR

```cangjie
public static const CALL_JS_METHOD_ERROR: Int32 = 1900012
```

**功能：** 执行JS回调方法失败。

**类型：** Int32

**起始版本：** 19

### static const CHECK_PARAM_ERROR

```cangjie
public static const CHECK_PARAM_ERROR: Int32 = 401
```

**功能：** 检查参数失败。

**类型：** Int32

**起始版本：** 19

### static const COMMUNICATION_ERROR

```cangjie
public static const COMMUNICATION_ERROR: Int32 = 1900007
```

**功能：** 和远端对象进行进程间通信失败。

**类型：** Int32

**起始版本：** 19

### static const ONLY_PROXY_OBJECT_PERMITTED_ERROR

```cangjie
public static const ONLY_PROXY_OBJECT_PERMITTED_ERROR: Int32 = 1900005
```

**功能：** 只有proxy对象允许该操作。

**类型：** Int32

**起始版本：** 19

### static const ONLY_REMOTE_OBJECT_PERMITTED_ERROR

```cangjie
public static const ONLY_REMOTE_OBJECT_PERMITTED_ERROR: Int32 = 1900006
```

**功能：** 只有remote对象允许该操作。

**类型：** Int32

**起始版本：** 19

### static const OS_DUP_ERROR

```cangjie
public static const OS_DUP_ERROR: Int32 = 1900013
```

**功能：** 执行系统调用dup失败。

**类型：** Int32

**起始版本：** 19

### static const OS_IOCTL_ERROR

```cangjie
public static const OS_IOCTL_ERROR: Int32 = 1900002
```

**功能：** 在共享内存文件描述符上执行系统调用ioctl失败。

**类型：** Int32

**起始版本：** 19

### static const OS_MMAP_ERROR

```cangjie
public static const OS_MMAP_ERROR: Int32 = 1900001
```

**功能：** 执行系统调用mmap失败。

**类型：** Int32

**起始版本：** 19

### static const PARCEL_MEMORY_ALLOC_ERROR

```cangjie
public static const PARCEL_MEMORY_ALLOC_ERROR: Int32 = 1900011
```

**功能：** 序列化过程中内存分配失败。

**类型：** Int32

**起始版本：** 19

### static const PROXY_OR_REMOTE_OBJECT_INVALID_ERROR

```cangjie
public static const PROXY_OR_REMOTE_OBJECT_INVALID_ERROR: Int32 = 1900008
```

**功能：** 非法的代理对象或者远端对象。

**类型：** Int32

**起始版本：** 19

### static const READ_DATA_FROM_MESSAGE_SEQUENCE_ERROR

```cangjie
public static const READ_DATA_FROM_MESSAGE_SEQUENCE_ERROR: Int32 = 1900010
```

**功能：** 读取MessageSequence数据失败。

**类型：** Int32

**起始版本：** 19

### static const READ_FROM_ASHMEM_ERROR

```cangjie
public static const READ_FROM_ASHMEM_ERROR: Int32 = 1900004
```

**功能：** 从共享内存读数据失败。

**类型：** Int32

**起始版本：** 19

### static const WRITE_DATA_TO_MESSAGE_SEQUENCE_ERROR

```cangjie
public static const WRITE_DATA_TO_MESSAGE_SEQUENCE_ERROR: Int32 = 1900009
```

**功能：** 向MessageSequence写数据失败。

**类型：** Int32

**起始版本：** 19