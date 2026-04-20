## API 列表

### 类

|                 类名              |                功能                 |
| --------------------------------- | ---------------------------------- |
| [DateTimeFormat](./time_package_api/time_package_classes.md#class-datetimeformat) | 提供时间格式的功能，用于解析和生成 [DateTime](./time_package_api/time_package_structs.md#struct-datetime) 。|
| [TimeZone](./time_package_api/time_package_classes.md#class-timezone) | `TimeZone` 表示时区，记录了某一地区在不同时间较零时区的时间偏移，提供了从系统加载时区、自定义时区等功能。 |

### 枚举

|                 枚举名              |                功能                 |
| --------------------------------- | ---------------------------------- |
| [DayOfWeek](./time_package_api/time_package_enums.md#enum-dayofweek) | `DayOfWeek` 表示一周中的某一天，提供了与 `Int64` 类型转换，相等性判别以及获取枚举值的字符串表示的功能。 |
| [Month](./time_package_api/time_package_enums.md#enum-month) | `Month` 用以表示月份，表示一年中的某一月，提供了与 `Int64` 类型转换和计算，相等性判别以及获取枚举值的字符串表示的功能。 |

### 结构体

|                 结构体名              |                功能                 |
| --------------------------------- | ---------------------------------- |
| [DateTime](./time_package_api/time_package_structs.md#struct-datetime) | `DateTime` 表示日期时间，是一个描述某一时间点的时间类型，提供了基于时区的日期时间读取、计算、比较、转换，以及序列化和反序列化等功能。 |
| [MonoTime](./time_package_api/time_package_structs.md#struct-monotime) | `MonoTime` 表示单调时间，是一个用来衡量经过时间的时间类型，类似于一直运行的秒表，提供了获取当前时间，计算和比较等功能。 |

### 异常类

|                 异常类名              |                功能                 |
| --------------------------------- | ---------------------------------- |
| [InvalidDataException](./time_package_api/time_package_exceptions.md#class-invaliddataexception) | `InvalidDataException` 表示加载时区时的异常。 |
| [TimeParseException](./time_package_api/time_package_exceptions.md#class-timeparseexception) | `TimeParseException` 表示解析时间字符串时的异常。 |