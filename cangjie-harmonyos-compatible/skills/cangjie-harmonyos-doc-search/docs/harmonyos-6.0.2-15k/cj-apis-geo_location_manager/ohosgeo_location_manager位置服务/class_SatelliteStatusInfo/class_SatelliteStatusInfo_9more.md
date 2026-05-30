## class SatelliteStatusInfo

```cangjie
public class SatelliteStatusInfo {
    public var satellitesNumber: Int32
    public var satelliteIds: Array<Int32>
    public var carrierToNoiseDensitys: Array<Float64>
    public var altitudes: Array<Float64>
    public var azimuths: Array<Float64>
    public var carrierFrequencies: Array<Float64>
    public var satelliteConstellation: Array<SatelliteConstellationCategory>
    public var satelliteAdditionalInfo: Array<Int32>
    public init(satellitesNumber: Int32, satelliteIds: Array<Int32>, carrierToNoiseDensitys: Array<Float64>,
        altitudes: Array<Float64>, azimuths: Array<Float64>, carrierFrequencies: Array<Float64>,
        satelliteConstellation!: Array<SatelliteConstellationCategory> = Array<SatelliteConstellationCategory>(),
        satelliteAdditionalInfo!: Array<Int32> = Array<Int32>())
}
```

**功能：** 卫星状态信息。

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

### var altitudes

```cangjie
public var altitudes: Array<Float64>
```

**功能：** 表示卫星高度角信息。单位是“度”，取值范围为-90到90。

**类型：** Array\<Float64>

**读写能力：** 可读写

**起始版本：** 19

### var azimuths

```cangjie
public var azimuths: Array<Float64>
```

**功能：** 表示方位角。单位是“度”，取值范围为0到360。

**类型：** Array\<Float64>

**读写能力：** 可读写

**起始版本：** 19

### var carrierFrequencies

```cangjie
public var carrierFrequencies: Array<Float64>
```

**功能：** 表示载波频率。单位是Hz，取值范围为大于等于0。

**类型：** Array\<Float64>

**读写能力：** 可读写

**起始版本：** 19

### var carrierToNoiseDensitys

```cangjie
public var carrierToNoiseDensitys: Array<Float64>
```

**功能：** 表示载波噪声功率谱密度比，即cn0。取值范围为大于0。

**类型：** Array\<Float64>

**读写能力：** 可读写

**起始版本：** 19

### var satelliteAdditionalInfo

```cangjie
public var satelliteAdditionalInfo: Array<Int32>
```

**功能：** 表示卫星的附加信息。

每个比特位代表不同含义，具体定义参见[SatelliteAdditionalInfo](#enum-satelliteadditionalinfo)。

**类型：** Array\<Int32>

**读写能力：** 可读写

**起始版本：** 19

### var satelliteConstellation

```cangjie
public var satelliteConstellation: Array<SatelliteConstellationCategory>
```

**功能：** 表示卫星星座类型。

**类型：** Array\<[SatelliteConstellationCategory](#enum-satelliteconstellationcategory)>

**读写能力：** 可读写

**起始版本：** 19

### var satelliteIds

```cangjie
public var satelliteIds: Array<Int32>
```

**功能：** 表示每个卫星的ID，数组类型。取值范围为大于等于0。

**类型：** Array\<Int32>

**读写能力：** 可读写

**起始版本：** 19

### var satellitesNumber

```cangjie
public var satellitesNumber: Int32
```

**功能：** 表示卫星个数。取值范围为大于等于0。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19