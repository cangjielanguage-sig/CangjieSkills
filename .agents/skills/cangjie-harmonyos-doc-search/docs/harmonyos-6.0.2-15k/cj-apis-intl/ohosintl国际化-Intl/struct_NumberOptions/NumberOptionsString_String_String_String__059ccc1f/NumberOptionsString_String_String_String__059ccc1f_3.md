// 用科学计数法显示数字
let n1 = NumberOptions(notation: "scientific", maximumSignificantDigits: 3)
let numberFormat1 = NumberFormat('zh-CN', options: n1)
let formattedNumber1 = numberFormat1.format(123400.00) // formattedNumber1: 1.23E5

// 用紧凑的格式显示数字
let n2 = NumberOptions(notation: "compact", compactDisplay: "short")
let numberFormat2 = NumberFormat('zh-CN', options: n2)
let formattedNumber2 = numberFormat2.format(123400.00) // formattedNumber2: 12万

// 显示数字的符号
let n3 = NumberOptions(signDisplay: "always")
let numberFormat3 = NumberFormat('zh-CN', options: n3)
let formattedNumber3 = numberFormat3.format(123400.00) // formattedNumber3: +123,400

// 显示百分数
let n4 = NumberOptions(style: "percent")
let numberFormat4 = NumberFormat('zh-CN', options: n4)
let formattedNumber4 = numberFormat4.format(0.25) // formattedNumber4: 25%

// 格式化货币
let n5 = NumberOptions(style: "currency", currency: "USD")
let numberFormat5 = NumberFormat('zh-CN', options: n5)
let formattedNumber5 = numberFormat5.format(123400.00) // formattedNumber5: US$123,400.00

// 用名称表示货币
let n6 = NumberOptions(style: "currency", currency: "USD", currencyDisplay: "name")
let numberFormat6 = NumberFormat('zh-CN', options: n6)
let formattedNumber6 = numberFormat6.format(123400.00) // formattedNumber6: 123,400.00美元

// 格式化度量衡
let n7 = NumberOptions(style: "unit", unit: "hectare")
let numberFormat7 = NumberFormat('en-GB', options: n7)
let formattedNumber7 = numberFormat7.format(123400.00) // formattedNumber7: 123,400 ha

// 格式化特定场景下度量衡，如面积-土地-农业
let n8 = NumberOptions(style: "unit", unit: "hectare", unitUsage: "area-land-agricult")
let numberFormat8 = NumberFormat('en-GB', options: n8)
let formattedNumber8 = numberFormat8.format(123400.00) // formattedNumber8: 304,928.041 ac
```