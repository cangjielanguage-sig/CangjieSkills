## enum KeyOfCallState

```cangjie
public enum KeyOfCallState <: Equatable<KeyOfCallState> {
    | KEY_OF_CALLSTATE_STATE
    | KEY_OF_CALLSTATE_MUTED
    | ...
}
```

**功能：** 通话状态相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[KeyOfCallState](#enum-keyofcallstate)>

### KEY_OF_CALLSTATE_MUTED

```cangjie
KEY_OF_CALLSTATE_MUTED
```

**功能：** 通话mic是否静音。

**起始版本：** 19

### KEY_OF_CALLSTATE_STATE

```cangjie
KEY_OF_CALLSTATE_STATE
```

**功能：** 当前通话状态。

**起始版本：** 19

### func !=(KeyOfCallState)

```cangjie
public operator func !=(other: KeyOfCallState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyOfCallState](#enum-keyofcallstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(KeyOfCallState)

```cangjie
public operator func ==(other: KeyOfCallState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[KeyOfCallState](#enum-keyofcallstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的字符串表示。|