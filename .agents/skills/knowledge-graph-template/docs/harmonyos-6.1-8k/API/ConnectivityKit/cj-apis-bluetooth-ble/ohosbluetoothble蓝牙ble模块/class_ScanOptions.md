## class ScanOptions

```cangjie
public class ScanOptions {
    public var interval: Int32
    public var dutyMode: ScanDuty
    public var matchMode: MatchMode
    public var phyType: PhyType
    public init(
        interval!: Int32 = 0,
        dutyMode!: ScanDuty = ScanModeLowPower,
        matchMode!: MatchMode = MatchModeAggressive,
        phyType!: PhyType = PhyLe1M,
        reportMode!: ScanReportMode = Normal
    )
}
```

**功能：** BLE扫描的配置参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var dutyMode

```cangjie
public var dutyMode: ScanDuty
```

**功能：** 扫描模式。

**类型：** [ScanDuty](#enum-scanduty)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var interval

```cangjie
public var interval: Int32
```

**功能：** 扫描结果上报的延迟时间，单位：ms。搭配[ScanReportMode](#enum-scanreportmode)使用。

- 在常规或围栏扫描上报模式下，该值不生效，扫描到符合过滤条件的广播报文后立即上报。

- 在批量扫描上报模式下，该值生效，扫描到符合过滤条件的广播报文后，会存入缓存队列，延迟上报。若不设置该值或设置在[0, 5000)范围内，蓝牙子系统会默认设置延迟时间为5000ms。延迟时间内，若符合过滤条件的广播报文数量超过硬件缓存能力，蓝牙子系统会提前上报扫描结果。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var matchMode

```cangjie
public var matchMode: MatchMode
```

**功能：** 硬件的过滤匹配模式。

**类型：** [MatchMode](#enum-matchmode)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var phyType

```cangjie
public var phyType: PhyType
```

**功能：** 扫描中使用的物理通道类型。

**类型：** [PhyType](#enum-phytype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(Int32, ScanDuty, MatchMode, PhyType, ScanReportMode)

```cangjie
public init(
    interval!: Int32 = 0,
    dutyMode!: ScanDuty = ScanModeLowPower,
    matchMode!: MatchMode = MatchModeAggressive,
    phyType!: PhyType = PhyLe1M,
    reportMode!: ScanReportMode = Normal
)
```

**功能：** 创建扫描的配置参数结构体ScanOptions。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|interval|Int32|否|0|**命名参数。** 扫描结果上报的延迟时间，单位：ms，默认值为0。搭配[ScanReportMode](#enum-scanreportmode)使用。|
|dutyMode|[ScanDuty](#enum-scanduty)|否|ScanModeLowPower|**命名参数。** 扫描模式，默认值为ScanModeLowPower。|
|matchMode|[MatchMode](#enum-matchmode)|否|MatchModeAggressive|**命名参数。** 硬件的过滤匹配模式，默认值为MatchModeAggressive。|
|phyType|[PhyType](#enum-phytype)|否|PhyLe1M|**命名参数。** 扫描中使用的物理通道类型，默认值为PhyLe1M。|
|reportMode|[ScanReportMode](#enum-scanreportmode)|否|Normal|**命名参数。** 扫描结果数据上报模式，默认值为Normal。|