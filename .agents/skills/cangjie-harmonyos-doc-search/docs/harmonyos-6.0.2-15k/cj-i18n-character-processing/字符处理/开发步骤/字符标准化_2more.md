### 字符标准化

字符标准化是指按指定的范式标准化字符。通过 `Normalizer` 类的 [normalize](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#func-normalizestring) 接口实现，具体开发步骤如下：

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 创建标准化对象。传入文本标准化的范式，创建标准化对象，文本标准化的范式包括NFC、NFD、NFKC和NFKD，范式的详细介绍请参见[国际标准](https://www.unicode.org/reports/tr15/#Norm_Forms)。

   ```cangjie
   let normalizer: Normalizer = Normalizer.getInstance(mode: NormalizerMode)
   ```

3. 文本标准化。

   ```cangjie
   let normalizedText: String = normalizer.normalize(text: String); // 对text文本进行标准化
   ```

**开发实例**

<!-- run -->

```cangjie
// 导入模块
import kit.LocalizationKit.*

// 以NFC范式标准化字符
let normalizer: Normalizer = Normalizer.getInstance(NormalizerMode.NFC)
let normalizedText: String = normalizer.normalize("\u{1E9B}\u{0323}") // normalizedText = 'ẛ̣'
```

### 断词换行

断词换行是指根据设定的区域参数获取文本中的分割点，通过 [BreakIterator](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#class-breakiterator) 类的接口实现，具体开发步骤如下：

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 创建用于断句的对象。
   传入合法的locale参数，生成BreakIterator类型的对象，该对象将按照locale所指定的区域的规则进行断句。

   ```cangjie
   let iterator: BreakIterator = getLineInstance(locale: string)
   ```

3. 设置要处理的文本。

   ```cangjie
   iterator.setLineBreakText(text: String) // 设置要处理的文本
   let breakText: String = iterator.getLineBreakText() // 查看iterator正在处理的文本
   ```

4. 获取可断句的位置。

   ```cangjie
   let currentPos: Int32 = iterator.current() // 获取iterator在当前所处理文本中的位置
   let firstPos: Int32 = iterator.first() // 设置为第一个可断句的分割点，返回该分割点的位置。第一个分割点总是在文本的起始位置，firstPos = 0
   let nextPos: Int32 = iterator.next(index!: Int32 = 1) // 将iterator移动index数量个分割点，index为正数代表向后移动，index为负数代表向前移动，默认值为1。nextPos为移动后在文本中的位置，如果超出文本的长度范围，返回-1
   let isBoundary: Bool = iterator.isBoundary(offset: Int32) // 判断offset位置是否是分割点
   ```

**开发实例**

<!-- run -->

```cangjie
// 导入模块
import kit.LocalizationKit.*

// 断句对象
let iterator: BreakIterator  = getLineInstance('en-GB')

// 断句文本
iterator.setLineBreakText('Apple is my favorite fruit.')

// 将BreakIterator对象移动到文本起始位置
let firstPos: Int32 = iterator.first() // firstPos = 0

// 将BreakIterator对象移动几个分割点
let nextPos: Int32 = iterator.next(index: 2) // nextPos = 9

// 判断某个位置是否是分割点
let isBoundary: Bool = iterator.isBoundary(9) // isBoundary = true

// 获取BreakIterator对象处理的文本
let breakText: String = iterator.getLineBreakText() // breakText = 'Apple is my favorite fruit.'
```