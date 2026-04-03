## enum AVImageQueryOptions

```cangjie
public enum AVImageQueryOptions <: Equatable<AVImageQueryOptions> & ToString {
    | AV_IMAGE_QUERY_NEXT_SYNC
    | AV_IMAGE_QUERY_PREVIOUS_SYNC
    | AV_IMAGE_QUERY_CLOSEST_SYNC
    | AV_IMAGE_QUERY_CLOSEST
    | ...
}
```

**功能：** 需要获取的缩略图时间点与视频帧的对应关系。<br/>在获取视频缩略图时，传入的时间点与实际取得的视频帧所在时间点不一定相等，需要指定传入的时间点与实际取得的视频帧的时间关系。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

**父类型：**

- Equatable\<AVImageQueryOptions>
- ToString

### AV_IMAGE_QUERY_CLOSEST

```cangjie
AV_IMAGE_QUERY_CLOSEST
```

**功能：** 表示选取离传入时间点最近的帧，该帧不一定是关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

### AV_IMAGE_QUERY_CLOSEST_SYNC

```cangjie
AV_IMAGE_QUERY_CLOSEST_SYNC
```

**功能：** 表示选取离传入时间点最近的关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

### AV_IMAGE_QUERY_NEXT_SYNC

```cangjie
AV_IMAGE_QUERY_NEXT_SYNC
```

**功能：** 表示选取传入时间点或之后的关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

### AV_IMAGE_QUERY_PREVIOUS_SYNC

```cangjie
AV_IMAGE_QUERY_PREVIOUS_SYNC
```

**功能：** 表示选取传入时间点或之前的关键帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

### func !=(AVImageQueryOptions)

```cangjie
public operator func !=(other: AVImageQueryOptions): Bool
```

**功能：** 比较两个AVImageQueryOptions是否不等。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

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

**起始版本：** 19

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

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|AVImageQueryOptions的字符串表示。|