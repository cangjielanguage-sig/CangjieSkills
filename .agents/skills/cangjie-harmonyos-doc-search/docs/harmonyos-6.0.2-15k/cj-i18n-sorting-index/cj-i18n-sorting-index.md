# 创建索引

## 使用场景

当列表选项过多时，需要用户滑动窗口查找目标选项，为了快速找到目标选项，可以使用创建索引的方法。创建索引方式实质是打标签，例如，在联系人页面右侧通常会有“ABCD”的英文标记与联系人姓名首字母对应，若需寻找王同学，单击“W”可直接跳转到目标项范围。诸如“ABCD”的英文标记称为索引，通过创建索引的方式快速让窗口滑动到相应范围，找到目标选项。

## 开发步骤

接口的具体使用方法和说明请参见[IndexUtil](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#class-indexutil)的API接口文档。

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 创建对象。

   ```cangjie
   let indexUtil: IndexUtil = getInstance(locale!: String = "") // locale 表示本地化标识符，默认值是系统当前locale
   ```

3. 获取索引列表。

   ```cangjie
   let indexList: Array<String> = indexUtil.getIndexList()
   ```

4. 获取字符串的索引。

   ```cangjie
   let index: String = indexUtil.getIndex(text: String)
   ```

**开发实例**

<!-- run -->

```cangjie
// 导入模块
import kit.LocalizationKit.*

// 创建索引
let indexUtil: IndexUtil = getInstance(locale: 'zh-CN');
var indexList: Array<String> = indexUtil.getIndexList() // indexList = ['…', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '…']

// 多语言index混排
indexUtil.addLocale('ru-RU')
// indexList = ['…', 'A', 'B', 'C', ... 'X', 'Y', 'Z', '…', 'А', 'Б', 'В', ... 'Э', 'Ю', 'Я', '…']
indexList = indexUtil.getIndexList()

// 获取字符串的索引
let index: String = indexUtil.getIndex('你好') // index = 'N'
```
