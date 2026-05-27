## class UIFontFallbackInfo

```cangjie
public class UIFontFallbackInfo {
    public UIFontFallbackInfo(
        public let language: String,
        public let family: String
    )
}
```

**功能：** 字体集的备用字体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let language

```cangjie
public let language: String
```

**功能：** 表示字体集所支持的语言类型，语言格式为bcp47。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let family

```cangjie
public let family: String
```

**功能：** 表示字体集名，字体文件中指定的"family"值。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### UIFontFallbackInfo(String, String)

```cangjie
public UIFontFallbackInfo(
    public let language: String,
    public let family: String
)
```

**功能：** UIFontFallbackInfo构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|language|String|是|-|字体集所支持的语言类型，语言格式为bcp47。|
|family|String|是|-|字体集名，字体文件中指定的"family"值。|