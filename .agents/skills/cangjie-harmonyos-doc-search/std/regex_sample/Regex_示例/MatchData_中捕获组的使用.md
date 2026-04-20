## MatchData 中捕获组的使用

示例：

<!-- verify -->
```cangjie
import std.regex.*

main(): Unit {
    var r = Regex(#"(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})"#)
    for (md in r.lazyFindAll("2024-10-24&2025-01-01", group: true)) {
        println("# found: `${md.matchString()}` and groupCount: ${md.groupCount()}")
        if (md.groupCount() > 0) {
            for (i in 0..=md.groupCount()) {
                println("group[${i}] : ${md.matchString(i)}")
                let pos = md.matchPosition(i)
                println("position : [${pos.start}, ${pos.end})")
            }
        }
        for ((name, index) in r.getNamedGroups()) {
            let pos = md.matchPosition(name)
            println("${name} 是第 ${index} 组, position: [${pos.start}, ${pos.end}), 捕获: ${md.matchString(name)}")
        }
    }
}
```

运行结果：

```text
# found: `2024-10-24` and groupCount: 3
group[0] : 2024-10-24
position : [0, 10)
group[1] : 2024
position : [0, 4)
group[2] : 10
position : [5, 7)
group[3] : 24
position : [8, 10)
day 是第 3 组, position: [8, 10), 捕获: 24
month 是第 2 组, position: [5, 7), 捕获: 10
year 是第 1 组, position: [0, 4), 捕获: 2024
# found: `2025-01-01` and groupCount: 3
group[0] : 2025-01-01
position : [11, 21)
group[1] : 2025
position : [11, 15)
group[2] : 01
position : [16, 18)
group[3] : 01
position : [19, 21)
day 是第 3 组, position: [19, 21), 捕获: 01
month 是第 2 组, position: [16, 18), 捕获: 01
year 是第 1 组, position: [11, 15), 捕获: 2025
```