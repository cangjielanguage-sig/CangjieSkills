## class Constants

```cangjie
public class Constants {
    public static let MAX_KEY_LENGTH: Int32 = 1024
    public static let MAX_VALUE_LENGTH: Int32 = 4194303
    public static let MAX_KEY_LENGTH_DEVICE: Int32 = 896
    public static let MAX_STORE_ID_LENGTH: Int32 = 128
    public static let MAX_QUERY_LENGTH: Int32 = 512000
    public static let MAX_BATCH_SIZE: Int32 = 128
}
```

**功能：** 分布式键值数据库常量。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### static let MAX_BATCH_SIZE

```cangjie
public static let MAX_BATCH_SIZE: Int32 = 128
```

**功能：** 值为128，表示最大批处理操作数量。

**类型：** Int32

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### static let MAX_KEY_LENGTH

```cangjie
public static let MAX_KEY_LENGTH: Int32 = 1024
```

**功能：** 值为1024，表示数据库中Key允许的最大长度，单位字节。

**类型：** Int32

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### static let MAX_KEY_LENGTH_DEVICE

```cangjie
public static let MAX_KEY_LENGTH_DEVICE: Int32 = 896
```

**功能：** 值为896，表示设备协同数据库中Key允许的最大长度，单位字节。

**类型：** Int32

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### static let MAX_QUERY_LENGTH

```cangjie
public static let MAX_QUERY_LENGTH: Int32 = 512000
```

**功能：** 值为512000，表示最大查询长度，单位字节。

**类型：** Int32

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### static let MAX_STORE_ID_LENGTH

```cangjie
public static let MAX_STORE_ID_LENGTH: Int32 = 128
```

**功能：** 值为128，表示数据库标识符允许的最大长度，单位字节。

**类型：** Int32

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### static let MAX_VALUE_LENGTH

```cangjie
public static let MAX_VALUE_LENGTH: Int32 = 4194303
```

**功能：** 值为4194303，表示数据库中Value允许的最大长度，单位字节。

**类型：** Int32

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22