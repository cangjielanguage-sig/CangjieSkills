## enum MemberType

```cangjie
public enum MemberType {
    | INT64(Int64)
    | STRING(String)
    | BOOL(Bool)
    | ...
}
```

**功能：** PhotoAsset的成员类型。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### BOOL(Bool)

```cangjie
BOOL(Bool)
```

**功能：** 表示值类型为布尔类型。

**起始版本：** 19

### INT64(Int64)

```cangjie
INT64(Int64)
```

**功能：** 表示值类型为数字，可取任意值。

**起始版本：** 19

### STRING(String)

```cangjie
STRING(String)
```

**功能：** 表示值类型为字符，可取任意值。

**起始版本：** 19

### func getBool()

```cangjie
public func getBool(): Bool
```

**功能：** 获取BOOL(Bool)中的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回BOOL(Bool)中的值。|

### func getNumber()

```cangjie
public func getNumber(): Int64
```

**功能：** 获取INT64(Int64)中的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|返回INT64(Int64)中的值。|

### func getString()

```cangjie
public func getString(): String
```

**功能：** 获取STRING(String)中的值。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回STRING(String)中的值。|