### class RichEditorImageSpanStyle

```cangjie
public class RichEditorImageSpanStyle {
    public init(size!: (Length, Length), verticalAlign!: ImageSpanAlignment = ImageSpanAlignment.BASELINE, objectFit!: ImageFit = ImageFit.Cover)
    public init(verticalAlign!: ImageSpanAlignment = ImageSpanAlignment.BASELINE, objectFit!: ImageFit = ImageFit.Cover)
}
```

**功能：** 图片样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init((Length, Length), ImageSpanAlignment, ImageFit)

```cangjie
public init(size!: (Length, Length), verticalAlign!: ImageSpanAlignment = ImageSpanAlignment.BASELINE, objectFit!: ImageFit = ImageFit.Cover)
```

**功能：** 创建RichEditorImageSpanStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| size | ([Length](./cj-common-types.md#interface-length), [Length](./cj-common-types.md#interface-length)) | 是 | - | **命名参数。**  图片宽度和高度。<br>初始值：size的默认值与objectFit的值有关，不同的objectFit值对应的size默认值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。不支持以Percentage形式设置。 |
| verticalAlign | [ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment) | 否 | ImageSpanAlignment.BASELINE | **命名参数。**  图片垂直对齐方式。 |
| objectFit | [ImageFit](./cj-common-types.md#enum-imagefit) | 否 | ImageFit.Cover | **命名参数。**  图片缩放类型。 |

#### init(ImageSpanAlignment, ImageFit)

```cangjie
public init(verticalAlign!: ImageSpanAlignment = ImageSpanAlignment.BASELINE, objectFit!: ImageFit = ImageFit.Cover)
```

**功能：** 创建RichEditorImageSpanStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| verticalAlign | [ImageSpanAlignment](./cj-common-types.md#enum-imagespanalignment) | 否 | ImageSpanAlignment.BASELINE | **命名参数。**  图片垂直对齐方式。 |
| objectFit | [ImageFit](./cj-common-types.md#enum-imagefit) | 否 | ImageFit.Cover | **命名参数。**  图片缩放类型。 |