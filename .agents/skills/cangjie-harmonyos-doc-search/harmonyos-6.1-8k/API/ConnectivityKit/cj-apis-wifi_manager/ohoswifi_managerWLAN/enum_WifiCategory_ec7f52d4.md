## enum WifiCategory

```cangjie
public enum WifiCategory <: Equatable<WifiCategory> & ToString {
    | Default
    | Wifi6
    | Wifi6Plus
    | ...
}
```

**功能：** 表示热点支持的最高wifi类别。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**父类型：**

- Equatable\<WifiCategory>
- ToString

### Default

```cangjie
Default
```

**功能：** Default。Wifi6以下的wifi类别。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### Wifi6

```cangjie
Wifi6
```

**功能：** Wifi6。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### Wifi6Plus

```cangjie
Wifi6Plus
```

**功能：** Wifi6+。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### func !=(WifiCategory)

```cangjie
public operator func !=(other: WifiCategory): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WifiCategory](#enum-wificategory)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(WifiCategory)

```cangjie
public operator func ==(other: WifiCategory): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WifiCategory](#enum-wificategory)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|