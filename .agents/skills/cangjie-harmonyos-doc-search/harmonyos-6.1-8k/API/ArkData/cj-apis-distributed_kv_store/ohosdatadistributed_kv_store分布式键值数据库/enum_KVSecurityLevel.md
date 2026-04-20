## enum KVSecurityLevel

```cangjie
public enum KVSecurityLevel {
    | S1
    | S2
    | S3
    | S4
    | ...
}
```

**功能：** 数据库的安全级别枚举。

> **说明**：
>
> 在单设备使用场景下，KV数据库支持修改securityLevel参数进行安全等级升级。升级操作需要注意以下几点：
>
> * 该操作不支持跨设备同步的数据库。不同安全等级的数据库之间不能进行数据同步。若需升级数据库的安全等级，建议重新创建更高安全等级的数据库。
> * 关闭当前数据库后，修改securityLevel参数以重新设置数据库的安全等级，然后重新打开数据库。
> * 该操作仅支持升级，例如从S2到S3，不支持降级，例如从S3到S2。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### S1

```cangjie
S1
```

**功能：** 表示数据库的安全级别为低级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致有限的不利影响。例如，性别、国籍，用户申请记录等。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### S2

```cangjie
S2
```

**功能：** 表示数据库的安全级别为中级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。例如，个人详细通信地址，姓名昵称等。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### S3

```cangjie
S3
```

**功能：** 表示数据库的安全级别为高级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。例如，个人实时精确定位信息、运动轨迹等。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22

### S4

```cangjie
S4
```

**功能：** 表示数据库的安全级别为关键级别，业界法律法规中定义的特殊数据类型，涉及个人的最私密领域的信息，一旦泄露、篡改、破坏、销毁可能会给个人或组织造成重大不利影响的数据。例如，政治观点、宗教、和哲学信仰、工会成员资格、基因数据、生物信息、健康和性生活状况、性取向、设备认证鉴权、个人的信用卡等财务信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**起始版本：** 22