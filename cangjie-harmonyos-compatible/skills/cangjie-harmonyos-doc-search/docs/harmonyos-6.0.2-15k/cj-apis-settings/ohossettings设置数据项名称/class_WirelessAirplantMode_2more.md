## class WirelessAirplantMode

```cangjie
public class WirelessAirplantMode {
    public static let BLUETOOTH_RADIO: String = "settings.wireless.bluetooth_radio"
    public static let CELL_RADIO: String = "settings.wireless.cell_radio"
    public static let NFC_RADIO: String = "settings.wireless.nfc_radio"
    public static let WIFI_RADIO: String = "settings.wireless.wifi_radio"
}
```

**功能：** 无线网络信息。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### static let BLUETOOTH_RADIO

```cangjie
public static let BLUETOOTH_RADIO: String = "settings.wireless.bluetooth_radio"
```

**功能：** 常量，作为AIRPLANE_MODE_RADIOS的取值时表示蓝牙在飞行模式下禁用。

**系统能力：** SystemCapability.Applications.Settings.Core

**类型：** String

**起始版本：** 19

### static let CELL_RADIO

```cangjie
public static let CELL_RADIO: String = "settings.wireless.cell_radio"
```

**功能：** 常量，作为AIRPLANE_MODE_RADIOS的取值时表示蜂窝无线电在飞行模式下禁用。

**系统能力：** SystemCapability.Applications.Settings.Core

**类型：** String

**起始版本：** 19

### static let NFC_RADIO

```cangjie
public static let NFC_RADIO: String = "settings.wireless.nfc_radio"
```

**功能：** 常量，作为AIRPLANE_MODE_RADIOS的取值时表示NFC在飞行模式下禁用。

**系统能力：** SystemCapability.Applications.Settings.Core

**类型：** String

**起始版本：** 19

### static let WIFI_RADIO

```cangjie
public static let WIFI_RADIO: String = "settings.wireless.wifi_radio"
```

**功能：** 常量，作为AIRPLANE_MODE_RADIOS的取值时表示WIFI在飞行模式下禁用。

**系统能力：** SystemCapability.Applications.Settings.Core

**类型：** String

**起始版本：** 19

## enum Date

```cangjie
public enum Date <: ToString {
    | DATE_FORMAT
    | TIME_FORMAT
    | AUTO_GAIN_TIME
    | AUTO_GAIN_TIME_ZONE
    | ...
}
```

**功能：** 提供设置时间和日期格式的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### AUTO_GAIN_TIME

```cangjie
AUTO_GAIN_TIME
```

**功能：** 是否自动从网络获取日期、时间和时区。 值为true表示自动从网络获取信息；值为false表示不自动获取。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### AUTO_GAIN_TIME_ZONE

```cangjie
AUTO_GAIN_TIME_ZONE
```

**功能：** 是否自动从NITZ获取时区。值为true表示自动获取；值为false表示不自动获取。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### DATE_FORMAT

```cangjie
DATE_FORMAT
```

**功能：** 日期格式。日期格式包括MM/dd/yyyy、dd/MM/yyyy和yyyy/MM/dd ，其中MM、dd和yyyy分别代表月份、日期和年份。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### TIME_FORMAT

```cangjie
TIME_FORMAT
```

**功能：** 时间是以12小时格式还是24小时格式显示。值为 “12” 表示12小时格式；值为 ”24“ 表示24小时格式。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置时间和日期格式的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置时间和日期格式的数据项。 |