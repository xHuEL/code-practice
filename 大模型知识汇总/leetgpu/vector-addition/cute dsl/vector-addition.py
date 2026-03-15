import cutlass
import cutlass.cute as cute

@cute.kernel
def vector_add_kernel(A: cute.Tensor, B: cute.Tensor, C: cute.Tensor, N: cute.Int32):

    tidx, _, _ = cute.arch.thread_idx()
    bidx, _, _ = cute.arch.block_idx()
    bdim, _, _ = cute.arch.block_dim()

    thread_idx = bidx * bdim + tidx

    if thread_idx < N:
        idx = (thread_idx,)
        C[idx] = A[idx] + B[idx]

@cute.jit
def solve(A: cute.Tensor, B: cute.Tensor, C: cute.Tensor, N: cute.Int32):

    num_threads_per_block = 256
    grid_x = cute.ceil_div(N, num_threads_per_block)

    vector_add_kernel(A, B, C, N).launch(
        grid=(grid_x, 1, 1),
        block=(num_threads_per_block, 1, 1)
    )