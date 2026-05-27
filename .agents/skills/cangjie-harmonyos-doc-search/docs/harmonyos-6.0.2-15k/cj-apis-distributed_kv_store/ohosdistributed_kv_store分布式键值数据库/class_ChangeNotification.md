## class ChangeNotification

```cangjie
public class ChangeNotification <: ToString {
    public let insertEntries: ArrayList<Entry>
    public let updateEntries: ArrayList<Entry>
    public let deleteEntries: ArrayList<Entry>
    public let deviceId: String
}
```

**功能：** 数据变更时通知的对象，包括数据插入的数据、更新的数据、删除的数据和设备ID。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**父类型：**

- ToString

### let deleteEntries

```cangjie
public let deleteEntries: ArrayList<Entry>
```

**功能：** 数据删除记录。

**类型：** ArrayList\<[Entry](#struct-entry)>

**读写能力：** 只读

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 设备ID，此处为设备UUID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let insertEntries

```cangjie
public let insertEntries: ArrayList<Entry>
```

**功能：** 数据添加记录。

**类型：** ArrayList\<[Entry](#struct-entry)>

**读写能力：** 只读

**起始版本：** 19

### let updateEntries

```cangjie
public let updateEntries: ArrayList<Entry>
```

**功能：** 数据更新记录。

**类型：** ArrayList\<[Entry](#struct-entry)>

**读写能力：** 只读

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转成字符串格式。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回转换后的字符串。|