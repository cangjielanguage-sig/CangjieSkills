package macro_dsl

import std.collection.*
import std.sort.*
import macros.*

main(): Int64 {
    let data = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10]

    // Filter and transform
    let result = @query[Int64](from x in data where x > 5 select x * 2)
    print("Filtered and doubled:")
    for (v in result) {
        print(" ${v}")
    }
    println("")

    // Count
    let cnt = @query[count](from x in data where x > 5)
    println("Count > 5: ${cnt}")

    // Sort descending
    let sorted = @query[Int64](from x in data select x orderby desc)
    print("Sorted desc:")
    for (v in sorted) {
        print(" ${v}")
    }
    println("")

    return 0
}
