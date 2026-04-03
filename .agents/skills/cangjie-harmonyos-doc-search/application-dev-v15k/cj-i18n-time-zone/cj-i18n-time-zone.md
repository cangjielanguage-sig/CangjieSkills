# 时区

## 使用场景

全球各国家和地区由于经度不同，地方时间也有所差异，因此划分了不同的时区。例如英国采用0时区，中国采用东8时区，中国时间要比英国快8个小时，中国北京中午12:00是英国伦敦凌晨4点。时区模块主要用于获取时区列表，同时，应用可基于获取的时区列表实现自身业务逻辑，如双时钟应用。

## 开发步骤

### 时区相关功能

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 开发实例，包括获取特定时区、计算固定和实际时区偏移量、获取和遍历时区列表等。

   ```cangjie
   // 获取巴西时区
   let timezone: TimeZone = getTimeZone(zoneID: 'America/Sao_Paulo') // 传入特定时区，创建时区类
   var timezoneId: String = timezone.getID() // timezoneId = 'America/Sao_Paulo'

   // 获取城市Id对应的时区对象
   let aucklandTimezone: TimeZone = TimeZone.getTimezoneFromCity('Auckland')
   timezoneId = aucklandTimezone.getID() // timezoneId = 'Pacific/Auckland'

   // 时区的本地化名称
   let timeZoneName: String = timezone.getDisplayName(locale: 'zh-Hans', isDST: true) // timeZoneName = '巴西利亚标准时间'

   // 本地化城市名称
   let cityDisplayName: String = TimeZone.getCityDisplayName('Auckland', 'zh-Hans') // cityDisplayName = '奥克兰 (新西兰)'

   // 时区的固定偏移量
   let rawOffset: Int32 = timezone.getRawOffset() // rawOffset = -10800000

   // 时区的实际偏移量（固定偏移量+夏令时）
   let offset: Int32 = timezone.getOffset(date: 1234567890.0) // offset = -10800000

   // 系统支持的时区Id列表
   let availableIDs: Array<String> = TimeZone.getAvailableIDs() // availableIDs = ['America/Adak', 'Asia/Hovd', ...]

   // 系统支持的时区城市Id列表
   let cityIDs: Array<String> = TimeZone.getAvailableZoneCityIDs() // cityIDs = ['Auckland', 'Magadan', ...]

   public struct Item {
      public Item(
         var cityDisplayName!: String = "",
         var timezoneId!: String = "",
         var offset!: String = "",
         var cityId!: String = ""
      ) {}
   }

   // 遍历时区城市Id列表
   let timezoneList: Array<Item> = [] // 呈现给用户的时区列表

   for (i in 0..cityIDs.size) {
      let cityId: String = cityIDs[i]
      let timezone: TimeZone = TimeZone.getTimezoneFromCity(cityId) // 城市Id对应的时区对象
      let cityDisplayName: String = TimeZone.getCityDisplayName(cityId, 'zh-CN') // 本地化城市名称
      let timestamp = 1672531200.0 // any INT32 value
      let item: Item = Item(
            cityDisplayName: cityDisplayName,
            timezoneId: timezone.getID(),
            offset: "GMT${(timezone.getOffset(date: timestamp) / 3600 * 1000)}",
            cityId: cityId
      )
      timezoneList.add(item)
   }

   // 指定地理坐标所在的时区对象数组
   let timezoneArray: Array<TimeZone> = TimeZone.getTimezonesByLocation(-43.1, -22.5)
   ```

### 双时钟应用

1. 导入模块。

   ```cangjie
   import kit.LocalizationKit.*
   ```

2. 选择时区列表中的时区放入应用偏好时区列表中。

   ```cangjie
   let pauloTimezone: TimeZone = getTimeZone(zoneID: 'America/Sao_Paulo')
   let defaultTimezone: TimeZone = getTimeZone()
   let appPreferredTimeZoneList: ArrayList<TimeZone> = ArrayList<TimeZone>() // 应用偏好时区列表
   appPreferredTimeZoneList.add(pauloTimezone)
   appPreferredTimeZoneList.add(defaultTimezone)
   ```

3. 遍历应用偏好时区列表，获取各时区时间。

   ```cangjie
   let locale: String = System.getSystemLocale()
   for (i in 0..appPreferredTimeZoneList.size) {
      let timezone: String = appPreferredTimeZoneList[i].getID()
      let calendar: Calendar = getCalendar(locale)
      calendar.setTimeZone(timezone) // 设置日历对象的时区

      // 获取年月日时分秒
      let year: Int32 = calendar.get('year')
      let month: Int32 = calendar.get('month')
      let day: Int32 = calendar.get('date')
      let hour: Int32 = calendar.get('hour')
      let minute: Int32 = calendar.get('minute')
      let second: Int32 = calendar.get('second')
   }
   ```
