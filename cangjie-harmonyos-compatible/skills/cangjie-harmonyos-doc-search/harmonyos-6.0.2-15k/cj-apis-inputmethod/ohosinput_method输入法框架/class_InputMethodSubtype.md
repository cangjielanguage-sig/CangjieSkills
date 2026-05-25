## class InputMethodSubtype

```cangjie
public class InputMethodSubtype <: ToString {
    public InputMethodSubtype(
        public let name: String,
        public let id: String,
        public let locale: String,
        public let language: String,
        public let label: ?String,
        public let labelId: ?UInt32,
        public let icon: ?String,
        public let iconId: ?UInt32,
        public let mode: ?String
    )
}
```

**功能：** 提供对输入法子类型的属性管理。输入法子类型允许输入法根据需要显示不用的输入模式或语言，完成模式或语言切换，如：输入法的中文/英文键盘等均属于输入法的子类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**父类型：**

- ToString

### let icon

```cangjie
public let icon: ?String
```

**功能：** 输入法子类型的图标，可以通过iconId查询获取。预留字段，暂不支持使用。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let iconId

```cangjie
public let iconId: ?UInt32
```

**功能：** 输入法子类型的图标id。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let id

```cangjie
public let id: String
```

**功能：** 输入法子类型的id。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let label

```cangjie
public let label: ?String
```

**功能：** 输入法子类型的标签。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let labelId

```cangjie
public let labelId: ?UInt32
```

**功能：** 输入法子类型的标签资源号。

**类型：** ?UInt32

**读写能力：** 只读

**起始版本：** 19

### let language

```cangjie
public let language: String
```

**功能：** 输入法子类型的语言。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let locale

```cangjie
public let locale: String
```

**功能：** 输入法子类型的方言版本。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let mode

```cangjie
public let mode: ?String
```

**功能：** 输入法子类型的模式，可选的值包括upper（大写）和lower（小写）。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 输入法子类型所属应用的包名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### InputMethodSubtype(String, String, String, String, ?String, ?UInt32, ?String, ?UInt32, ?String)

```cangjie
public InputMethodSubtype(
    public let name: String,
    public let id: String,
    public let locale: String,
    public let language: String,
    public let label: ?String,
    public let labelId: ?UInt32,
    public let icon: ?String,
    public let iconId: ?UInt32,
    public let mode: ?String
)
```

**功能：** 构建提供对输入法子类型的属性管理的对象。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|输入法子类型所属应用的包名。|
|id|String|是|-|输入法子类型的id。|
|locale|String|是|-|输入法子类型的方言版本。|
|language|String|是|-|输入法子类型的语言。|
|label|?String|是|-|输入法子类型的标签。|
|labelId|?UInt32|是|-|输入法子类型的标签资源号。|
|icon|?String|是|-|输入法子类型的图标，可以通过iconId查询获取。预留字段，暂不支持使用。|
|iconId|?UInt32|是|-|输入法子类型的图标id。|
|mode|?String|是|-|输入法子类型的模式，可选的值包括upper（大写）和lower（小写）。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回输入法子类型的字符串表示。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|输入法子类型的字符串表示。|