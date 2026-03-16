import torch
import triton
import triton.language as tl


@triton.jit
def reverse_kernel(input, N, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(0)
    offsets = pid * BLOCK_SIZE + tl.arange(0, BLOCK_SIZE)
    
    mask = offsets < N // 2
    re_offsets = N - 1 - offsets
    A_ptr = tl.load(input + offsets, mask)
    B_ptr = tl.load(input + re_offsets, mask)

    tl.store(input + offsets, B_ptr, mask=mask)
    tl.store(input + re_offsets, A_ptr, mask=mask)
        



# input is a tensor on the GPU
def solve(input: torch.Tensor, N: int):
    BLOCK_SIZE = 1024
    n_blocks = triton.cdiv(N // 2, BLOCK_SIZE)
    grid = (n_blocks,)

    reverse_kernel[grid](input, N, BLOCK_SIZE)
