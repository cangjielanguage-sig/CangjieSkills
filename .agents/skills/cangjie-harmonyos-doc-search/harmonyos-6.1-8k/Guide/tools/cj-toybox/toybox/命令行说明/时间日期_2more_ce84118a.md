### 时间日期

| 命令 | 说明 |
| :- | :- |
| cal     | 打印日历。<br/>usage: cal [[month] year] |
| date    | 设置/获取当前日期/时间。<br/>usage: date [-u] [-r FILE] [-d DATE] [+DISPLAY\_FORMAT] [SET] |
| hwclock | 获取/设置硬件时钟。<br/>usage: hwclock [-rswtluf] |
| sleep   | 等待设置的时间后再退出。可以是小数。可选的后缀可以是“m”（分钟）、“h”（小时）、“d”（天）或“s”（秒，默认值）。<br/>usage: sleep DURATION |
| time    | 运行命令行并报告真实时间、用户时间和系统时间（以秒为单位）。(真实时间=时钟时间，用户时间=命令代码使用cpu的时间，系统时间=操作系统使用cpu的时间。)<br/>usage: time [-pv] COMMAND [ARGS...] |
| uptime  | 显示当前时间，系统运行了多长时间，用户数量，以及过去1、5和15分钟的系统负载平均值。<br/>usage: uptime [-ps] |
| usleep  | 等待设置的时间后再退出，单位微秒。<br/>usage: usleep MICROSECONDS |

### 登录用户操作

| 命令 | 说明 |
| :- | :- |
| groups  | 打印用户所在的组。<br/>usage: groups [user] |
| id      | 打印用户和组ID。<br/>usage: id [-nGgru] [USER...] |
| login   | 用户登录。<br/>usage: login [-p] [-h host] [-f USERNAME] [USERNAME] |
| logname/whoami | 打印当前用户名。<br/>usage: logname/whoami |
| passwd  | 更新用户的认证令牌。<br/>usage: passwd [-a ALGO] [-dlu] [USER] |
| who     | 打印有关已登录用户的信息。 <br/>usage: who |
| w       | 显示用户登录情况和登录时间。<br/>usage: w |