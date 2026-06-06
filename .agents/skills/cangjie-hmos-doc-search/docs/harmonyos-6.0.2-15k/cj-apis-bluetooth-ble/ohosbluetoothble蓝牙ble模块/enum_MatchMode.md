## enum MatchMode

```cangjie
public enum MatchMode <: Equatable<MatchMode> & ToString {
    | MATCH_MODE_AGGRESSIVE
    | MATCH_MODE_STICKY
    | ...
}
```

**功能：** 硬件过滤匹配模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<MatchMode>
- ToString

### MATCH_MODE_AGGRESSIVE

```cangjie
MATCH_MODE_AGGRESSIVE
```

**功能：** 表示硬件上报扫描结果门限较低，比如扫描到的功率较低或者一段时间扫描到的次数较少也触发上报，默认值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### MATCH_MODE_STICKY

```cangjie
MATCH_MODE_STICKY
```

**功能：** 表示硬件上报扫描结果门限较高，更高的功率门限以及扫描到多次才会上报。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(MatchMode)

```cangjie
public operator func !=(other: MatchMode): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[MatchMode](#enum-matchmode)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(MatchMode)

```cangjie
public operator func ==(other: MatchMode): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[MatchMode](#enum-matchmode)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|