## enum AVImageQueryOptions

```cangjie
public enum AVImageQueryOptions <: Equatable<AVImageQueryOptions> & ToString {
    | AvImageQueryNextSync
    | AvImageQueryPreviousSync
    | AvImageQueryClosestSync
    | AvImageQueryClosest
    | ...
}
```

**功能：** 需要获取的缩略图时间点与视频帧的对应关系。

在获取视频缩略图时，传入的时间点与实际取得的视频帧所在时间点不一定相等，需要指定传入的时间点与实际取得的视频帧的时间关系。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

**父类型：**

- Equatable\<AVImageQueryOptions>
- ToString

### AvImageQueryClosest

```cangjie
AvImageQueryClosest
```

**功能：** 表示选取离传入时间点最近的帧，该帧不一定是关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

### AvImageQueryClosestSync

```cangjie
AvImageQueryClosestSync
```

**功能：** 表示选取离传入时间点最近的关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

### AvImageQueryNextSync

```cangjie
AvImageQueryNextSync
```

**功能：** 表示选取传入时间点或之后的关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

### AvImageQueryPreviousSync

```cangjie
AvImageQueryPreviousSync
```

**功能：** 表示选取传入时间点或之前的关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

### func !=(AVImageQueryOptions)

```cangjie
public operator func !=(other: AVImageQueryOptions): Bool
```

**功能：** 比较两个AVImageQueryOptions是否不等。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVImageQueryOptions](#enum-avimagequeryoptions)|是|-|另一AVImageQueryOptions实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个AVImageQueryOptions不等返回true，否则返回false。|

### func ==(AVImageQueryOptions)

```cangjie
public operator func ==(other: AVImageQueryOptions): Bool
```

**功能：** 比较两个AVImageQueryOptions是否相等。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AVImageQueryOptions](#enum-avimagequeryoptions)|是|-|另一AVImageQueryOptions实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个AVImageQueryOptions相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回AVImageQueryOptions的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|AVImageQueryOptions的字符串表示。|