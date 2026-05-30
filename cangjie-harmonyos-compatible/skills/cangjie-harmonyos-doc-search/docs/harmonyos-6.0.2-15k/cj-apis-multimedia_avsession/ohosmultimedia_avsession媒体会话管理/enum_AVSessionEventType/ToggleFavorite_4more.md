### ToggleFavorite

```cangjie
ToggleFavorite
```

**功能：** 是否收藏监听事件，当设置播放速率的命令被发送到会话时触发，提供String，表示媒体id。

**起始版本：** 19

### func !=(AVSessionEventType)

```cangjie
public operator func !=(other: AVSessionEventType): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVSessionEventType](#enum-avsessioneventtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(AVSessionEventType)

```cangjie
public operator func ==(other: AVSessionEventType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVSessionEventType](#enum-avsessioneventtype)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 会话监听事件提供的转字符串方法。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回对应事件小驼峰写法的字符串。|