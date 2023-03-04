from dovado_rtl.explorers.range import Range
from dovado_rtl.explorers.spaces import ContinuousSpace
import os
from pathlib import Path


def test_continuous_space():
    path_prexif: str = "../" + os.curdir + "/resources"

    toml_file = Path(path_prexif + "/exploration_files/neorv_exploration_file.toml")

    space = ContinuousSpace(toml_file)

    assert space.get_range(
        Path("core/neorv32_top.vhd"), "neorv32_top", "CPU_EXTENSION_RISCV_B"
    ) == Range([0, 1])

    assert space.get_range(
        Path("core/neorv32_top.vhd"), "neorv32_top", "PMP_NUM_REGIONS"
    ) == Range([0, 16])

    assert space.get_range(
        Path("core/neorv32_top.vhd"), "neorv32_top", "MEM_INT_IMEM_SIZE"
    ) == Range({"range": [1024, 16384], "step": "powers_of_two"})
