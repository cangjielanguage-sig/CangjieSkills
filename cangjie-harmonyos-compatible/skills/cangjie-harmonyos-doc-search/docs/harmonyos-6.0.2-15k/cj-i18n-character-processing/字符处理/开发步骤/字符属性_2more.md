### 字符属性

字符属性用于判断字符类别，如判断字符是否为数字、字母、空格，是否为从右到左语言的字符，是否为表意文字（主要涉及中文、日文、韩文）等。

该功能通过 `Unicode` 类的 [isDigit](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#static-func-isdigitstring) 等接口实现，具体开发步骤如下：

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 判断字符属性。

   ```cangjie
   let isDigit: Bool = Unicode.isDigit(text: String)
   ```

3. 以一般类别值为例，判断字符类型，具体请参见 `getType` 接口文档。

   ```cangjie
   let unicodeType: String = Unicode.getType(text: String)
   ```

**开发实例**

<!-- run -->

```cangjie
// 导入模块
import kit.LocalizationKit.*

// 判断字符是否是数字
let isDigit: Bool = Unicode.isDigit('1') // isDigit = true

// 判断字符是否是从右到左语言的字符
let isRTL: Bool = Unicode.isRTL('a') // isRTL = false

// 判断字符是否是表意文字
let isIdeograph: Bool = Unicode.isIdeograph('华') // isIdeograph = true

// 获取字符的一般类别值
let unicodeType: String = Unicode.getType('a') // unicodeType = 'U_LOWERCASE_LETTER'
```

### 音译

音译是指以当地语言发音相近的内容替换原本的内容。通过 `Transliterator` 类的 [transform](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#func-transformstring) 接口实现，具体开发步骤如下：

> **说明：**
>
> 本模块支持中文汉字转为拼音，但对于多音字无法根据上下文语义有效处理。

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 创建 `Transliterator` 对象，获取音译列表。

   ```cangjie
   let ids: Array<String> = Transliterator.getAvailableIDs() // 获取音译支持的ID列表
   let transliterator: Transliterator = Transliterator.getInstance(id: String) // 传入音译支持的ID，创建Transliterator对象
   ```

3. 音译文本。

   ```cangjie
   let translatedText: String = transliterator.transform(text: String) // 对text内容进行音译
   ```

**开发实例**

<!-- run -->

```cangjie
// 导入模块
import kit.LocalizationKit.*

// 音译成Latn格式
let transliterator: Transliterator = Transliterator.getInstance('Any-Latn')
let text: String = '中国'
var translatedText: String = transliterator.transform(text) // translatedText = 'zhōng guó'

// 汉语音译去声调
let toneLessTransliterator: Transliterator = Transliterator.getInstance('Any-Latn;Latin-Ascii')
translatedText = toneLessTransliterator.transform('中国') // translatedText = 'zhong guo'

// 汉语姓氏读音
let nameTransliterator: Transliterator = Transliterator.getInstance('Han-Latin/Names')
translatedText = nameTransliterator.transform('单老师') // translatedText = 'shàn lǎo shī'

translatedText = nameTransliterator.transform('长孙无忌') // translatedText = 'zhǎng sūn wú jì'

// 获取音译支持的ID列表
let ids: Array<String> = Transliterator.getAvailableIDs() // ids = ['ASCII-Latin', 'Accents-Any', ...]
```