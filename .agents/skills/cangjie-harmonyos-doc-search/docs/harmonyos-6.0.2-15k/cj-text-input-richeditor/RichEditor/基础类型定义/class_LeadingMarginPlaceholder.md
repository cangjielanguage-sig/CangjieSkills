### class LeadingMarginPlaceholder

```cangjie
public class LeadingMarginPlaceholder {
    public init(pixelMap!: PixelMap, size!: (Length, Length))
}
```

**功能：** 前导边距占位符，用于表示文本段落左侧与组件边缘之间的距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(PixelMap, (Length, Length))

```cangjie
public init(pixelMap!: PixelMap, size!: (Length, Length))
```

**功能：** 创建LeadingMarginPlaceholder类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| pixelMap | PixelMap | 是 | - | **命名参数。**  图片内容。 |
| size | ([Length](./cj-common-types.md#interface-length), [Length](./cj-common-types.md#interface-length)) | 是 | - | **命名参数。**  图片大小，不支持设置百分比。 |