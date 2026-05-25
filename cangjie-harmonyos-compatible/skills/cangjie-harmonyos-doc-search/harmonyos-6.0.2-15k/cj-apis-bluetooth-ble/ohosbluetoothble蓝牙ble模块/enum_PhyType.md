## enum PhyType

```cangjie
public enum PhyType <: Equatable<PhyType> & ToString {
    | PHY_LE_1M
    | PHY_LE_ALL_SUPPORTED
    | ...
}
```

**功能：** 广播状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<PhyType>
- ToString

### PHY_LE_1M

```cangjie
PHY_LE_1M
```

**功能：** 表示扫描中使用1M PHY。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### PHY_LE_ALL_SUPPORTED

```cangjie
PHY_LE_ALL_SUPPORTED
```

**功能：** 表示扫描中使用蓝牙协议支持的PHY模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(PhyType)

```cangjie
public operator func !=(other: PhyType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[PhyType](#enum-phytype)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(PhyType)

```cangjie
public operator func ==(other: PhyType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[PhyType](#enum-phytype)|是|另一个枚举值。|

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