# 获取系统语言与区域

## 实现原理

在设置的“语言和地区”中可以添加多种语言，多种语言形成的列表称为语言列表，列表中的第一种语言称为系统语言。系统区域是依据区域标识划分的特定地区。

当设置/切换系统语言时，系统会检查[扩展参数](./cj-i18n-locale-culture.md)与系统语言是否匹配，若不匹配，则删除扩展属性。例如，当前系统语言设置为阿拉伯语“ar”，使用本地数字为“arab”。当系统语言切换为马来西亚语“my”时，本地数字属性更改为马来西亚的本地数字“mymr”。当切换为中文时，因中文不支持设置本地数字，采用阿拉伯数字，因此本地数字的扩展属性会被移除。

## 开发步骤

接口的具体使用方法和说明请参见[System](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#class-system)的API接口文档。

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 获取系统语言、系统地区、系统区域。

   ```cangjie
   // 获取系统语言
   let systemLanguage: String = System.getSystemLanguage() // systemLanguage为当前系统语言

   // 获取系统地区
   let systemRegion: String = System.getSystemRegion() // systemRegion为当前系统地区

   // 获取系统区域
   let systemLocale: String = System.getSystemLocale() // systemLocale为当前系统区域
   ```
