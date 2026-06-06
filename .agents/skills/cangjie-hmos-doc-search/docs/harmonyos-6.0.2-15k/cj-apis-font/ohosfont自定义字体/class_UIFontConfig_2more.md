## class UIFontConfig

```cangjie
public class UIFontConfig {
    public UIFontConfig(
        public let fontDir: Array<String>,
        public let generic: Array<UIFontGenericInfo>,
        public let fallbackGroups: Array<UIFontFallbackGroupInfo>
    )
}
```

**功能：** 系统的UI字体配置信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let fontDir

```cangjie
public let fontDir: Array<String>
```

**功能：** 表示系统字体文件所在的路径。

**类型：** Array\<String>

**读写能力：** 只读

**起始版本：** 19

### let generic

```cangjie
public let generic: Array<UIFontGenericInfo>
```

**功能：** 表示系统所支持的通用字体集列表。

**类型：** Array\<[UIFontGenericInfo](#class-uifontgenericinfo)>

**读写能力：** 只读

**起始版本：** 19

### let fallbackGroups

```cangjie
public let fallbackGroups: Array<UIFontFallbackGroupInfo>
```

**功能：** 表示备用字体集。

**类型：** Array\<[UIFontFallbackGroupInfo](#class-uifontfallbackgroupinfo)>

**读写能力：** 只读

**起始版本：** 19

### UIFontConfig(Array\<String>, Array\<UIFontGenericInfo>, Array\<UIFontFallbackGroupInfo>)

```cangjie
public UIFontConfig(
    public let fontDir: Array<String>,
    public let generic: Array<UIFontGenericInfo>,
    public let fallbackGroups: Array<UIFontFallbackGroupInfo>
)
```

**功能：** UIFontConfig构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fontDir|Array\<String>|是|-|系统字体文件所在的路径。|
|generic|Array\<[UIFontGenericInfo](#class-uifontgenericinfo)>|是|-|系统所支持的通用字体集列表。|
|fallbackGroups|Array\<[UIFontFallbackGroupInfo](#class-uifontfallbackgroupinfo)>|是|-|备用字体集。|

## class UIFontGenericInfo

```cangjie
public class UIFontGenericInfo {
    public UIFontGenericInfo(
        public let family: String,
        public let alias: Array<UIFontAliasInfo>,
        public let adjust: Array<UIFontAdjustInfo>
    )
}
```

**功能：** 表示通用字体集。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let family

```cangjie
public let family: String
```

**功能：** 字体集名，字体文件中指定的"family"值。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let alias

```cangjie
public let alias: Array<UIFontAliasInfo>
```

**功能：** 表示别名列表。

**类型：** Array\<[UIFontAliasInfo](#class-uifontaliasinfo)>

**读写能力：** 只读

**起始版本：** 19

### let adjust

```cangjie
public let adjust: Array<UIFontAdjustInfo>
```

**功能：** 表示字体原本的weight值对应需显示的值。

**类型：** Array\<[UIFontAdjustInfo](#class-uifontadjustinfo)>

**读写能力：** 只读

**起始版本：** 19

### UIFontGenericInfo(String, Array\<UIFontAliasInfo>, Array\<UIFontAdjustInfo>)

```cangjie
public UIFontGenericInfo(
    public let family: String,
    public let alias: Array<UIFontAliasInfo>,
    public let adjust: Array<UIFontAdjustInfo>
)
```

**功能：** UIFontGenericInfo构造器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|family|String|是|-|字体集名，字体文件中指定的"family"值。|
|alias|Array\<[UIFontAliasInfo](#class-uifontaliasinfo)>|是|-|别名列表。|
|adjust|Array\<[UIFontAdjustInfo](#class-uifontadjustinfo)>|是|-|字体原本的weight值对应需显示的值。|