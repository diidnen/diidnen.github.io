# 群论基础

## 群的定义

群是一个集合 G 和一个二元运算 ∗，满足以下性质：
1. **封闭性**：对任意 a,b ∈ G，有 a ∗ b ∈ G
2. **结合律**：对任意 a,b,c ∈ G，有 (a ∗ b) ∗ c = a ∗ (b ∗ c)
3. **单位元**：存在 e ∈ G，使得对任意 a ∈ G，有 e ∗ a = a ∗ e = a
4. **逆元**：对任意 a ∈ G，存在 b ∈ G，使得 a ∗ b = b ∗ a = e

## 基本群的例子

### 数系群
- 整数集 ℤ 对加法构成群
- 有理数集 ℚ 对加法和乘法（除0外）构成群
- 实数集 ℝ 对加法和乘法（除0外）构成群
- 复数集 ℂ 对加法和乘法（除0外）构成群

### 重要的群
1. **一般线性群** GL(n,ℝ)
   - 由 n×n 可逆实矩阵组成
   - 运算为矩阵乘法

2. **对称群** Sₙ
   - 由 n 个元素的所有置换组成
   - 运算为函数复合

3. **二面体群** Dₙ
   - 由正 n 边形的对称变换组成
   - 包含旋转和翻转变换

## 群的基本性质

### 唯一性定理
1. 单位元是唯一的
2. 每个元素的逆元是唯一的

### 逆元性质
- (g⁻¹)⁻¹ = g
- (gh)⁻¹ = h⁻¹g⁻¹

## 群的表示

### 记号约定
- 通常省略群的运算符号 ∗，直接写作 gh
- 在加法群中使用加号 +
- 在乘法群中使用乘号 · 或省略

### 群表
- 用于表示有限群的运算关系
- 每行每列都包含群的所有元素恰好一次
- 单位元 e 在每行每列都有唯一对应

## 具体群例子

### 循环群
- ℤ₄：模4的整数加法群
- 元素：{0,1,2,3}
- 运算：模4加法

### 直积群
- (ℤ₂)²：两个ℤ₂的直积
- 元素：{(0,0), (0,1), (1,0), (1,1)}
- 运算：分量分别进行模2加法




















