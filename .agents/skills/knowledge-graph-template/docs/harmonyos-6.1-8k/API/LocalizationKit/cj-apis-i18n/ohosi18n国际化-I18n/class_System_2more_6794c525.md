## class System

```cangjie
public class System {}
```

**功能：** I18n系统对象。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### static func getAppPreferredLanguage()

```cangjie
public static func getAppPreferredLanguage(): String
```

**功能：** 获取应用偏好语言。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|应用偏好语言。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.i18n.*
import kit.LocalizationKit.getCalendar
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let appPreferredLanguage = System.getAppPreferredLanguage() // 获取应用偏好语言
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## enum CalendarType

```cangjie
public enum CalendarType {
    | Buddhist
    | Chinese
    | Coptic
    | Ethiopic
    | Hebrew
    | Gregory
    | Indian
    | IslamicCivil
    | IslamicTbla
    | IslamicUmalqura
    | Japanese
    | Persian
    | ...
}
```

**功能：** 日历类型枚举，用于指定不同的日历系统。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Buddhist

```cangjie
Buddhist
```

**功能：** 佛历。

**系统能力：**  SystemCapability.Global.I18n

**起始版本：** 22

### Chinese

```cangjie
Chinese
```

**功能：** 农历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Coptic

```cangjie
Coptic
```

**功能：** 科普特历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Ethiopic

```cangjie
Ethiopic
```

**功能：** 埃塞俄比亚历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Hebrew

```cangjie
Hebrew
```

**功能：** 希伯来历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Gregory

```cangjie
Gregory
```

**功能：** 公历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Indian

```cangjie
Indian
```

**功能：** 印度历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### IslamicCivil

```cangjie
IslamicCivil
```

**功能：** 伊斯兰希吉来历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### IslamicTbla

```cangjie
IslamicTbla
```

**功能：** 伊斯兰天文历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### IslamicUmalqura

```cangjie
IslamicUmalqura
```

**功能：** 伊斯兰历（乌姆库拉）。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Japanese

```cangjie
Japanese
```

**功能：** 日本历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

### Persian

```cangjie
Persian
```

**功能：** 波斯历。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22