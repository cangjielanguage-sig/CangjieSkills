## enum WifiCallbackType

```cangjie
public enum WifiCallbackType <: Equatable<WifiCallbackType> & Hashable & ToString {
    | WifiScanStateChange
    | ...
}
```

**功能：** WLAN回调触发事件类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**父类型：**

- Equatable\<WifiCallbackType>
- Hashable
- ToString

### WifiScanStateChange

```cangjie
WifiScanStateChange
```

**功能：** 注册WLAN状态改变事件类型。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

### func !=(WifiCallbackType)

```cangjie
public operator func !=(other: WifiCallbackType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WifiCallbackType](#enum-wificallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(WifiCallbackType)

```cangjie
public operator func ==(other: WifiCallbackType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[WifiCallbackType](#enum-wificallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取输入数据的哈希值。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int64|数据的哈希值。|

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