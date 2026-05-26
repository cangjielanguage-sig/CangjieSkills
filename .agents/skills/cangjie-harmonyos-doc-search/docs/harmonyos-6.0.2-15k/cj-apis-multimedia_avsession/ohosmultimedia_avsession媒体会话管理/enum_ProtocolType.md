## enum ProtocolType

```cangjie
public enum ProtocolType <: Equatable<ProtocolType> & ToString {
    | TYPE_LOCAL
    | TYPE_CAST_PLUS_STREAM
    | TYPE_DLNA
    | ...
}
```

**功能：** 远端设备支持的协议类型的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**父类型：**

- Equatable\<[ProtocolType](#enum-protocoltype)>
- ToString

### TYPE_CAST_PLUS_STREAM

```cangjie
TYPE_CAST_PLUS_STREAM
```

**功能：** Cast+的Stream模式。表示媒体正在其他设备上展示。

**起始版本：** 19

### TYPE_DLNA

```cangjie
TYPE_DLNA
```

**功能：** DLNA协议。表示媒体正在其他设备上展示。

**起始版本：** 19

### TYPE_LOCAL

```cangjie
TYPE_LOCAL
```

**功能：** 本地设备，包括设备本身的内置扬声器或音频插孔、A2DP设备。

**起始版本：** 19

### func !=(ProtocolType)

```cangjie
public operator func !=(other: ProtocolType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProtocolType](#enum-protocoltype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(ProtocolType)

```cangjie
public operator func ==(other: ProtocolType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[ProtocolType](#enum-protocoltype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|