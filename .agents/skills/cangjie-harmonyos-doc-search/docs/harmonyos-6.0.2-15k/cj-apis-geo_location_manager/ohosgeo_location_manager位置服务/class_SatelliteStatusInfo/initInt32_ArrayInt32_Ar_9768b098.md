### init(Int32, Array\<Int32>, Array\<Float64>, Array\<Float64>, Array\<Float64>, Array\<Float64>, Array\<SatelliteConstellationCategory>, Array\<Int32>)

```cangjie
public init(satellitesNumber: Int32, satelliteIds: Array<Int32>, carrierToNoiseDensitys: Array<Float64>,
    altitudes: Array<Float64>, azimuths: Array<Float64>, carrierFrequencies: Array<Float64>,
    satelliteConstellation!: Array<SatelliteConstellationCategory> = Array<SatelliteConstellationCategory>(),
    satelliteAdditionalInfo!: Array<Int32> = Array<Int32>())
```

**功能：** 构造SatelliteStatusInfo对象。

**系统能力：** SystemCapability.Location.Location.Gnss

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|satellitesNumber|Int32|是|-|表示卫星个数。取值范围为大于等于0。|
|satelliteIds|Array\<Int32>|是|-|表示每个卫星的ID，数组类型。取值范围为大于等于0。|
|carrierToNoiseDensitys|Array\<Float64>|是|-|表示载波噪声功率谱密度比，即cn0。取值范围为大于0。|
|altitudes|Array\<Float64>|是|-|表示卫星高度角信息。单位是“度”，取值范围为-90到90。|
|azimuths|Array\<Float64>|是|-|表示方位角。单位是“度”，取值范围为0到360。|
|carrierFrequencies|Array\<Float64>|是|-|表示载波频率。单位是Hz，取值范围为大于等于0。|
|satelliteConstellation|Array\<[SatelliteConstellationCategory](#enum-satelliteconstellationcategory)>|否|Array\<[SatelliteConstellationCategory](#enum-satelliteconstellationcategory)>()| **命名参数。** 表示卫星星座类型。|
|satelliteAdditionalInfo|Array\<Int32>|否|Array\<Int32>()| **命名参数。** 表示卫星的附加信息。<br/>每个比特位代表不同含义，具体定义参见[SatelliteAdditionalInfo](#enum-satelliteadditionalinfo)。|