# %% [markdown]
# # 张量
#
# 创建日期：2017年3月24日 | 最后更新：2026年5月12日 | 最后验证：2024年11月5日

# %%
import torch
import numpy as np

# %% [markdown]
# ## 张量初始化
#
# 直接从数据创建

# %%
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)

# %% [markdown]
# 从 NumPy 数组创建

# %%
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# %% [markdown]
# 从另一个张量创建

# %%
x_ones = torch.ones_like(x_data)  # retains the properties of x_data
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)  # overrides the datatype of x_data
print(f"Random Tensor: \n {x_rand} \n")

# %% [markdown]
# 使用随机值或常量值

# %%
shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")

# %% [markdown]
# ## 张量属性

# %%
tensor = torch.rand(3, 4)

print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

# %% [markdown]
# ## 张量运算
#
# 将张量移动到可用的加速设备上。

# %%
# We move our tensor to the GPU if available
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
tensor = tensor.to(device)
print(f"Device tensor is stored on: {tensor.device}")

# %% [markdown]
# 标准的类 NumPy 索引和切片

# %%
tensor = torch.ones(4, 4)
tensor[:, 1] = 0
print(tensor)

# %% [markdown]
# 拼接张量

# %%
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

# %% [markdown]
# 乘法运算

# %%
# This computes the element-wise product
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")

# Alternative syntax:
print(f"tensor * tensor \n {tensor * tensor}")

# %% [markdown]
# 这会计算两个张量之间的矩阵乘法

# %%
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")

# Alternative syntax:
print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

# %% [markdown]
# 原地操作（In-place operations）

# %%
print(tensor, "\n")
tensor.add_(5)
print(tensor)

# %% [markdown]
# ## 与 NumPy 的桥接
#
# ### 张量转 NumPy 数组

# %%
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

# %% [markdown]
# 张量的改变会反映在 NumPy 数组中。

# %%
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

# %% [markdown]
# ### NumPy 数组转张量

# %%
n = np.ones(5)
t = torch.from_numpy(n)

# %% [markdown]
# NumPy 数组的改变会反映在张量中。

# %%
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")
