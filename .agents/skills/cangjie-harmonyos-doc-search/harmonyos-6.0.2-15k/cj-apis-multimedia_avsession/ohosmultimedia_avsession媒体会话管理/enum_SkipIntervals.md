## enum SkipIntervals

```cangjie
public enum SkipIntervals <: Equatable<SkipIntervals> & ToString {
    | SECONDS_10
    | SECONDS_15
    | SECONDS_30
    | ...
}
```

**功能：** 表示session支持的快进快退时间间隔的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[SkipIntervals](#enum-skipintervals)>
- ToString

### SECONDS_10

```cangjie
SECONDS_10
```

**功能：** 时间为10秒。

**起始版本：** 19

### SECONDS_15

```cangjie
SECONDS_15
```

**功能：** 时间为15秒。

**起始版本：** 19

### SECONDS_30

```cangjie
SECONDS_30
```

**功能：** 时间为30秒。

**起始版本：** 19

### func !=(SkipIntervals)

```cangjie
public operator func !=(other: SkipIntervals): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SkipIntervals](#enum-skipintervals)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(SkipIntervals)

```cangjie
public operator func ==(other: SkipIntervals): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SkipIntervals](#enum-skipintervals)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|