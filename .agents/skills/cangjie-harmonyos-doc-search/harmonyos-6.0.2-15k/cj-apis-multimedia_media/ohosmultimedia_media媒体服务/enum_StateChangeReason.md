## enum StateChangeReason

```cangjie
public enum StateChangeReason <: Equatable<StateChangeReason> & ToString {
    | USER
    | BACKGROUND
    | ...
}
```

**功能：** 表示播放或录制实例状态机切换原因的枚举，伴随state一起上报。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- Equatable\<StateChangeReason>
- ToString

### BACKGROUND

```cangjie
BACKGROUND
```

**功能：** 表示后台系统行为造成的状态切换，比如应用未注册播控中心权限，退到后台时被系统强制暂停或停止。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### USER

```cangjie
USER
```

**功能：** 表示用户行为造成的状态切换，由用户或客户端主动调用接口产生。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func !=(StateChangeReason)

```cangjie
public operator func !=(other: StateChangeReason): Bool
```

**功能：** 判断两个StateChangeReason是否不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StateChangeReason](#enum-statechangereason)|是|-|另一StateChangeReason。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个StateChangeReason不等返回true，否则返回false。|

### func ==(StateChangeReason)

```cangjie
public operator func ==(other: StateChangeReason): Bool
```

**功能：** 判断两个StateChangeReason是否相等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[StateChangeReason](#enum-statechangereason)|是|-|另一StateChangeReason。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个StateChangeReason相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回StateChangeReason的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回StateChangeReason的字符串表示。|