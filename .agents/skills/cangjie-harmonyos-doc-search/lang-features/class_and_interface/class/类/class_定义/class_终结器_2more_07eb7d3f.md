### class 终结器

`class` 支持定义终结器，当类的实例被垃圾回收时，会触发该函数。终结器的函数名固定为 `~init`，通常用于释放系统资源。如下示例中的 `unsafe`，详见 [unsafe 小节](../FFI/cangjie-c.md)：

<!-- compile -->

```cangjie
class C {
    var p: CString

    init(s: String) {
        p = unsafe { LibC.mallocCString(s) }
        println(s)
    }
    ~init() {
        unsafe { LibC.free(p) }
    }
}
```

使用终结器有些限制条件，需要开发者注意：

1. 终结器没有参数，没有返回类型，没有泛型类型参数，没有任何修饰符，也不可以被显式调用。
2. 带有终结器的类不可被 `open` 修饰，只有非 `open` 的类可以拥有终结器。
3. 一个类最多只能定义一个终结器。
4. 终结器不可以定义在扩展中。
5. 终结器被触发的时机是不确定的。
6. 终结器可能在任意一个线程上执行。
7. 多个终结器的执行顺序是不确定的。
8. 终结器向外抛出未捕获异常属于未定义行为。
9. 终结器中创建线程或者使用线程同步功能属于未定义行为。
10. 终结器执行结束之后，如果这个对象还可以被继续访问，则属于未定义行为。
11. 如果对象在初始化过程中抛出异常，这样未完整初始化的对象的终结器不会执行。
12. 依赖终结器的同步行为属于未定义行为。例如，下例中 `main` 函数通过 `while (Test.t0 != 0)` 等待 `Test` 类中的终结器修改 `t0` 的值，属于未定义行为。

    <!-- run -->

    ```cangjie
    import std.collection.ArrayList
    import std.runtime.gc

    class Test {
        public static var t0 : Int32 = 0
        public init () {
            t0++
        }
        ~init () {
            t0--
        }
    }

    var list: ArrayList<Test> = ArrayList<Test>()

    func foo() : Int32 {
        let o1 = Test()
        list.add(o1)
        if (Test.t0 != 1) {
            return 1
        }
        list.remove(at: 0)
        return 0
    }

    main(): Int64 {
        var i : Int64 = 0
        while (i < 100) {
            if (foo() != 0) {
                print("fail: obj is freed before gc!")
                return 1
            }
            gc(heavy: true) // blocking gc expected
            // wait ~init() to be executed
            while (Test.t0 != 0) {  // error, this is undefined behavior
                continue
            }
            i++
        }
        return 0
    }
    ```

### class 成员函数

`class` 成员函数同样分为实例成员函数和静态成员函数（使用 `static` 修饰符修饰），实例成员函数只能通过对象访问，静态成员函数只能通过 `class` 类型名访问；静态成员函数中不能访问实例成员变量，也不能调用实例成员函数，但在实例成员函数中可以访问静态成员变量以及静态成员函数。

下例中，`area` 是实例成员函数，`typeName` 是静态成员函数。

<!-- compile -->

```cangjie
class Rectangle {
    let width: Int64 = 10
    let height: Int64 = 20

    public func area() {
        this.width * this.height
    }

    public static func typeName(): String {
        "Rectangle"
    }
}
```

根据是否有函数体，实例成员函数又可以分为抽象成员函数和非抽象成员函数。抽象成员函数没有函数体，只能定义在抽象类或接口（详见[接口](interface.md)）中。需要注意的是，抽象实例成员函数默认具有 `open` 的语义，`open` 修饰符是可选的，且必须使用 `public` 或 `protected` 进行修饰。

非抽象函数必须有函数体，在函数体中可以通过 `this` 访问实例成员变量，例如：

<!-- compile -->

```cangjie
class Rectangle {
    let width: Int64 = 10
    let height: Int64 = 20

    public func area() {
        this.width * this.height
    }
}
```