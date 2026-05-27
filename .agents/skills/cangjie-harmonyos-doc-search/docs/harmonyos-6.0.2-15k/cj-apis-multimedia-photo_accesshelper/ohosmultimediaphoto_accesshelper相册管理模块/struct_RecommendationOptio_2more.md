## struct RecommendationOptions

```cangjie
public struct RecommendationOptions {
    public RecommendationOptions(
        public var recommendationType!: ?RecommendationType = None,
        public var textContextInfo!: ?TextContextInfo = None
    )
}
```

**功能：** 图片推荐选项(基于图片数据分析结果，依赖设备适配)。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### var recommendationType

```cangjie
public var recommendationType: ?RecommendationType = None
```

**功能：** 文本。

**类型：** ?[RecommendationType](#enum-recommendationtype)

**读写能力：** 可读写

**起始版本：** 19

### var textContextInfo

```cangjie
public var textContextInfo: ?TextContextInfo = None
```

**功能：** 文本。

**类型：** ?[TextContextInfo](#struct-textcontextinfo)

**读写能力：** 可读写

**起始版本：** 19

### RecommendationOptions(?RecommendationType, ?TextContextInfo)

```cangjie
public RecommendationOptions(
    public var recommendationType!: ?RecommendationType = None,
    public var textContextInfo!: ?TextContextInfo = None
)
```

**功能：** 构造RecommendationOptions对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|recommendationType|?[RecommendationType](#enum-recommendationtype)|否|None| **命名参数。** 如果需要根据枚举值推荐相应的图片，则配置此参数。|
|textContextInfo|?[TextContextInfo](#struct-textcontextinfo)|否|None| **命名参数。** 如果需要根据文本信息推荐相应的图片，则配置此参数(如果同时配置了recommendationType，则仅textContextInfo生效)。|

## struct TextContextInfo

```cangjie
public struct TextContextInfo {
    public TextContextInfo (
        public let text!: String = ""
    )
}
```

**功能：** 文本信息，用于推荐图片的文本信息。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

### let text

```cangjie
public let text: String = ""
```

**功能：** 文本。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### TextContextInfo(String)

```cangjie
public TextContextInfo (public let text!: String = "")
```

**功能：** 构造TextContextInfo对象。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|text|String|否|""| **命名参数。** 如果需要根据文本(支持250字以内的简体中文)推荐相应的图片，则配置此参数。|