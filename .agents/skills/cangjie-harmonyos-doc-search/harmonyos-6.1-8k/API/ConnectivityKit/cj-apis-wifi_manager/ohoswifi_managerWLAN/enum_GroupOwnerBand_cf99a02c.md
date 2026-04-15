## enum GroupOwnerBand

```cangjie
public enum GroupOwnerBand <: Equatable<GroupOwnerBand> & ToString {
    | GoBandAuto
    | GoBand2GHz
    | GoBand5GHz
    | ...
}
```

**功能：** 表示群组带宽。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**父类型：**

- Equatable\<GroupOwnerBand>
- ToString

### GoBand2GHz

```cangjie
GoBand2GHz
```

**功能：** 2.4GHZ。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### GoBand5GHz

```cangjie
GoBand5GHz
```

**功能：** 5GHZ。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### GoBandAuto

```cangjie
GoBandAuto
```

**功能：** 自动模式。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

### func !=(GroupOwnerBand)

```cangjie
public operator func !=(other: GroupOwnerBand): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GroupOwnerBand](#enum-groupownerband)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(GroupOwnerBand)

```cangjie
public operator func ==(other: GroupOwnerBand): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[GroupOwnerBand](#enum-groupownerband)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.WiFi.P2P

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|