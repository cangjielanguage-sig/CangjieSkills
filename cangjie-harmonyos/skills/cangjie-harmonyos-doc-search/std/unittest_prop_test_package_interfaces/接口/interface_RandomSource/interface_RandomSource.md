## interface RandomSource

```cangjie
public interface RandomSource {
    func nextBool(): Bool
    func nextInt8(): Int8
    func nextInt16(): Int16
    func nextInt32(): Int32
    func nextInt64(): Int64
    func nextInt8(max: Int8): Int8
    func nextInt16(max: Int16): Int16
    func nextInt32(max: Int32): Int32
    func nextInt64(max: Int64): Int64
    func nextUInt8(): UInt8
    func nextUInt16(): UInt16
    func nextUInt32(): UInt32
    func nextUInt64(): UInt64
    func nextUInt8(max: UInt8): UInt8
    func nextUInt16(max: UInt16): UInt16
    func nextUInt32(max: UInt32): UInt32
    func nextUInt64(max: UInt64): UInt64
    func nextFloat16(): Float16
    func nextFloat32(): Float32
    func nextFloat64(): Float64
    func nextGaussianFloat64(mean!: Float64, sigma!: Float64): Float64
    func nextIntNative(): IntNative
    func nextUIntNative(): UIntNative

    func suggestUInt8(): UInt8
    func suggestUInt16(): UInt16
    func suggestUInt32(): UInt32
    func suggestUInt64(): UInt64
    func suggestUIntNative(): UIntNative
    func suggestInt8(): Int8
    func suggestInt16(): Int16
    func suggestInt32(): Int32
    func suggestInt64(): Int64
    func suggestIntNative(): IntNative
    func suggestFloat16(): Float16
    func suggestFloat32(): Float32
    func suggestFloat64(): Float64
    func suggestBool(): Bool
    func suggestRune(): Rune

    func suggestInt64(l: Int64, r: Int64): Int64
    func suggestUInt64(l: UInt64, r: UInt64): UInt64
    func suggestInt32(l: Int32, r: Int32): Int32
    func suggestUInt32(l: UInt32, r: UInt32): UInt32
    func suggestInt16(l: Int16, r: Int16): Int16
    func suggestUInt16(l: UInt16, r: UInt16): UInt16
    func suggestInt8(l: Int8, r: Int8): Int8
    func suggestUInt8(l: UInt8, r: UInt8): UInt8
    func suggestIntNative(l: IntNative, r: IntNative): IntNative
    func suggestUIntNative(l: UIntNative, r: UIntNative): UIntNative
    func suggestFloat64(l: Float64, r: Float64): Float64
    func suggestFloat32(l: Float32, r: Float32): Float32
    func suggestFloat16(l: Float16, r: Float16): Float16
}
```

功能：提供 [Arbitrary](#interface-arbitraryt) 所需的随机生成基础类型数据的能力。