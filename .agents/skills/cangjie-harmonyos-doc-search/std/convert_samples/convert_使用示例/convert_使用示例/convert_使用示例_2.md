println("After the conversion of parse, \"18446744073709551615\" became ${UInt64.parse(strUInt64_parse)}")
    println("After the conversion of tryParse, \"18446744073709551615\" became ${UInt64.tryParse(strUInt64_tryParse)}")
    return 0
}
```

运行结果：

```text
After the conversion of parse, "true" became true
After the conversion of tryParse, "false" became Some(false)
After the conversion of parse, "'a'" became a
After the conversion of tryParse, "'\u{00e2}'" became Some(â)
After the conversion of parse, "-128" became -128
After the conversion of tryParse, "127" became Some(127)
After the conversion of parse, "-32768" became -32768
After the conversion of tryParse, "32767" became Some(32767)
After the conversion of parse, "-2147483648" became -2147483648
After the conversion of tryParse, "2147483647" became Some(2147483647)
After the conversion of parse, "-9223372036854775808" became -9223372036854775808
After the conversion of tryParse, "9223372036854775807" became Some(9223372036854775807)
After the conversion of parse, "-65504.0" became -65504.000000
After the conversion of tryParse, "65504.0" became Some(65504.000000)
After the conversion of parse, "-3.14159" became -3.141590
After the conversion of tryParse, "3.14159" became Some(3.141590)
After the conversion of parse, "-3.1415926" became -3.141593
After the conversion of tryParse, "3.1415926" became Some(3.141593)
After the conversion of parse, "255" became 255
After the conversion of tryParse, "255" became Some(255)
After the conversion of parse, "65535" became 65535
After the conversion of tryParse, "65535" became Some(65535)
After the conversion of parse, "4294967295" became 4294967295
After the conversion of tryParse, "4294967295" became Some(4294967295)
After the conversion of parse, "18446744073709551615" became 18446744073709551615
After the conversion of tryParse, "18446744073709551615" became Some(18446744073709551615)
```