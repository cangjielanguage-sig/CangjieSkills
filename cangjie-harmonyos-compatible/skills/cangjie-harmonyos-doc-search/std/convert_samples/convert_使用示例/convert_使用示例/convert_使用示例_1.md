## convert 使用示例

示例：

<!-- verify -->
```cangjie
import std.convert.*

main(): Int64 {
    var strBool_parse: String = "true"
    var strBool_tryParse: String = "false"
    var strChar_parse: String = "'a'"
    var strChar_tryParse: String = "'\\u{00e2}'"
    var strInt8_parse: String = "-128"
    var strInt8_tryParse: String = "127"
    var strInt16_parse: String = "-32768"
    var strInt16_tryParse: String = "32767"
    var strInt32_parse: String = "-2147483648"
    var strInt32_tryParse: String = "2147483647"
    var strInt64_parse: String = "-9223372036854775808"
    var strInt64_tryParse: String = "9223372036854775807"
    var strFloat16_parse: String = "-65504.0"
    var strFloat16_tryParse: String = "65504.0"
    var strFloat32_parse: String = "-3.14159"
    var strFloat32_tryParse: String = "3.14159"
    var strFloat64_parse: String = "-3.1415926"
    var strFloat64_tryParse: String = "3.1415926"
    var strUInt8_parse: String = "255"
    var strUInt8_tryParse: String = "255"
    var strUInt16_parse: String = "65535"
    var strUInt16_tryParse: String = "65535"
    var strUInt32_parse: String = "4294967295"
    var strUInt32_tryParse: String = "4294967295"
    var strUInt64_parse: String = "18446744073709551615"
    var strUInt64_tryParse: String = "18446744073709551615"

    println("After the conversion of parse, \"true\" became ${Bool.parse(strBool_parse)}")
    println("After the conversion of tryParse, \"false\" became ${Bool.tryParse(strBool_tryParse)}")

    println("After the conversion of parse, \"'a'\" became ${Rune.parse(strChar_parse)}")
    println("After the conversion of tryParse, \"'\\u{00e2}'\" became ${Rune.tryParse(strChar_tryParse)}")

    println("After the conversion of parse, \"-128\" became ${Int8.parse(strInt8_parse)}")
    println("After the conversion of tryParse, \"127\" became ${Int8.tryParse(strInt8_tryParse)}")

    println("After the conversion of parse, \"-32768\" became ${Int16.parse(strInt16_parse)}")
    println("After the conversion of tryParse, \"32767\" became ${Int16.tryParse(strInt16_tryParse)}")

    println("After the conversion of parse, \"-2147483648\" became ${Int32.parse(strInt32_parse)}")
    println("After the conversion of tryParse, \"2147483647\" became ${Int32.tryParse(strInt32_tryParse)}")

    println("After the conversion of parse, \"-9223372036854775808\" became ${Int64.parse(strInt64_parse)}")
    println("After the conversion of tryParse, \"9223372036854775807\" became ${Int64.tryParse(strInt64_tryParse)}")

    println("After the conversion of parse, \"-65504.0\" became ${Float16.parse(strFloat16_parse)}")
    println("After the conversion of tryParse, \"65504.0\" became ${Float16.tryParse(strFloat16_tryParse)}")

    println("After the conversion of parse, \"-3.14159\" became ${Float32.parse(strFloat32_parse)}")
    println("After the conversion of tryParse, \"3.14159\" became ${Float32.tryParse(strFloat32_tryParse)}")

    println("After the conversion of parse, \"-3.1415926\" became ${Float64.parse(strFloat64_parse)}")
    println("After the conversion of tryParse, \"3.1415926\" became ${Float64.tryParse(strFloat64_tryParse)}")

    println("After the conversion of parse, \"255\" became ${UInt8.parse(strUInt8_parse)}")
    println("After the conversion of tryParse, \"255\" became ${UInt8.tryParse(strUInt8_tryParse)}")

    println("After the conversion of parse, \"65535\" became ${UInt16.parse(strUInt16_parse)}")
    println("After the conversion of tryParse, \"65535\" became ${UInt16.tryParse(strUInt16_tryParse)}")

    println("After the conversion of parse, \"4294967295\" became ${UInt32.parse(strUInt32_parse)}")
    println("After the conversion of tryParse, \"4294967295\" became ${UInt32.tryParse(strUInt32_tryParse)}")