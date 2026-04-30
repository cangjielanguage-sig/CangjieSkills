## enum DisplayTag

```cangjie
public enum DisplayTag <: Equatable<DisplayTag> & ToString {
    | TAG_AUDIO_VIVID
    | ...
}
```

**功能：** 枚举，表示当前媒体资源的金标，即应用媒体音源的特殊类型标识。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[DisplayTag](#enum-displaytag)>
- ToString

### TAG_AUDIO_VIVID

```cangjie
TAG_AUDIO_VIVID
```

**功能：** AUDIO VIVID。

**起始版本：** 19

### func !=(DisplayTag)

```cangjie
public operator func !=(other: DisplayTag): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DisplayTag](#enum-displaytag)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(DisplayTag)

```cangjie
public operator func ==(other: DisplayTag): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DisplayTag](#enum-displaytag)|是|-|待比较的另一个枚举值。|

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