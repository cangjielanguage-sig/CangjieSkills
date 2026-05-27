## enum WorkSchedulerValueType

```cangjie
public enum WorkSchedulerValueType <: Equatable<WorkSchedulerValueType> & ToString {
    | INT(Int32)
    | FLOAT64(Float64)
    | BOOL(Bool)
    | STRING(String)
    |...
}
```

**功能：** 类型用于表示参数信息中允许的数据字段类型。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

**父类型：**

- Equatable\<WorkSchedulerValueType>
- ToString

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** 表示字段类型为布尔值。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

### FLOAT64(Float64)

```cangjie
FLOAT64(Float64)
```

**功能：** 表示字段类型为浮点数。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

### INT(Int32)

```cangjie
INT(Int32)
```

**功能：** 表示字段类型为整型数。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示字段类型为字符串。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

### func !=(WorkSchedulerValueType)

```cangjie
public operator func !=(other: WorkSchedulerValueType): Bool
```

**功能：** 对数据字段类型判不等。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WorkSchedulerValueType](#enum-workschedulervaluetype)|是|-|类型用于表示参数信息中允许的数据字段类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果数据字段类型不同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|