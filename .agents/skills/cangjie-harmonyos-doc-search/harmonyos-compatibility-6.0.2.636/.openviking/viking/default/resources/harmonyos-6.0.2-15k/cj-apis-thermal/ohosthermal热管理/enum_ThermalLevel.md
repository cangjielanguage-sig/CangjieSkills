## enum ThermalLevel

```cangjie
public enum ThermalLevel <: Equatable<AVCastCategory> & ToString {
    | Cool
    | Normal
    | Warm
    | Hot
    | Overheated
    | Warning
    | Emergency
    | Escape
    | ...
}
```

**功能：** 热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**起始版本：** 20

**父类型：**

- Equatable\<[ThermalLevel](#enum-thermallevel)>
- ToString

### Cool

```cangjie
Cool
```

**功能：** 表明设备处于清凉状态，业务执行不受热控的限制。

**起始版本：** 20

### Normal

```cangjie
Normal
```

**功能：** 表明设备温度正常，但邻近温热状态，无感知业务应降低规格和负载。

**起始版本：** 20

### Warm

```cangjie
Warm
```

**功能：** 表明设备进入温热状态，无感知业务应暂停或延迟运行。

**起始版本：** 20

### Hot

```cangjie
Hot
```

**功能：** 表明设备发热明显，无感知业务应停止，非关键业务应降低规格及负载。

**起始版本：** 20

### Overheated

```cangjie
Overheated
```

**功能：** 表明设备发热严重，无感知业务与非关键业务应停止，前台关键业务应降低规格及负载。

**起始版本：** 20

### Warning

```cangjie
Warning
```

**功能：** 表明设备过热即将进入紧急状态，整机资源供给大幅降低，停止所有非关键业务，前台关键业务应降低至最低规格。

**起始版本：** 20

### Emergency

```cangjie
Emergency
```

**功能：** 表明设备已经进入过热紧急状态，整机资源供给降至最低，设备功能受限，仅保留基础功能可用。

**起始版本：** 20

### Escape

```cangjie
Escape
```

**功能：** 表明设备即将进入热逃生状态，所有业务将被强制停止，业务需做好逃生措施，例如保存重要数据等。

**起始版本：** 20

### func !=(ThermalLevel)

```cangjie
public operator func !=(other: ThermalLevel): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ThermalLevel](#enum-thermallevel)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(ThermalLevel)

```cangjie
public operator func ==(other: ThermalLevel): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ThermalLevel](#enum-thermallevel)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|