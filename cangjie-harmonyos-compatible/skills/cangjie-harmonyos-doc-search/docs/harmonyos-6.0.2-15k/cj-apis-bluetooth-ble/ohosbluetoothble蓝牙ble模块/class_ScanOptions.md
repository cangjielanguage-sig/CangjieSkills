## class ScanOptions

```cangjie
public class ScanOptions {
    public var interval: Int32 = 0
    public var dutyMode: ScanDuty = SCAN_MODE_LOW_POWER
    public var matchMode: MatchMode = MATCH_MODE_AGGRESSIVE
    public var phyType: PhyType = PHY_LE_1M
    public init(interval: Int32, dutyMode: ScanDuty, matchMode: MatchMode, phyType: PhyType)
}
```

**功能：** 扫描的配置参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var dutyMode

```cangjie
public var dutyMode: ScanDuty = SCAN_MODE_LOW_POWER
```

**功能：** 表示扫描模式，默认值为SCAN_MODE_LOW_POWER。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [ScanDuty](#enum-scanduty)

**读写能力：** 可读写

**起始版本：** 19

### var interval

```cangjie
public var interval: Int32 = 0
```

**功能：** 表示扫描结果上报延迟时间，默认值为0。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var matchMode

```cangjie
public var matchMode: MatchMode = MATCH_MODE_AGGRESSIVE
```

**功能：** 表示硬件的过滤匹配模式，默认值为MATCH_MODE_AGGRESSIVE。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [MatchMode](#enum-matchmode)

**读写能力：** 可读写

**起始版本：** 19

### var phyType

```cangjie
public var phyType: PhyType = PHY_LE_1M
```

**功能：** 表示扫描中使用的PHY类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [PhyType](#enum-phytype)

**读写能力：** 可读写

**起始版本：** 19

### init(Int32, ScanDuty, MatchMode, PhyType)

```cangjie
public init(interval: Int32, dutyMode: ScanDuty, matchMode: MatchMode, phyType: PhyType)
```

**功能：** 创建扫描的配置参数结构体ScanOptions。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|interval|Int32|是|表示扫描结果上报延迟时间，初始值为0。|
|dutyMode|[ScanDuty](#enum-scanduty)|是|表示扫描模式，初始值为SCAN_MODE_LOW_POWER。|
|matchMode|[MatchMode](#enum-matchmode)|是|表示硬件的过滤匹配模式，初始值为MATCH_MODE_AGGRESSIVE。|
|phyType|[PhyType](#enum-phytype)|是|表示扫描中使用的PHY类型。|