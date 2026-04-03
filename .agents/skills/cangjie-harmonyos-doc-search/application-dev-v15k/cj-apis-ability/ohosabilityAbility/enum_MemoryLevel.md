## enum MemoryLevel

```cangjie
public enum MemoryLevel <: Equatable<MemoryLevel> & ToString {
    | MEMORY_LEVEL_MODERATE
    | MEMORY_LEVEL_LOW
    | MEMORY_LEVEL_CRITICAL
    | MEMORY_LEVEL_UNKNOWN
    | ...
}
```

**功能：** 内存级别，该类型为枚举。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- Equatable\<MemoryLevel>

- ToString

### MEMORY_LEVEL_CRITICAL

```cangjie
MEMORY_LEVEL_CRITICAL
```

**功能：** 内存占用高。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### MEMORY_LEVEL_LOW

```cangjie
MEMORY_LEVEL_LOW
```

**功能：** 内存占用低。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### MEMORY_LEVEL_MODERATE

```cangjie
MEMORY_LEVEL_MODERATE
```

**功能：** 内存占用适中。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### MEMORY_LEVEL_UNKNOWN

```cangjie
MEMORY_LEVEL_UNKNOWN
```

**功能：** 内存占用级别未知。

**起始版本：** 19

### func !=(MemoryLevel)

```cangjie
public operator func !=(other: MemoryLevel): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MemoryLevel](#enum-memorylevel)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(MemoryLevel)

```cangjie
public operator func ==(other: MemoryLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[MemoryLevel](#enum-memorylevel)|是|-|另一个枚举值|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取当前枚举的字符串表示。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|当前枚举的字符串表示。|