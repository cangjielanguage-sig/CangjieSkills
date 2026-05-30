## 使用场景

当应用自身不具备图片编辑能力、但存在图片编辑的场景时，可以通过startAbilityByType拉起图片编辑类应用扩展面板，由对应的应用完成图片编辑操作。图片编辑类应用可以通过PhotoEditorExtensionAbility实现图片编辑页面，并将该页面注册到图片编辑面板，从而将图片编辑能力开放给其他应用。

流程示意图如下：

![photoEditorExtensionAbility](figures/photoEditorExtensionAbility.png)

例如：用户在图库App中选择编辑图片时，图库App可以通过startAbilityByType拉起图片编辑类应用扩展面板。用户可以从已实现PhotoEditorExtensionAbility应用中选择一款，并进行图片编辑。

## 接口说明

接口详情参见[PhotoEditorExtensionAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-photoeditorextensionability)和[PhotoEditorExtensionContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-photoeditorextensioncontext)。

| **接口名**  | **描述** |
| -------- | -------- |
| onStartContentEditing(uri: String, want: Want, session: UIExtensionContentSession): Unit       | 可以执行读取原始图片、加载页面等操作。|
| saveEditedContentWithImage(pixelMap: PixelMap, option: PackingOption): AbilityResult  | 传入编辑过的图片的PixelMap对象并保存。   |