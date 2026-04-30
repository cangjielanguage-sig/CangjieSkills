## enum CastDisplayState

```cangjie
public enum CastDisplayState <: Equatable<CastDisplayState> & ToString {
    | STATE_ON
    | STATE_OFF
    | ...
}
```

**功能：** 投播显示设备状态的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**起始版本：** 19

**父类型：**

- Equatable\<[CastDisplayState](#enum-castdisplaystate)>
- ToString

### STATE_OFF

```cangjie
STATE_OFF
```

**功能：** 设备连接成功，扩展屏可用。

**起始版本：** 19

### STATE_ON

```cangjie
STATE_ON
```

**功能：** 设备断开，扩展屏不再显示内容。

**起始版本：** 19

### func !=(CastDisplayState)

```cangjie
public operator func !=(other: CastDisplayState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CastDisplayState](#enum-castdisplaystate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(CastDisplayState)

```cangjie
public operator func ==(other: CastDisplayState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CastDisplayState](#enum-castdisplaystate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|