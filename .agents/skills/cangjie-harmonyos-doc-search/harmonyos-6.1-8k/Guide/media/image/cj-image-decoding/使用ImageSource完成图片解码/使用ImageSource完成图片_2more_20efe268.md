# 使用ImageSource完成图片解码

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

图片解码指将所支持格式的存档图片解码成统一的[PixelMap](./cj-image-overview.md)，以便在应用或系统中进行图片显示或[图片处理](./cj-image-transformation.md)。当前支持的存档图片格式包括JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG 和 HEIF（不同硬件设备支持情况可能有所不同）。

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../reference/cj-development-intro.md#仓颉示例代码说明)。