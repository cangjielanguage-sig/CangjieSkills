## class UIFontFallbackGroupInfo

```cangjie
public class UIFontFallbackGroupInfo {
    public UIFontFallbackGroupInfo(
        public let fontSetName: String,
        public let fallback: Array<UIFontFallbackInfo>
    )
}
```

**功能：** 备用字体集。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let fontSetName

```cangjie
public let fontSetName: String
```

**功能：** 表示备用字体集所对应的字体集名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let fallback

```cangjie
public let fallback: Array<UIFontFallbackInfo>
```

**功能：** 表示以下列表为该字体集的备用字体，如果fontSetName为""，表示可以作为所有字体集的备用字体。

**类型：** Array\<[UIFontFallbackInfo](#class-uifontfallbackinfo)>

**读写能力：** 只读

**起始版本：** 19

### UIFontFallbackGroupInfo(String, Array\<UIFontFallbackInfo>)

```cangjie
public UIFontFallbackGroupInfo(
    public let fontSetName: String,
    public let fallback: Array<UIFontFallbackInfo>
)
```

**功能：** UIFontFallbackGroupInfo构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontSetName|String|是|-|备用字体集所对应的字体集名称。|
|fallback|Array\<[UIFontFallbackInfo](#class-uifontfallbackinfo)>|是|-|表示以下列表为该字体集的备用字体，如果fontSetName为""，表示可以作为所有字体集的备用字体。|

## class UIFontAliasInfo

```cangjie
public class UIFontAliasInfo {
    public UIFontAliasInfo(
        public let name: String,
        public let weight: UInt32
    )
}
```

**功能：** 字体集别名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let name

```cangjie
public let name: String
```

**功能：** 表示别名名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let weight

```cangjie
public let weight: UInt32
```

**功能：** 当weight>0时表示此字体集只包含所指定weight的字体，当weight=0时，表示此字体集包含所有字体。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### UIFontAliasInfo(String, UInt32)

```cangjie
public UIFontAliasInfo(
    public let name: String,
    public let weight: UInt32
)
```

**功能：** UIFontAliasInfo构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|别名名称。|
|weight|UInt32|是|-|当weight>0时表示此字体集只包含所指定weight的字体，当weight=0时，表示此字体集包含所有字体。可返回的值有0、100、400、700、900。|

## class UIFontAdjustInfo

```cangjie
public class UIFontAdjustInfo {
    public UIFontAdjustInfo(
        public let weight: UInt32,
        public let to: UInt32
    )
}
```

**功能：** 字体原大小与实际大小的对应关系。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let weight

```cangjie
public let weight: UInt32
```

**功能：** 代表字体原本的weight值。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let to

```cangjie
public let to: UInt32
```

**功能：** 代表字体在应用中显示的weight值。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### UIFontAdjustInfo(UInt32, UInt32)

```cangjie
public UIFontAdjustInfo(
    public let weight: UInt32,
    public let to: UInt32
)
```

**功能：** UIFontAdjustInfo构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|weight|UInt32|是|-|字体原本的weight值。可返回的值有50、80、100、200。|
|to|UInt32|是|-|字体在应用中显示的weight值。可返回的值有100、400、700、900。|