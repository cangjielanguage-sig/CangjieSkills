## class InputMethodProperty

```cangjie
public class InputMethodProperty <: ToString {
    public InputMethodProperty(
        public let name: String,
        public let id: String,
        public let label: String,
        public let labelId: UInt32,
        public let icon: String,
        public let iconId: UInt32
    )
}
```

**功能：** 输入法应用属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**父类型：**

- ToString

### let icon

```cangjie
public let icon: String
```

**功能：** 输入法图标数据，可以通过iconId查询获取。预留字段，暂不支持使用。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let iconId

```cangjie
public let iconId: UInt32
```

**功能：** 输入法图标资源号。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let id

```cangjie
public let id: String
```

**功能：** 输入法唯一标识。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let label

```cangjie
public let label: String
```

**功能：** 输入法对外显示名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let labelId

```cangjie
public let labelId: UInt32
```

**功能：** 输入法对外显示名称资源号。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 输入法包名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### InputMethodProperty(String, String, String, UInt32, String, UInt32)

```cangjie
public InputMethodProperty(
    public let name: String,
    public let id: String,
    public let label: String,
    public let labelId: UInt32,
    public let icon: String,
    public let iconId: UInt32
)
```

**功能：** 构建输入法应用属性的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|输入法包名。|
|id|String|是|-|输入法唯一标识。|
|label|String|是|-|输入法对外显示名称。|
|labelId|UInt32|是|-|输入法对外显示名称资源号。|
|icon|String|是|-|输入法图标数据，可以通过iconId查询获取。预留字段，暂不支持使用。|
|iconId|UInt32|是|-|输入法图标资源号。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回输入法应用属性的字符串表示。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|输入法应用属性的字符串表示。|