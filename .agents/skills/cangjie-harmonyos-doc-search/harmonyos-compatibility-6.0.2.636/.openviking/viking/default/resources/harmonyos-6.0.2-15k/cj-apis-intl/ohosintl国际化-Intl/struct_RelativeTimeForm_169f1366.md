## struct RelativeTimeFormatResolvedOptions

```cangjie
public struct RelativeTimeFormatResolvedOptions {
    public RelativeTimeFormatResolvedOptions(
        public var localeMatcher: String,
        public var numeric: String,
        public var style: String,
        public var numberingSystem: String
    )
}
```

**功能：** 表示RelativeTimeFormat对象可设置的属性。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

### var localeMatcher

```cangjie
public var localeMatcher: String
```

**功能：** locale匹配算法，取值包括："best fit", "lookup"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var numberingSystem

```cangjie
public var numberingSystem: String
```

**功能：** 使用的数字系统。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var numeric

```cangjie
public var numeric: String
```

**功能：** 输出消息的格式，取值包括："always", "auto"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var style

```cangjie
public var style: String
```

**功能：** 国际化消息的长度，取值包括："long", "short", "narrow"。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### RelativeTimeFormatResolvedOptions(String, String, String, String)

```cangjie
public RelativeTimeFormatResolvedOptions(
    public var localeMatcher: String,
    public var numeric: String,
    public var style: String,
    public var numberingSystem: String
)
```

**功能：** 构建表示RelativeTimeFormat对象可设置的属性的对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|localeMatcher|String|是|-|包含区域设置信息的字符串，包括语言以及可选的脚本和区域。|
|numeric|String|是|-|输出消息的格式，取值包括："always", "auto"。|
|style|String|是|-|国际化消息的长度，取值包括："long", "short", "narrow"。|
|numberingSystem|String|是|-|使用的数字系统。|