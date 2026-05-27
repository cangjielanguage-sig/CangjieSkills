# 设置日历和历法

## 使用场景

不同地区的用户使用不同的日历，大多数地区使用公历，也有些地区的用户使用其他日历，例如农历、伊斯兰历或希伯来历。此外，日历上的时间和日期也会随着时区和夏令时的不同而改变。因此，用户应设置符合本地习惯的日历。国际化提供了[Calendar](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#class-calendar)类，可以设置日历类型、日期、年月日、时区、一周的起始日期、一年中第一周的最小天数、判断具体某一天在日历中是否为周末、计算相差天数等。在应用开发过程中，开发者可以根据业务需求选择使用不同功能。

## 开发步骤

以查看公历对应的农历日期为例，说明[Calendar](../../API_Reference/source_zh_cn/apis/LocalizationKit/cj-apis-i18n.md#class-calendar)类接口使用方法。

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 公历相关用法。

   ```cangjie
   import std.time.DateTime as d

   let calendar: Calendar = getCalendar('zh-Hans', calendarType: 'gregory')
   // 设置日历对象的时间日期为2022.05.13 08:00:00
   calendar.setTime(d.of(year: 2022,month: 5, dayOfMonth: 13, hour:5, minute:0))
   calendar.setTime(10540800000.0)

   // 设置日历对象的时间日期为2022.05.13 08:00:00
   calendar.set(2022, 5, 13, hour: 8, minute: 0, second: 0)

   // 设置日历对象的时区
   calendar.setTimeZone('Asia/Shanghai')

   // 获取日历对象的时区
   let timezone: String = calendar.getTimeZone() // timezone = 'Asia/Shanghai'

   // 获取日历对象的一周起始日
   let firstDayOfWeek: Int32 = calendar.getFirstDayOfWeek() // firstDayOfWeek = 1

   // 设置每一周的起始日
   calendar.setFirstDayOfWeek(1)

   // 获取一年中第一周的最小天数
   let minimalDaysInFirstWeek: Int32 = calendar.getMinimalDaysInFirstWeek() // minimalDaysInFirstWeek = 1

   // 设置一年中第一周的最小天数
   calendar.setMinimalDaysInFirstWeek(3)

   // 获取日历对象中与field相关联的值
   let year: Int32 = calendar.get('year') // year = 2022

   // 获取日历对象本地化名称
   let calendarName: String = calendar.getDisplayName('zh-Hans') // calendarName = '公历'

   // 判断指定的日期在日历中是否为周末
   let isWeekend: Bool = calendar.isWeekend(date: d.of(year: 2023,month: 9, dayOfMonth: 15)) // isWeekend = false

   // 在日历的给定字段进行加减操作
   calendar.set(2023, 10, 15)
   calendar.add('date', 2)
   let day: Int32 = calendar.get('date') // day = 17

   // 比较日历和指定日期相差的天数
   let daysDifference: Int32 = calendar.compareDays(d.of(year: 2023,month: 10, dayOfMonth: 15)) // daysDifference = -34
   ```

3. 获取公历对应的农历日期。

   ```cangjie
   import std.time.DateTime as d

   let calendar: Calendar = getCalendar('zh-Hans', calendarType: 'chinese')
   //将公历信息设置到calendar对象，时间日期为2023.07.25 08:00:00
   calendar.setTime(d.of(year: 2023,month: 7, dayOfMonth: 25, hour:8, minute:0))
   //获取农历年月日
   let year: Int32 = calendar.get('year') // year = 40，指干支纪年40，范围1-60
   let month: Int32 = calendar.get('month') // month = 5，指6月
   let day: Int32 = calendar.get('date') // day = 8，指8日
   ```

支持的日历类型如下：

| 类型 | 中文名称 |
| -------- | -------- |
| buddhist | 佛历 |
| chinese | 农历 |
| coptic | 科普特历 |
| ethiopic | 埃塞俄比亚历 |
| hebrew | 希伯来历 |
| gregory | 公历 |
| indian | 印度历 |
| islamic_civil | 伊斯兰希吉来历 |
| islamic_tbla | 伊斯兰天文历 |
| islamic_umalqura | 伊斯兰历（乌姆库拉） |
| japanese | 日本历 |
| persian | 波斯历 |
