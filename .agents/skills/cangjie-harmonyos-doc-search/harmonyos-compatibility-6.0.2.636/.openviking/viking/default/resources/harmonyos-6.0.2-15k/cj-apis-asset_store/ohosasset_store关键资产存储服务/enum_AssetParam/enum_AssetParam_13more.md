## enum AssetParam

```cangjie
public enum AssetParam {
    | SECRET(Array<UInt8>)
    | ALIAS(Array<UInt8>)
    | ACCESSIBILITY(UInt32)
    | REQUIRE_PASSWORD_SET(Bool)
    | AUTH_TYPE(UInt32)
    | AUTH_VALIDITY_PERIOD(UInt32)
    | AUTH_CHALLENGE(Array<UInt8>)
    | AUTH_TOKEN(Array<UInt8>)
    | SYNC_TYPE(UInt32)
    | IS_PERSISTENT(Bool)
    | CONFLICT_RESOLUTION(UInt32)
    | DATA_LABEL_CRITICAL_1(Array<UInt8>)
    | DATA_LABEL_CRITICAL_2(Array<UInt8>)
    | DATA_LABEL_CRITICAL_3(Array<UInt8>)
    | DATA_LABEL_CRITICAL_4(Array<UInt8>)
    | DATA_LABEL_NORMAL_1(Array<UInt8>)
    | DATA_LABEL_NORMAL_2(Array<UInt8>)
    | DATA_LABEL_NORMAL_3(Array<UInt8>)
    | DATA_LABEL_NORMAL_4(Array<UInt8>)
    | DATA_LABEL_NORMAL_LOCAL_1(Array<UInt8>)
    | DATA_LABEL_NORMAL_LOCAL_2(Array<UInt8>)
    | DATA_LABEL_NORMAL_LOCAL_3(Array<UInt8>)
    | DATA_LABEL_NORMAL_LOCAL_4(Array<UInt8>)
    | RETURN_TYPE(UInt32)
    | RETURN_LIMIT(UInt32)
    | RETURN_OFFSET(UInt32)
    | RETURN_ORDERED_BY(UInt32)
    | UPDATE_TIME(Array<UInt8>)
    | OPERATION_TYPE(UInt32)
    | CJ_UNKNOWN_TYPE
    | ...
}
```

**功能：** 用于表示AssetParam中关键资产支持的属性名称类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

枚举值说明同[AssetTag](#class-assettag)中对应的tag名称。另外，CJ_UNKNOWN_TYPE为不属于以上操作类型的所有无效类型。

### ACCESSIBILITY(UInt32)

```cangjie
ACCESSIBILITY(UInt32)
```

**功能：** 基于锁屏状态的访问控制。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### ALIAS(Array\<UInt8>)

```cangjie
ALIAS(Array<UInt8>)
```

**功能：** 关键资产别名，每条关键资产的唯一索引。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### AUTH_CHALLENGE(Array\<UInt8>)

```cangjie
AUTH_CHALLENGE(Array<UInt8>)
```

**功能：** 用户认证的挑战值。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### AUTH_TOKEN(Array\<UInt8>)

```cangjie
AUTH_TOKEN(Array<UInt8>)
```

**功能：** 用户认证通过的授权令牌。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### AUTH_TYPE(UInt32)

```cangjie
AUTH_TYPE(UInt32)
```

**功能：** 访问关键资产所需的用户认证类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### AUTH_VALIDITY_PERIOD(UInt32)

```cangjie
AUTH_VALIDITY_PERIOD(UInt32)
```

**功能：** 用户认证的有效期。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### CJ_UNKNOWN_TYPE

```cangjie
CJ_UNKNOWN_TYPE
```

**功能：** 无效的操作类型。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### CONFLICT_RESOLUTION(UInt32)

```cangjie
CONFLICT_RESOLUTION(UInt32)
```

**功能：** 新增关键资产时的冲突（如：别名相同）处理策略。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### DATA_LABEL_CRITICAL_1(Array\<UInt8>)

```cangjie
DATA_LABEL_CRITICAL_1(Array<UInt8>)
```

**功能：** 关键资产附属信息，内容由业务自定义且有完整性保护。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### DATA_LABEL_CRITICAL_2(Array\<UInt8>)

```cangjie
DATA_LABEL_CRITICAL_2(Array<UInt8>)
```

**功能：** 关键资产附属信息，内容由业务自定义且有完整性保护。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### DATA_LABEL_CRITICAL_3(Array\<UInt8>)

```cangjie
DATA_LABEL_CRITICAL_3(Array<UInt8>)
```

**功能：** 关键资产附属信息，内容由业务自定义且有完整性保护。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19

### DATA_LABEL_CRITICAL_4(Array\<UInt8>)

```cangjie
DATA_LABEL_CRITICAL_4(Array<UInt8>)
```

**功能：** 关键资产附属信息，内容由业务自定义且有完整性保护。

**系统能力：** SystemCapability.Security.Asset

**起始版本：** 19