## class FontInfo

```cangjie
public class FontInfo {
    public FontInfo(
        public let path: String,
        public let postScriptName: String,
        public let fullName: String,
        public let family: String,
        public let subfamily: String,
        public let weight: UInt32,
        public let width: UInt32,
        public let italic: Bool,
        public let monoSpace: Bool,
        public let symbolic: Bool
    )
}
```

**功能：** 字体信息类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let path

```cangjie
public let path: String
```

**功能：** 描述系统字体的文件路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let postScriptName

```cangjie
public let postScriptName: String
```

**功能：** 表示系统字体的postScript名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let fullName

```cangjie
public let fullName: String
```

**功能：** 表示系统字体的名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let family

```cangjie
public let family: String
```

**功能：** 描述系统字体的字体家族。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let subfamily

```cangjie
public let subfamily: String
```

**功能：** 表示系统字体的子字体家族。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let weight

```cangjie
public let weight: UInt32
```

**功能：** 表示系统字体的字重，单位px。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let width

```cangjie
public let width: UInt32
```

**功能：** 表示系统字体的宽度，单位px。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let italic

```cangjie
public let italic: Bool
```

**功能：** 表示系统字体是否倾斜。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let monoSpace

```cangjie
public let monoSpace: Bool
```

**功能：** 表示系统字体是否紧凑。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### let symbolic

```cangjie
public let symbolic: Bool
```

**功能：** 表示系统字体是否支持符号字体。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### FontInfo(String, String, String, String, String, UInt32, UInt32, Bool, Bool, Bool)

```cangjie
public FontInfo(
    public let path: String,
    public let postScriptName: String,
    public let fullName: String,
    public let family: String,
    public let subfamily: String,
    public let weight: UInt32,
    public let width: UInt32,
    public let italic: Bool,
    public let monoSpace: Bool,
    public let symbolic: Bool
)
```

**功能：** FontInfo构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|path|String|是|-|系统字体的文件路径。|
|postScriptName|String|是|-|系统字体的postScript名称。|
|fullName|String|是|-|系统字体的名称。|
|family|String|是|-|系统字体的字体家族。|
|subfamily|String|是|-|系统字体的子字体家族。|
|weight|UInt32|是|-|系统字体的字重，单位px。<br>取值范围：[0,8]，取值间隔为1，分别对应FontWeight枚举中的值。<br>初始值：0|
|width|UInt32|是|-|系统字体的宽度，单位px。<br>取值范围：[1,9]，取值间隔为1，分别对应FontWidth枚举中的值。|
|italic|Bool|是|-|系统字体是否倾斜。<br>值为true，表示斜体字体，值为false，表示非斜体字体。<br>初始值：false|
|monoSpace|Bool|是|-|系统字体是否紧凑。<br>值为true，表示等宽字体，值为false，表示非等宽字体。<br>初始值：false|
|symbolic|Bool|是|-|系统字体是否支持符号字体。<br>值为true，表示支持符号字体，值为false，表示不支持符号字体。<br>初始值：false|