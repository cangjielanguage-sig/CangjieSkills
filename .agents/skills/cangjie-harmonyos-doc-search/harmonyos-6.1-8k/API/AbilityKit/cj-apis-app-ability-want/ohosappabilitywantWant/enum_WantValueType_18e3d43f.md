## enum WantValueType

```cangjie
public enum WantValueType {
    | Int64Value(Int64)
    | Float64Value(Float64)
    | StringValue(String)
    | BoolValue(Bool)
    | ArrayValue(Array<WantValueType>)
    | HashMapValue(HashMap<String, WantValueType>)
    | ...
}
```

**功能：** Want值类型。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### ArrayValue(Array\<WantValueType>)

```cangjie
ArrayValue(Array<WantValueType>)
```

**功能：** 数组值。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### BoolValue(Bool)

```cangjie
BoolValue(Bool)
```

**功能：** 布尔值。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### Float64Value(Float64)

```cangjie
Float64Value(Float64)
```

**功能：** 64位浮点值。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### HashMapValue(HashMap\<String, WantValueType>)

```cangjie
HashMapValue(HashMap<String, WantValueType>)
```

**功能：** 哈希映射值。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### Int64Value(Int64)

```cangjie
Int64Value(Int64)
```

**功能：** 64位整数值。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22

### StringValue(String)

```cangjie
StringValue(String)
```

**功能：** 字符串值。

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 22